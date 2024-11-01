# fiscus_sdk/client.py

import logging
import asyncio
from typing import Optional, Dict, Any, Callable, List

from fiscus.utility import _mask_sensitive_info
from fiscus.user import FiscusUser
from fiscus.response import FiscusResponse
from fiscus.audit import FiscusAuditTrail
from fiscus.connection import _ConnectionManager
from fiscus.orchestrator import _Orchestrator
from fiscus.ai_orchestrator import _AIOrchestrator
from fiscus.enums import (
	FiscusConnectionType,
	FiscusResponseType,
	FiscusInitType,
	FiscusLogLevel,
	FiscusActionType,
	FiscusExecutionType,
	FiscusMemoryRetrievalType,
	FiscusMemoryStorageType,
	FiscusLLMType,
	FiscusCallbackType
)
from .callbacks import (
	FiscusCallback
)


class FiscusClient:
	"""
	The main entry point to the Fiscus SDK.
	
	Provides methods to initialize connections, execute operations, and manage user actions.
	Supports both synchronous and asynchronous operations based on the initialization mode.
	"""

	def __init__(
		self,
		api_key: str,
		user_id: Optional[str] = None,
		logging_level: Optional[FiscusLogLevel] = None,
		log_to_file: bool = False,
		log_file_path: Optional[str] = None,
		enable_audit_logging: bool = False,
		connection_type: FiscusConnectionType = FiscusConnectionType.WEBSOCKET,
		response_format: FiscusResponseType = FiscusResponseType.JSON,
		retries: int = 3,
		backoff_factor: float = 0.5,
		context_loader: Optional[Callable[[], Dict[str, Any]]] = None,
		context_saver: Optional[Callable[[Dict[str, Any]], None]] = None,
		initialization_mode: FiscusInitType = FiscusInitType.LAZY,
		initialization_async: bool = False,
		llm: Any = None,
		memory: Any = None,
		**kwargs,
	):
		"""
		Initialize the FiscusClient with the provided configuration.

		:param api_key: API key for authenticating requests.
		:param user_id: Optional user ID for user-specific operations.
		:param logging_level: Optional logging level from FiscusLogLevel enum.
		:param log_to_file: Whether to log to a file instead of the console.
		:param log_file_path: Path to the log file if log_to_file is True.
		:param enable_audit_logging: Enable or disable audit trail logging.
		:param connection_type: Type of connection to use (e.g., WEBSOCKET).
		:param response_format: Format of the responses (e.g., TEXT).
		:param retries: Number of retries for failed operations.
		:param backoff_factor: Factor for exponential backoff between retries.
		:param context_loader: Optional callable to load user context.
		:param context_saver: Optional callable to save user context.
		:param initialization_mode: Mode of initialization (LAZY or EAGER).
		:param initialization_async: Whether to initialize asynchronously.
		:param kwargs: Additional custom options.
		"""
		# Store initialization parameters
		self.api_key = api_key
		self.user_id = user_id
		self.enable_audit_logging = enable_audit_logging

		# Initialize audit trail for logging actions
		self.audit_trail = FiscusAuditTrail(
			'FiscusClient', enable_logging=self.enable_audit_logging
		)

		# Configure logging based on provided parameters
		self._configure_logging(logging_level, log_to_file, log_file_path)

		# Store connection and response configurations
		self.connection_type = connection_type
		self.response_format = response_format
		self.retries = retries
		self.backoff_factor = backoff_factor
		self.context_loader = context_loader
		self.context_saver = context_saver
		self.custom_options: Dict[str, Any] = kwargs.get('custom_options', {})
		self.initialization_mode = initialization_mode
		self.initialization_async = initialization_async

		# Initialize default LLM and memory
		self.llm = llm
		self.memory = memory

		# Log client initialization
		self.logger.info("FiscusClient initialized with provided configuration.")

		# Initialize the connection manager with the API key
		self.connection_manager = _ConnectionManager(api_key=self.api_key)
		self.logger.debug("Connection manager initialized successfully.")

		# Initialize orchestrator to manage operations, whether user_id is provided or not
		self.orchestrator = _Orchestrator(
			user=None,  # Initialize without a user initially
			connection_manager=self.connection_manager,
			client=self,
		)
		self.logger.debug("Orchestrator initialized without user context.")

		# If a user_id is provided, initialize the user context and update the orchestrator
		if self.user_id is not None:
			self.logger.debug("User ID provided; initializing user context.")
			self.user = FiscusUser(user_id=self.user_id, client=self)
			if self.context_loader:
				self.user.context = self.context_loader()
				self.logger.debug("User context loaded successfully.")
			# Update the orchestrator with the new user context
			self.orchestrator.user = self.user
			self.logger.debug("Orchestrator updated with user context.")
		else:
			self.logger.warning("User ID not provided; some features may be limited.")
			self.user = None

		# Handle eager initialization based on the initialization mode
		if self.initialization_mode == FiscusInitType.EAGER:
			if self.initialization_async:
				self.logger.debug(
					"Eager asynchronous initialization selected. Please call 'await initialize_async()' after creating the client."
				)
			else:
				self.logger.debug(
					"Eager synchronous initialization selected. Initializing now."
				)
				self.initialize()

	def _configure_logging(
		self, level: Optional[FiscusLogLevel], log_to_file: bool, log_file_path: Optional[str]
	) -> None:
		"""
		Configure the logging for the FiscusClient.
		"""
		# Initialize root logger for 'fiscus_sdk'
		logger_name = 'fiscus_sdk'
		self.logger = logging.getLogger(logger_name)

		if level is None:
			# Disable logging for this logger and all its children
			self.logger.disabled = True
			self.logger.debug("Logging disabled for 'fiscus_sdk' and all its child loggers.")
		else:
			numeric_level = level.to_logging_level()
			self.logger.setLevel(numeric_level)

			# Remove any existing handlers to prevent duplicate logs
			if self.logger.hasHandlers():
				self.logger.handlers.clear()

			# Set up handler
			if log_to_file and log_file_path:
				handler = logging.FileHandler(log_file_path)
				self.logger.debug(f"Logging to file: {log_file_path}")
			else:
				handler = logging.StreamHandler()
				self.logger.debug("Logging to console.")

			handler.setLevel(numeric_level)
			formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
										datefmt='%Y-%m-%d %H:%M:%S')
			handler.setFormatter(formatter)
			self.logger.addHandler(handler)

			# Set 'websocket' logger level to prevent unwanted logs
			websocket_logger = logging.getLogger('fiscus.websocket')
			websocket_logger.setLevel(logging.CRITICAL + 1)
			self.logger.debug("'websocket' module logging level set to CRITICAL+1 to suppress logs.")

	def initialize(self) -> None:
		"""
		Eagerly initialize resources synchronously.
		"""
		self.logger.debug("Starting synchronous initialization.")
		if self.connection_type == FiscusConnectionType.WEBSOCKET:
			if not self.user_id:
				self.logger.debug(
					"User ID not provided; WebSocket initialization deferred until execution."
				)
			else:
				self.logger.info("Starting synchronous WebSocket connection.")
				try:
					self.connection_manager.start_websocket_connection_sync(self.user_id)
					self.logger.info("Synchronous WebSocket connection established successfully.")
				except Exception as e:
					self.logger.critical(f"Failed to establish synchronous WebSocket connection: {e}", exc_info=True)
		self.logger.debug("Synchronous initialization complete.")

	async def initialize_async(self) -> None:
		"""
		Eagerly initialize resources asynchronously.
		"""
		self.logger.debug("Starting asynchronous initialization.")
		if self.connection_type == FiscusConnectionType.WEBSOCKET:
			if not self.user_id:
				self.logger.debug(
					"User ID not provided; WebSocket initialization deferred until execution."
				)
			else:
				self.logger.info("Starting asynchronous WebSocket connection.")
				try:
					await self.connection_manager.start_websocket_connection(self.user_id)
					self.logger.info("Asynchronous WebSocket connection established successfully.")
				except Exception as e:
					self.logger.critical(f"Failed to establish asynchronous WebSocket connection: {e}", exc_info=True)
		self.logger.debug("Asynchronous initialization complete.")
		
	def _invoke_callback(self, callback: Callable, response: FiscusResponse) -> None:
		"""
		Simplified callback invocation: passes result data or error message.
		"""
		if response.success:
			# If it's a single result, pass that; otherwise, pass the entire batch of results
			result_data = response.result if not response._is_batch else response.results
			callback(result_data)  # Pass only the result data
		else:
			callback({'error': response.error_message})  # Pass error message


	def _handle_response(self, response: FiscusResponse, callbacks: Optional[Dict[str, Callable]] = None):
		"""
		Handles response by invoking the appropriate callbacks.
		If no callbacks are provided, simply return or log the result.
		"""
		# Check if callbacks are provided before proceeding
		if callbacks:
			if response.success:
				success_callback = callbacks.get('fiscus_on_success')
				if success_callback:
					self._invoke_callback(success_callback, response)
			else:
				error_callback = callbacks.get('fiscus_on_error')
				if error_callback:
					self._invoke_callback(error_callback, response)
		else:
			# If no callbacks are provided, you can log or handle the response as needed
			if response.success:
				self.logger.debug(f"Operation successful, result: {response.result or response.results}")
			else:
				self.logger.error(f"Operation failed with error: {response.error_message}")

	def execute(
		self,
		connector_name: Optional[str] = None,
		operation: Optional[str] = None,
		params: Optional[Dict[str, Any]] = None,
		callbacks: Optional[Dict[str, FiscusCallback]] = None,
		custom_options: Optional[Dict[str, Any]] = None,
		tasks: Optional[List[Dict[str, Any]]] = None,
		connection_type: Optional[FiscusConnectionType] = None,
		response_format: Optional[FiscusResponseType] = None,
		user: Optional[FiscusUser] = None,
	) -> FiscusResponse:
		"""
		Execute one or more operations synchronously.

		:param connector_name: Name of the connector to use.
		:param operation: Specific operation to perform.
		:param params: Parameters for the operation.
		:param callbacks: Callbacks to handle responses.
		:param custom_options: Custom options for the operation.
		:param tasks: List of tasks to execute.
		:param connection_type: Type of connection to use.
		:param response_format: Format of the response.
		:param user: FiscusUser instance to perform the operation.
		:return: FiscusResponse object containing the result.
		"""
		self.logger.debug("Executing synchronous operation.")

		if connection_type is None:
			connection_type = self.connection_type
		if response_format is None:
			response_format = self.response_format
		if params is None:
			params = {}

		if not user and not self.user:
			self.logger.error("User instance must be provided for execution.")
			raise ValueError("A FiscusUser instance must be provided.")
		current_user = user or self.user

		if not current_user.user_id:
			self.logger.critical("User instance with a user_id must be provided.")
			raise ValueError("A FiscusUser instance with a user_id must be provided.")

		if not self.orchestrator:
			self.logger.debug("Creating orchestrator.")
			self.orchestrator = _Orchestrator(
				user=current_user, connection_manager=self.connection_manager, client=self
			)
			self.logger.debug("Orchestrator created successfully.")

		if tasks and isinstance(tasks, list):
			self.logger.info("Executing multiple synchronous tasks.")
			# Execute multiple tasks and handle responses
			responses = []
			for task in tasks:
				response = self.orchestrator._execute_operation(
					connector_name=task.get("connector"),
					operation=task.get("operation"),
					params=task.get("params"),
					callbacks=task.get("callbacks", callbacks),
					custom_options=custom_options,
					connection_type=connection_type,
					response_format=response_format,
					user=current_user,
				)
				responses.append(response)

				# Callbacks per task
				if task.get("callbacks"):
					self._handle_response(response, task.get("callbacks"))

			# Return aggregated results as FiscusResponse
			return FiscusResponse(success=True, result=responses)

		elif connector_name and operation:
			self.logger.info(f"Executing synchronous operation: Connector='{connector_name}', Operation='{operation}'.")
			# Execute a single operation and handle responses
			response = self.orchestrator._execute_operation(
				connector_name=connector_name,
				operation=operation,
				params=params,
				callbacks=callbacks,
				custom_options=custom_options,
				connection_type=connection_type,
				response_format=response_format,
				user=current_user,
			)
			self._handle_response(response, callbacks)
			return response
		else:
			self.logger.error("Invalid parameters provided for execution.")
			raise ValueError(
				"Either 'tasks' or both 'connector_name' and 'operation' must be provided."
			)

	async def execute_async(
		self,
		connector_name: Optional[str] = None,
		operation: Optional[str] = None,
		params: Optional[Dict[str, Any]] = None,
		callbacks: Optional[Dict[str, FiscusCallback]] = None,
		custom_options: Optional[Dict[str, Any]] = None,
		tasks: Optional[List[Dict[str, Any]]] = None,
		connection_type: Optional[FiscusConnectionType] = None,
		response_format: Optional[FiscusResponseType] = None,
		user: Optional[FiscusUser] = None,
	) -> FiscusResponse:
		"""
		Execute one or more operations asynchronously.

		:param connector_name: Name of the connector to use.
		:param operation: Specific operation to perform.
		:param params: Parameters for the operation.
		:param callbacks: Callbacks to handle responses.
		:param custom_options: Custom options for the operation.
		:param tasks: List of tasks to execute.
		:param connection_type: Type of connection to use.
		:param response_format: Format of the response.
		:param user: FiscusUser instance to perform the operation.
		:return: FiscusResponse object containing the result.
		"""
		self.logger.debug("Executing asynchronous operation.")

		if connection_type is None:
			connection_type = self.connection_type
		if response_format is None:
			response_format = self.response_format
		if params is None:
			params = {}

		if not user and not self.user:
			self.logger.error("User instance must be provided for asynchronous execution.")
			raise ValueError("A FiscusUser instance must be provided.")
		current_user = user or self.user

		if not current_user.user_id:
			self.logger.critical("User instance with a user_id must be provided.")
			raise ValueError("A FiscusUser instance with a user_id must be provided.")

		if not self.orchestrator:
			self.logger.debug("Creating orchestrator for asynchronous execution.")
			self.orchestrator = _Orchestrator(
				user=current_user, connection_manager=self.connection_manager, client=self
			)
			self.logger.debug("Orchestrator created successfully.")

		if tasks and isinstance(tasks, list):
			self.logger.info("Executing multiple asynchronous tasks.")
			responses = []
			for task in tasks:
				response = await self.orchestrator._execute_operation_async(
					connector_name=task.get("connector"),
					operation=task.get("operation"),
					params=task.get("params"),
					callbacks=task.get("callbacks", callbacks),
					custom_options=custom_options,
					connection_type=connection_type,
					response_format=response_format,
					user=current_user,
				)
				responses.append(response)

				# Callbacks per task
				if task.get("callbacks"):
					self._handle_response(response, task.get("callbacks"))

			# Return aggregated results as FiscusResponse
			return FiscusResponse(success=True, result=responses)

		elif connector_name and operation:
			self.logger.info(f"Executing asynchronous operation: Connector='{connector_name}', Operation='{operation}'.")
			# Execute a single operation and handle responses
			response = await self.orchestrator._execute_operation_async(
				connector_name=connector_name,
				operation=operation,
				params=params,
				callbacks=callbacks,
				custom_options=custom_options,
				connection_type=connection_type,
				response_format=response_format,
				user=current_user,
			)
			self._handle_response(response, callbacks)
			return response
		else:
			self.logger.error("Invalid parameters provided for asynchronous execution.")
			raise ValueError(
				"Either 'tasks' or both 'connector_name' and 'operation' must be provided."
			)

	def execute_ai(
		self,
		input: str,
		llm_type: FiscusLLMType,
		llm: Any = None,
		memory: Any = None,
		callbacks: Optional[Dict[FiscusCallbackType, FiscusCallback]] = None,  # Use FiscusCallbackType as keys
		custom_overrides: Optional[Dict[str, Any]] = None,
		connection_type: Optional[FiscusConnectionType] = None,
		response_format: Optional[FiscusResponseType] = None,
		user: Optional[FiscusUser] = None,
		custom_prompt_template: Optional[str] = None,
		preprocess_function: Optional[Callable[[str], str]] = None,
		postprocess_function: Optional[Callable[[FiscusResponse], Any]] = None,
		custom_options: Optional[Dict[str, Any]] = None,
		execution_mode: FiscusExecutionType = FiscusExecutionType.SEQUENTIAL,
		error_callback: Optional[Callable[[Exception], None]] = None,
		decision_logic_override: Optional[Callable[[str], List[Dict[str, Any]]]] = None,
		memory_retrieval_logic: Optional[Callable[[str], str]] = None,
		memory_storage_logic: Optional[Callable[[Any], None]] = None,
		few_shot_examples: Optional[Dict[str, List[str]]] = None,
		embedding_model: Optional[Any] = None,
		indexing_algorithm: Optional[str] = None,
		retrieval_strategy: FiscusMemoryRetrievalType = FiscusMemoryRetrievalType.SEMANTIC_SEARCH,
		storage_strategy: FiscusMemoryStorageType = FiscusMemoryStorageType.APPEND,
	) -> FiscusResponse:
		"""
		Execute AI-based dynamic workflow based on user input synchronously, with AI-specific callbacks at each stage.
		"""
		self.logger.info("Starting synchronous AI execution.")
		self.logger.debug(f"Input: {input}")
		self.logger.debug(f"LLM Type: {llm_type}")

		if connection_type is None:
			connection_type = self.connection_type
		if response_format is None:
			response_format = self.response_format

		if not user and not self.user:
			self.logger.error("User instance must be provided for AI execution.")
			raise ValueError("A FiscusUser instance must be provided.")
		current_user = user or self.user

		if not current_user.user_id:
			self.logger.fatal("User instance with a user_id must be provided for AI execution.")
			raise ValueError("A FiscusUser instance with a user_id must be provided.")

		if llm is None:
			llm = self.llm
		if memory is None:
			memory = self.memory

		# Initialize ai_callbacks using FiscusCallbackType enums
		ai_callbacks = {
			callback_type.value: callbacks.get(callback_type, globals().get(callback_type.name)) 
			if callbacks else globals().get(callback_type.name)
			for callback_type in FiscusCallbackType
			if "AI" in callback_type.name  # Filter for only AI-related callbacks
		}

		# Log the initialization of AIOrchestrator
		self.logger.debug("Initializing AIOrchestrator with provided parameters.")

		# Initialize AIOrchestrator with AI-specific callbacks
		ai_orchestrator = _AIOrchestrator(
			client=self,
			user=current_user,
			llm=llm,
			llm_type=llm_type,
			memory=memory,
			custom_prompt_template=custom_prompt_template,
			preprocess_function=preprocess_function,
			postprocess_function=postprocess_function,
			custom_options=custom_options,
			error_callback=error_callback,
			decision_logic_override=decision_logic_override,
			memory_retrieval_logic=memory_retrieval_logic,
			memory_storage_logic=memory_storage_logic,
			few_shot_examples=few_shot_examples,
			embedding_model=embedding_model,
			indexing_algorithm=indexing_algorithm,
			retrieval_strategy=retrieval_strategy,
			storage_strategy=storage_strategy,
			ai_callbacks=ai_callbacks,  # Pass AI-specific callbacks to orchestrator
		)

		# Run AIOrchestrator
		self.logger.info("Running AIOrchestrator synchronously.")
		response = ai_orchestrator.run(
			input_text=input,
			connection_type=connection_type,
			response_format=response_format,
			execution_mode=execution_mode,
		)

		# Log the response from AIOrchestrator
		if response.success:
			self.logger.info("AIOrchestrator run completed successfully.")
		else:
			self.logger.error(f"AIOrchestrator run failed with error: {response.error}")

		self.logger.debug(f"Response from AIOrchestrator: {_mask_sensitive_info(response.data)}")

		if self.context_saver:
			try:
				self.context_saver(current_user.context)
				self.logger.debug("User context saved successfully after AI execution.")
			except Exception as e:
				self.logger.error(f"Failed to save user context after AI execution: {e}", exc_info=True)

		return response

	async def execute_ai_async(
		self,
		input: str,
		llm_type: FiscusLLMType,
		llm: Any = None,
		memory: Any = None,
		callbacks: Optional[Dict[FiscusCallbackType, FiscusCallback]] = None,  # Use FiscusCallbackType as keys
		custom_overrides: Optional[Dict[str, Any]] = None,
		connection_type: Optional[FiscusConnectionType] = None,
		response_format: Optional[FiscusResponseType] = None,
		user: Optional[FiscusUser] = None,
		custom_prompt_template: Optional[str] = None,
		preprocess_function: Optional[Callable[[str], str]] = None,
		postprocess_function: Optional[Callable[[FiscusResponse], Any]] = None,
		custom_options: Optional[Dict[str, Any]] = None,
		execution_mode: FiscusExecutionType = FiscusExecutionType.SEQUENTIAL,
		error_callback: Optional[Callable[[Exception], None]] = None,
		decision_logic_override: Optional[Callable[[str], List[Dict[str, Any]]]] = None,
		memory_retrieval_logic: Optional[Callable[[str], str]] = None,
		memory_storage_logic: Optional[Callable[[Any], None]] = None,
		few_shot_examples: Optional[Dict[str, List[str]]] = None,
		embedding_model: Optional[Any] = None,
		indexing_algorithm: Optional[str] = None,
		retrieval_strategy: FiscusMemoryRetrievalType = FiscusMemoryRetrievalType.SEMANTIC_SEARCH,
		storage_strategy: FiscusMemoryStorageType = FiscusMemoryStorageType.APPEND,
	) -> FiscusResponse:
		"""
		Asynchronously execute AI-based dynamic workflow based on user input, with AI-specific callbacks at each stage.
		"""
		self.logger.info("Starting asynchronous AI execution.")
		self.logger.debug(f"Input: {input}")
		self.logger.debug(f"LLM Type: {llm_type}")

		if connection_type is None:
			connection_type = self.connection_type
		if response_format is None:
			response_format = self.response_format

		if not user and not self.user:
			self.logger.error("User instance must be provided for asynchronous AI execution.")
			raise ValueError("A FiscusUser instance must be provided.")
		current_user = user or self.user

		if not current_user.user_id:
			self.logger.fatal("User instance with a user_id must be provided for asynchronous AI execution.")
			raise ValueError("A FiscusUser instance with a user_id must be provided.")

		if llm is None:
			llm = self.llm
		if memory is None:
			memory = self.memory

		# Initialize ai_callbacks using FiscusCallbackType enums
		ai_callbacks = {
			callback_type.value: callbacks.get(callback_type, globals().get(callback_type.name)) 
			if callbacks else globals().get(callback_type.name)
			for callback_type in FiscusCallbackType
			if "AI" in callback_type.name  # Filter for only AI-related callbacks
		}

		# Log the initialization of AIOrchestrator
		self.logger.debug("Initializing AIOrchestrator with provided parameters.")

		# Initialize AIOrchestrator with AI-specific callbacks
		ai_orchestrator = _AIOrchestrator(
			client=self,
			user=current_user,
			llm=llm,
			llm_type=llm_type,
			memory=memory,
			custom_prompt_template=custom_prompt_template,
			preprocess_function=preprocess_function,
			postprocess_function=postprocess_function,
			custom_options=custom_options,
			error_callback=error_callback,
			decision_logic_override=decision_logic_override,
			memory_retrieval_logic=memory_retrieval_logic,
			memory_storage_logic=memory_storage_logic,
			few_shot_examples=few_shot_examples,
			embedding_model=embedding_model,
			indexing_algorithm=indexing_algorithm,
			retrieval_strategy=retrieval_strategy,
			storage_strategy=storage_strategy,
			ai_callbacks=ai_callbacks,  # Pass AI-specific callbacks to orchestrator
		)

		# Run AIOrchestrator asynchronously
		self.logger.info("Running AIOrchestrator asynchronously.")
		response = await ai_orchestrator.run_async(
			input_text=input,
			connection_type=connection_type,
			response_format=response_format,
			execution_mode=execution_mode,
		)

		# Log the response from AIOrchestrator
		if response.success:
			self.logger.info("AIOrchestrator asynchronous run completed successfully.")
		else:
			self.logger.error(f"AIOrchestrator asynchronous run failed with error: {response.error}")

		self.logger.debug(f"Response from AIOrchestrator: {_mask_sensitive_info(response.result)}")

		if self.context_saver:
			try:
				self.context_saver(current_user.context)
				self.logger.debug("User context saved successfully after asynchronous AI execution.")
			except Exception as e:
				self.logger.error(f"Failed to save user context after asynchronous AI execution: {e}", exc_info=True)

		return response

	def stop_stream(self) -> None:
		"""
		Stop the WebSocket stream.
		"""
		self.logger.info("Stopping WebSocket stream.")
		if self.initialization_async:
			try:
				asyncio.run(self.connection_manager.stop_websocket_connection())
				self.logger.debug("WebSocket connection stopped asynchronously.")
			except Exception as e:
				self.logger.error(f"Failed to stop asynchronous WebSocket connection: {e}", exc_info=True)
		else:
			try:
				self.connection_manager.stop_websocket_connection_sync()
				self.logger.debug("WebSocket connection stopped synchronously.")
			except Exception as e:
				self.logger.error(f"Failed to stop synchronous WebSocket connection: {e}", exc_info=True)
		self.logger.info("WebSocket stream stopped.")

	def restart_stream(self) -> None:
		"""
		Restart the WebSocket stream.
		"""
		self.logger.info("Restarting WebSocket stream.")
		if self.initialization_async:
			try:
				asyncio.run(
					self.connection_manager.restart_websocket_connection(self.user_id)
				)
				self.logger.debug("WebSocket connection restarted asynchronously.")
			except Exception as e:
				self.logger.error(f"Failed to restart asynchronous WebSocket connection: {e}", exc_info=True)
		else:
			try:
				self.connection_manager.restart_websocket_connection_sync(self.user_id)
				self.logger.debug("WebSocket connection restarted synchronously.")
			except Exception as e:
				self.logger.error(f"Failed to restart synchronous WebSocket connection: {e}", exc_info=True)
		self.logger.info("WebSocket stream restarted.")

	def user_action(
		self,
		action: FiscusActionType,
		params: Optional[Dict[str, Any]] = None,
		user: Optional[FiscusUser] = None,
		connection_type: Optional[FiscusConnectionType] = None,
		response_format: Optional[FiscusResponseType] = None,
	) -> FiscusResponse:
		"""
		Execute a user action synchronously.

		:param action: The action to perform.
		:param params: Parameters for the action.
		:param user: FiscusUser instance to perform the action.
		:param connection_type: Type of connection to use.
		:param response_format: Format of the response.
		:return: FiscusResponse object containing the result.
		"""
		self.logger.debug(f"Executing synchronous user action: {action}")

		if connection_type is None:
			connection_type = self.connection_type
		if response_format is None:
			response_format = self.response_format
		if params is None:
			params = {}

		if not user and not self.user:
			self.logger.error("User instance must be provided for user action.")
			raise ValueError("A FiscusUser instance must be provided.")
		current_user = user or self.user

		if not current_user.user_id:
			self.logger.critical("User instance with a user_id must be provided for user action.")
			raise ValueError("A FiscusUser instance with a user_id must be provided.")

		data = {'action': action, 'params': params or {}}
		self.logger.debug("User action payload prepared.")

		if not self.orchestrator:
			self.logger.debug("Creating orchestrator for user action.")
			self.orchestrator = _Orchestrator(
				user=current_user, connection_manager=self.connection_manager, client=self
			)
			self.logger.debug("Orchestrator created successfully.")

		try:
			response = self.orchestrator._send_operation_to_server(
				action=FiscusActionType.USER,
				data=data,
				response_format=response_format,
				connection_type=connection_type,
				custom_options=None,
				user=current_user,
			)
			self.logger.info(f"User action '{action}' executed successfully.")
		except Exception as e:
			self.logger.critical(f"User action '{action}' failed: {e}", exc_info=True)
			raise e

		return response

	async def user_action_async(
		self,
		action: FiscusActionType,
		params: Optional[Dict[str, Any]] = None,
		user: Optional[FiscusUser] = None,
		connection_type: Optional[FiscusConnectionType] = None,
		response_format: Optional[FiscusResponseType] = None,
	) -> FiscusResponse:
		"""
		Execute a user action asynchronously.

		:param action: The action to perform.
		:param params: Parameters for the action.
		:param user: FiscusUser instance to perform the action.
		:param connection_type: Type of connection to use.
		:param response_format: Format of the response.
		:return: FiscusResponse object containing the result.
		"""
		self.logger.debug(f"Asynchronously executing user action: {action}")

		if connection_type is None:
			connection_type = self.connection_type
		if response_format is None:
			response_format = self.response_format
		if params is None:
			params = {}

		if not user and not self.user:
			self.logger.error("User instance must be provided for asynchronous user action.")
			raise ValueError("A FiscusUser instance must be provided.")
		current_user = user or self.user

		if not current_user.user_id:
			self.logger.critical("User instance with a user_id must be provided for asynchronous user action.")
			raise ValueError("A FiscusUser instance with a user_id must be provided.")

		data = {'action': action, 'params': params or {}}
		self.logger.debug("Asynchronous user action payload prepared.")

		if not self.orchestrator:
			self.logger.debug("Creating orchestrator for asynchronous user action.")
			self.orchestrator = _Orchestrator(
				user=current_user, connection_manager=self.connection_manager, client=self
			)
			self.logger.debug("Orchestrator created successfully.")

		try:
			response = await self.orchestrator._send_operation_to_server_async(
				action=FiscusActionType.USER,
				data=data,
				response_format=response_format,
				connection_type=connection_type,
				custom_options=None,
				user=current_user,
			)
			self.logger.info(f"Asynchronous user action '{action}' executed successfully.")
		except Exception as e:
			self.logger.critical(f"Asynchronous user action '{action}' failed: {e}", exc_info=True)
			raise e

		return response

	def _mask_sensitive_info(self, info: str) -> str:
		"""
		Masks sensitive information in logs to prevent exposure.

		:param info: The sensitive information string.
		:return: Masked string.
		"""
		if not info:
			return ""
		return f"{info[:4]}****{info[-4:]}"

# ai_orchestrator.py

import logging
import asyncio
import json
import time
from typing import TYPE_CHECKING, Optional, Dict, Any, List, Callable

from fiscus.orchestrator import _Orchestrator
from fiscus.utility import _mask_sensitive_info
from fiscus.response import FiscusResponse, FiscusError, FiscusErrorCode
from fiscus.user import FiscusUser
from fiscus.audit import FiscusAuditTrail
from fiscus.llm_adapter import _LLMAdapter
from fiscus.llm_config import _LLMConfig
from fiscus.category_few_shot import category_few_shot_examples
from fiscus.connector_few_shot import connector_few_shot_examples
from fiscus.operation_few_shot import operation_few_shot_examples
from fiscus.task_few_shot import task_few_shot_examples
from fiscus.enums import (
	FiscusConnectionType,
	FiscusResponseType,
	FiscusExecutionType,
	FiscusMemoryRetrievalType,
	FiscusMemoryStorageType,
	FiscusLLMType,
	FiscusCallbackType,
)
from .callbacks import (
	FiscusCallback
)

if TYPE_CHECKING:
	from .client import FiscusClient


class _AIOrchestrator:
	def __init__(
		self,
		client: 'FiscusClient',
		user: FiscusUser,
		llm: Any,
		llm_type: FiscusLLMType,
		memory: Any = None,
		custom_prompt_template: Optional[str] = None,
		preprocess_function: Optional[Callable[[str], str]] = None,
		postprocess_function: Optional[Callable[[FiscusResponse], Any]] = None,
		custom_options: Optional[Dict[str, Any]] = None,
		error_callback: Optional[Callable[[Exception], None]] = None,
		decision_logic_override: Optional[Callable[[str], List[Dict[str, Any]]]] = None,
		memory_retrieval_logic: Optional[Callable[[str], str]] = None,
		memory_storage_logic: Optional[Callable[[Any], None]] = None,
		few_shot_examples: Optional[Dict[str, List[Dict[str, str]]]] = None,
		embedding_model: Optional[Any] = None,
		indexing_algorithm: Optional[str] = None,
		retrieval_strategy: FiscusMemoryRetrievalType = FiscusMemoryRetrievalType.SEMANTIC_SEARCH,
		storage_strategy: FiscusMemoryStorageType = FiscusMemoryStorageType.APPEND,
		ai_callbacks: Optional[Dict[str, FiscusCallback]] = None
	):
		self.client = client
		self.user = user
		self.llm = llm
		self.llm_type = llm_type  # Store llm_type
		self.memory = memory
		self.custom_prompt_template = custom_prompt_template
		self.preprocess_function = preprocess_function
		self.postprocess_function = postprocess_function
		self.custom_options = custom_options or {}
		self.error_callback = error_callback
		self.decision_logic_override = decision_logic_override
		self.memory_retrieval_logic = memory_retrieval_logic
		self.memory_storage_logic = memory_storage_logic
		self.few_shot_examples = few_shot_examples or {}
		self.embedding_model = embedding_model
		self.indexing_algorithm = indexing_algorithm or 'hnsw'
		self.retrieval_strategy = retrieval_strategy
		self.storage_strategy = storage_strategy
		self.llm_config = _LLMConfig()  # Initialize configuration class

		# Load AI-specific callbacks, defaulting to those in callbacks.py
		# Initialize ai_callbacks, using .value for consistency in lookup
		self.ai_callbacks = {
			callback_type.value: ai_callbacks.get(callback_type.value, globals().get(callback_type.name))
			for callback_type in FiscusCallbackType
			if "AI" in callback_type.name  # Only AI-specific callbacks
		}

		# Conditionally set the logger based on user_id availability
		if self.user and self.user.user_id:
			logger_name = f"fiscus.ai_orchestrator.{self.user.user_id}"
		else:
			logger_name = "fiscus.ai_orchestrator.unknown"
		self.logger = logging.getLogger(logger_name)

		# Configure logger based on client's logging settings
		self._configure_logging()

		# Initialize orchestrator class
		self.orchestrator = self.client.orchestrator

		# Initialize _LLMAdapter
		self.llm_adapter = _LLMAdapter(
			llm=self.llm,
			llm_type=self.llm_type,
			logger=self.logger,
			error_callback=self.error_callback
		)

		self.logger.info("AIOrchestrator initialized successfully.")

		# Initialize audit trail for logging actions
		self.audit_trail = FiscusAuditTrail(
			f"AIOrchestrator_{self.user.user_id}",
			enable_logging=self.client.enable_audit_logging,
		)

	def _configure_logging(self) -> None:
		"""
		Configure the logging for the AIOrchestrator.

		Sets up the logger with appropriate handlers and formatters based on the client's configuration.
		Ensures that logs are consistent with other SDK components.
		"""
		# Inherit logging level and handlers from the client's logger
		self.logger.setLevel(self.client.logger.level)

		# Prevent adding multiple handlers if they already exist
		if not self.logger.hasHandlers():
			for handler in self.client.logger.handlers:
				self.logger.addHandler(handler)

		self.logger.debug("Logging configured for AIOrchestrator.")

	# Helper method to trigger callback methods
	def _trigger_callback(self, callback_type: FiscusCallbackType, data: Dict[str, Any]):
		"""Helper method to trigger a callback if it exists in ai_callbacks."""
		callback = self.ai_callbacks.get(callback_type.value)  # Use .value for lookup consistency
		if callback:
			self.logger.debug(f"Triggering callback '{callback_type.value}' with data: {data}")
			callback(data)

	def process_input(self, input_text: str) -> List[Dict[str, Any]]:
		"""
		Process user input to generate a list of tasks based on LLM reasoning.
		This involves querying the LLM and accessing memory.
		"""
		# Preprocess input if necessary
		if self.preprocess_function:
			input_text = self.preprocess_function(input_text)

		# Retrieve context from memory if necessary
		context = ""
		if self.memory:
			context = self.retrieve_memory(input_text)

		# Classify the input into categories
		categories = self.classify_input(input_text, context)

		if categories is None or not categories:
			self.logger.warning("No categories identified by LLM.")
			if self.error_callback:
				self.error_callback(Exception("No categories identified for the input."))
			# Optionally return an error response or handle accordingly
			return []

		# Select connectors based on categories
		connectors = self.select_connectors(input_text, categories, context)

		if not connectors:
			self.logger.warning("No connectors identified by LLM.")
			if self.error_callback:
				self.error_callback(Exception("No connectors identified for the categories."))
			return []

		# Select operations based on selected connectors
		connectors_operations = self.select_operations(connectors, input_text, context)

		if not connectors_operations:
			self.logger.warning("No operations identified for selected connectors.")
			if self.error_callback:
				self.error_callback(Exception("No operations identified for the selected connectors."))
			return []

		# Plan out the tasks to perform
		tasks = self.plan_tasks(input_text, connectors_operations, context)

		if not tasks:
			self.logger.warning("No tasks planned by LLM.")
			if self.error_callback:
				self.error_callback(Exception("No tasks could be planned based on the connectors and operations."))
			return []

		return tasks

	# Load few shot exmaples
	def _load_categories_few_shot(self) -> List[Dict[str, Any]]:
		"""
		Load the categories few shot examples from categories_few_shot.py.
		"""
		return category_few_shot_examples
	
	def _load_connectors_few_shot(self) -> List[Dict[str, Any]]:
		"""
		Load the connectors few shot examples from connectors_few_shot.py.
		"""
		return connector_few_shot_examples
	
	def _load_operations_few_shot(self) -> List[Dict[str, Any]]:
		"""
		Load the operations few shot examples from operations_few_shot.py.
		"""
		return operation_few_shot_examples
	
	def _load_tasks_few_shot(self) -> List[Dict[str, Any]]:
		"""
		Load the tasks few shot examples from tasks_few_shot.py.
		"""
		return task_few_shot_examples

	# Classify user's input into categories
	def classify_input(self, input_text: str, context: str) -> List[str]:
		"""
		Use _LLMAdapter to classify the user input into categories.
		"""
		self.logger.debug(f"Classifying input: {input_text}")

		# Load the categories few-shot examples
		all_categories_examples = self._load_categories_few_shot()

		# Get available categories for the user
		available_category_names = self.user._get_connected_categories()
		self.logger.debug(f"Available categories: {available_category_names}")

		# Trigger pre-fetch categories callback with available categories
		self._trigger_callback(FiscusCallbackType.AI_FETCH_CATEGORIES, {"available_categories": available_category_names})

		# Filter categories based on available categories for the user
		available_categories = [
			category for category in all_categories_examples if category["category"] in available_category_names
		]

		# Prepare few-shot examples
		few_shot_examples = [
			{
				"user": f"User Input: {example}",
				"assistant": f"Categories: {json.dumps([category['category']])}"
			}
			for category in available_categories
			for example in category["examples"]
		]

		# Retrieve model-specific function schema from LLMConfig
		function_schema = self.llm_config.get_function_schema(
			action='classify_input',
			llm_type=self.llm_type,
			available_enums=available_category_names
		)

		# Prepare prompt
		prompt = f"User Input: {input_text}\nIdentify the categories relevant to the user's request."

		# Execute using _LLMAdapter
		result = self.llm_adapter.execute(
			action='classify_input',
			prompt=prompt,
			context=context,
			function_schema=function_schema,
			few_shot_examples=few_shot_examples,
			temperature=0.0,
			max_tokens=256,
			response_format=FiscusResponseType.JSON,
			**self.custom_options
		)

		# Trigger post-category selection callback with LLM result
		self._trigger_callback(FiscusCallbackType.AI_CATEGORY_SELECTION, {"input_text": input_text, "selected_categories": result})

		return result if result else []

	# Select connectors based on categories
	def select_connectors(self, input_text: str, categories: List[str], context: str) -> List[str]:
		"""
		Use _LLMAdapter to select appropriate connectors based on categories.
		"""
		self.logger.debug(f"Selecting connectors for categories: {categories}")

		# Retrieve available connectors from SDK user data
		available_connectors = self.user._get_connected_connectors(categories)
		self.logger.debug(f"Available connectors for categories {categories}: {available_connectors}")

		# Trigger pre-fetch connectors callback with available connectors
		self._trigger_callback(FiscusCallbackType.AI_FETCH_CONNECTORS, {"available_connectors": available_connectors})

		# Load all connector few-shot examples and filter based on user's categories
		all_connectors_examples = self._load_connectors_few_shot()

		# Filter few-shot examples to only include relevant connectors for the categories
		few_shot_examples = [
			{
				"user": json.dumps({"categories": example["user"]}),
				"assistant": json.dumps({"connectors": example["assistant"]["connectors"]})
			}
			for example in all_connectors_examples
			if any(cat in categories for cat in example["user"])
		]

		# Retrieve model-specific function schema from LLMConfig with populated enums
		function_schema = self.llm_config.get_function_schema(
			action='select_connectors',
			llm_type=self.llm_type,
			available_enums=available_connectors
		)

		# Prepare prompt
		prompt = (
			f"User Input: {input_text}\n"
			f"Available Connectors: {available_connectors}\n"
			"Based on the user's request and available connectors, select the most relevant connectors."
		)

		# Execute using _LLMAdapter
		result = self.llm_adapter.execute(
			action='select_connectors',
			prompt=prompt,
			context=context,
			function_schema=function_schema,
			few_shot_examples=few_shot_examples,
			temperature=0.0,
			max_tokens=256,
			response_format=FiscusResponseType.JSON,
			**self.custom_options
		)

		# Trigger post-connector selection callback with LLM result
		self._trigger_callback(FiscusCallbackType.AI_CONNECTOR_SELECTION, {"categories": categories, "selected_connectors": result})

		# Check if result is a list and assign directly; otherwise, get 'connectors' key
		selected_connectors = result if isinstance(result, list) else result.get('connectors', [])

		if not selected_connectors:
			self.logger.warning("No connectors identified by LLM.")
			if self.error_callback:
				self.error_callback(Exception("No connectors identified for the input."))
			return []

		self.logger.debug(f"Selected connectors: {selected_connectors}")
		return selected_connectors

	# Select operations for each connector
	def select_operations(self, connectors: List[str], input_text: str, context: str) -> List[str]:
		"""
		Use LLM to select the relevant operations based on the user's selected connectors.
		"""
		self.logger.debug(f"Selecting operations for connectors: {connectors}")

		# Retrieve available operations from SDK user data
		available_operations = self.user._get_connected_operations(connectors)
		self.logger.debug(f"Available operations for connectors {connectors}: {available_operations}")

		# Trigger pre-fetch operations callback with available operations
		self._trigger_callback(FiscusCallbackType.AI_FETCH_OPERATIONS, {"available_operations": available_operations})

		# Create few-shot examples for connectors and operations
		all_operations_examples = self._load_operations_few_shot()
		few_shot_examples = [
			{
				"user": json.dumps({"connector": example["user"]}),
				"assistant": json.dumps({"operations": example["assistant"]["operations"]})
			}
			for example in all_operations_examples
			if any(connector in example["user"] for connector in connectors)
		]

		function_schema = self.llm_config.get_function_schema(
			action='select_operations',
			llm_type=self.llm_type,
			available_enums=available_operations
		)

		# Prepare prompt with the exact available operations per connector
		prompt = (
			f"User Input: {input_text}\n"
			f"Selected Connectors: {connectors}\n"
			f"Available Operations: {json.dumps(available_operations)}\n"
			"Based on the selected connectors, provide the exact operation names for each connector, matching exactly as listed in Available Operations."
		)

		# Execute using _LLMAdapter
		result = self.llm_adapter.execute(
			action='select_operations',
			prompt=prompt,
			context=context,
			function_schema=function_schema,
			few_shot_examples=few_shot_examples,
			temperature=0.0,
			max_tokens=256,
			response_format=FiscusResponseType.JSON,
			**self.custom_options
		)

		# Trigger post-operation selection callback with LLM result
		self._trigger_callback(FiscusCallbackType.AI_OPERATION_SELECTION, {"connectors": connectors, "selected_operations": result})

		# Process the LLM response
		if isinstance(result, list):
			selected_operations = result
		else:
			selected_operations = result.get('operations', [])

		if not selected_operations:
			self.logger.warning("No operations identified by LLM.")
			if self.error_callback:
				self.error_callback(Exception("No operations identified for the selected connectors."))
			return []

		self.logger.debug(f"Selected operations: {selected_operations}")
		return selected_operations

	# Plan tasks to fulfill the user's request
	def plan_tasks(self, input_text: str, connectors_operations: List[Dict[str, Any]], context: str) -> List[Dict[str, Any]]:
		"""
		Use _LLMAdapter to plan out the sequence of tasks (API calls) to perform.
		"""
		self.logger.debug(f"Planning tasks based on connectors and operations.")

		# Trigger pre-task planning callback with available connectors and operations
		self._trigger_callback(FiscusCallbackType.AI_FETCH_OPERATION_DETAILS, {"connectors_operations": connectors_operations})

		# Load all task few-shot examples
		few_shot_examples = self._load_tasks_few_shot()

		# Prepare function schema
		function_schema = self.llm_config.get_function_schema(
			action='plan_tasks',
			llm_type=self.llm_type,
			available_enums=connectors_operations
		)

		# Prepare prompt
		prompt = (
			f"User Input: {input_text}\n"
			f"Connectors and Operations: {json.dumps(connectors_operations)}\n"
			"Plan out the sequence of API calls needed to fulfill the user's request."
		)

		# Execute using _LLMAdapter
		result = self.llm_adapter.execute(
			action='plan_tasks',
			prompt=prompt,
			context=context,
			function_schema=function_schema,
			few_shot_examples=few_shot_examples,
			temperature=0.0,
			max_tokens=1024,
			response_format=FiscusResponseType.JSON,
			**self.custom_options
		)

		# Trigger post-task creation callback with final tasks planned by LLM
		self._trigger_callback(FiscusCallbackType.AI_TASK_CREATION, {"input_text": input_text, "planned_tasks": result})

		# Parse and validate result for 'tasks'
		if isinstance(result, list):
			tasks = result  # Already a list of task dictionaries
		elif isinstance(result, dict) and 'tasks' in result and isinstance(result['tasks'], list):
			tasks = result['tasks']
		else:
			self.logger.error("Failed to parse tasks JSON structure.")
			if self.error_callback:
				self.error_callback(Exception("Failed to parse tasks JSON structure."))
			return []

		# Validate each task's format
		for task in tasks:
			if not isinstance(task, dict) or 'connector' not in task or 'operation' not in task:
				self.logger.error("Each task must be a dictionary with 'connector' and 'operation'.")
				if self.error_callback:
					self.error_callback(Exception("Each task must have 'connector' and 'operation' keys."))
				return []

		return tasks

	def retrieve_memory(
		self,
		input_text: str,
		retrieval_strategy: Optional[FiscusMemoryRetrievalType] = None,
		top_k: int = 5,
		similarity_threshold: float = 0.8,
		**kwargs,
	) -> str:
		"""
		Retrieve context from memory (vector database) relevant to the input.
		"""
		if retrieval_strategy is None:
			retrieval_strategy = self.retrieval_strategy

		self.logger.debug(f"Retrieving memory for input: {input_text} using strategy: {retrieval_strategy}")
		if self.memory_retrieval_logic:
			context = self.memory_retrieval_logic(input_text)
		else:
			# Default logic with various retrieval strategies
			if retrieval_strategy == FiscusMemoryRetrievalType.SEMANTIC_SEARCH:
				context = self.memory.semantic_search(
					query=input_text,
					top_k=top_k,
					embedding_model=self.embedding_model,
					indexing_algorithm=self.indexing_algorithm,
					**kwargs,
				)
			elif retrieval_strategy == FiscusMemoryRetrievalType.KEYWORD_SEARCH:
				context = self.memory.keyword_search(
					query=input_text,
					**kwargs,
				)
			elif retrieval_strategy == FiscusMemoryRetrievalType.HYBRID_SEARCH:
				context = self.memory.hybrid_search(
					query=input_text,
					top_k=top_k,
					similarity_threshold=similarity_threshold,
					embedding_model=self.embedding_model,
					indexing_algorithm=self.indexing_algorithm,
					**kwargs,
				)
			else:
				raise ValueError(f"Unknown retrieval strategy: {retrieval_strategy}")
		self.logger.debug(f"Retrieved context: {context}")
		# Log memory lookup
		self.audit_trail.record('memory_retrieval', {'input': input_text, 'context': context})
		return context

	def store_memory(
		self,
		data: Any,
		storage_strategy: Optional[FiscusMemoryStorageType] = None,
		update_condition: Optional[Callable[[Any], bool]] = None,
		**kwargs,
	) -> None:
		"""
		Store data into memory (vector database).
		"""
		if storage_strategy is None:
			storage_strategy = self.storage_strategy

		self.logger.debug(f"Storing data into memory: {data} using strategy: {storage_strategy}")
		if self.memory_storage_logic:
			self.memory_storage_logic(data)
		else:
			# Default logic with various storage strategies
			if storage_strategy == FiscusMemoryStorageType.APPEND:
				self.memory.store(
					data,
					embedding_model=self.embedding_model,
					indexing_algorithm=self.indexing_algorithm,
					**kwargs,
				)
			elif storage_strategy == FiscusMemoryStorageType.UPDATE:
				if not update_condition:
					raise ValueError("An update_condition function must be provided for Update storage strategy.")
				self.memory.update(
					data,
					update_condition=update_condition,
					embedding_model=self.embedding_model,
					indexing_algorithm=self.indexing_algorithm,
					**kwargs,
				)
			elif storage_strategy == FiscusMemoryStorageType.UPSERT:
				self.memory.upsert(
					data,
					embedding_model=self.embedding_model,
					indexing_algorithm=self.indexing_algorithm,
					**kwargs,
				)
			else:
				raise ValueError(f"Unknown storage strategy: {storage_strategy}")
		# Log memory storage
		self.audit_trail.record('memory_storage', {'data': data})

	def evaluate_conditional_logic(self, conditional_logic: str, context: Dict[str, Any]) -> Any:
		"""
		Use _LLMAdapter to evaluate the conditional logic specified in the task.
		Returns the result of the evaluation.
		"""
		self.logger.debug(f"Evaluating conditional logic: {conditional_logic}")

		few_shot_examples = self.few_shot_examples.get('conditional_evaluation', [])

		# Prepare function schema
		function_schema = {
			"name": "evaluate_conditional_logic",
			"description": "Evaluate the conditional logic based on the provided context.",
			"parameters": {
				"type": "object",
				"properties": {
					"result": {
						"type": ["boolean", "number", "string", "object", "array"],
						"description": "The result of evaluating the conditional logic."
					}
				},
				"required": ["result"]
			}
		}

		# Prepare prompt
		prompt = (
			f"Conditional Logic: {conditional_logic}\n"
			f"Context: {json.dumps(context)}\n"
			"Evaluate the conditional logic and provide the result."
		)

		# Execute using _LLMAdapter
		result = self.llm_adapter.execute(
			action='evaluate_conditional_logic',
			prompt=prompt,
			context=None,
			function_schema=function_schema,
			few_shot_examples=few_shot_examples,
			temperature=0.0,
			max_tokens=256,
			response_format=FiscusResponseType.JSON,
			**self.custom_options
		)

		if not result or 'result' not in result:
			self.logger.warning("No result from LLM for conditional logic.")
			if self.error_callback:
				self.error_callback(Exception("No result from LLM for conditional logic."))
			return None

		return result['result']

	def run(
		self,
		input_text: str,
		callbacks: Optional[Dict[str, FiscusCallback]] = None,
		connection_type: Optional[FiscusConnectionType] = None,
		response_format: Optional[FiscusResponseType] = FiscusResponseType.JSON,
		execution_mode: FiscusExecutionType = FiscusExecutionType.SEQUENTIAL,
	) -> FiscusResponse:
		"""
		The main method to process input and execute tasks synchronously.
		"""
		self.logger.debug(f"Running AIOrchestrator with input: {input_text}")
		self.logger.debug(f"connection_type={connection_type}, response_format={response_format}")

		tasks = self.process_input(input_text)
		self.logger.debug(f"Processed tasks: {_mask_sensitive_info(tasks)}")

		if not tasks:
			self.logger.warning("No tasks could be planned based on the input.")
			return FiscusResponse(success=False, error=FiscusError(
				code=FiscusErrorCode.INVALID_REQUEST,
				message="No tasks could be planned based on the input."
			))

		# Execute tasks and receive response
		response = self.execute_tasks(
			tasks=tasks,
			callbacks=callbacks,
			connection_type=connection_type,
			response_format=response_format,
			execution_mode=execution_mode,
		)

		# Ensure we have a FiscusResponse instance
		if not isinstance(response, FiscusResponse):
			self.logger.warning("Received response is not a FiscusResponse instance; wrapping it now.")
			response = FiscusResponse(success=True, result=response)

		# Handle failure case
		if not response.success:
			self.logger.error(f"Task execution failed with error: {response.error}")
			return response  # Return the error-laden FiscusResponse as-is

		# Post-process response if necessary
		if self.postprocess_function:
			self.logger.debug("Applying postprocess_function to response.")
			response = self.postprocess_function(response)

		# Extract only the data contents
		if isinstance(response.data, list):
			response_result = [
				res.data if res.success else {'error': res.error.to_dict() if res.error else 'Unknown error'}
				for res in response.data if isinstance(res, FiscusResponse)
			]
		else:
			response_result = response.data

		# Add logging to inspect response_result
		self.logger.debug(f"Extracted response_result: {_mask_sensitive_info(response_result)}")

		# Create final response based on connection type and format
		final_response = FiscusResponse(success=True, result=response_result, message_id=response.message_id)

		if connection_type == FiscusConnectionType.WEBSOCKET and response_format == FiscusResponseType.TEXT:
			self.logger.debug("Generating final response as TEXT for WebSocket connection.")
			final_response_text = self.generate_final_response(input_text, response_result, response_format)
			return FiscusResponse(success=True, result=final_response_text, message_id=response.message_id)

		elif connection_type == FiscusConnectionType.REST and response_format == FiscusResponseType.JSON:
			self.logger.debug("Returning JSON response for REST connection.")
			return final_response

		elif connection_type == FiscusConnectionType.WEBSOCKET and response_format == FiscusResponseType.JSON:
			self.logger.debug("Returning JSON response for WebSocket connection.")
			return final_response

		elif connection_type == FiscusConnectionType.REST and response_format == FiscusResponseType.TEXT:
			self.logger.debug("Generating final response as TEXT for REST connection.")
			final_response_text = self.generate_final_response(input_text, response_result, response_format)
			return FiscusResponse(success=True, result=final_response_text, message_id=response.message_id)

		# Default case: return JSON format
		self.logger.debug("Defaulting to JSON response format.")
		return final_response

	async def run_async(
		self,
		input_text: str,
		callbacks: Optional[Dict[str, FiscusCallback]] = None,
		connection_type: Optional[FiscusConnectionType] = None,
		response_format: Optional[FiscusResponseType] = FiscusResponseType.JSON,
		execution_mode: FiscusExecutionType = FiscusExecutionType.SEQUENTIAL,
	) -> FiscusResponse:
		"""
		The main method to process input and execute tasks asynchronously.
		"""
		self.logger.debug(f"Running AIOrchestrator asynchronously with input: {input_text}")
		self.logger.debug(f"connection_type={connection_type}, response_format={response_format}")

		tasks = self.process_input(input_text)
		self.logger.debug(f"Processed tasks: {_mask_sensitive_info(tasks)}")

		if not tasks:
			self.logger.warning("No tasks could be planned based on the input.")
			return FiscusResponse(success=False, error=FiscusError(
				code=FiscusErrorCode.INVALID_REQUEST,
				message="No tasks could be planned based on the input."
			))

		# Execute tasks and receive response
		response = await self.execute_tasks_async(
			tasks=tasks,
			callbacks=callbacks,
			connection_type=connection_type,
			response_format=response_format,
			execution_mode=execution_mode,
		)

		# Ensure we have a FiscusResponse instance
		if not isinstance(response, FiscusResponse):
			self.logger.warning("Received response is not a FiscusResponse instance; wrapping it now.")
			response = FiscusResponse(success=True, result=response)

		# Handle failure case
		if not response.success:
			self.logger.error(f"Task execution failed with error: {response.error}")
			return response  # Return the error-laden FiscusResponse as-is

		# Post-process response if necessary
		if self.postprocess_function:
			self.logger.debug("Applying postprocess_function to response.")
			response = self.postprocess_function(response)

		# Extract only the data contents
		if isinstance(response.data, list):
			response_result = [
				res.data if res.success else {'error': res.error.to_dict() if res.error else 'Unknown error'}
				for res in response.data if isinstance(res, FiscusResponse)
			]
		else:
			response_result = response.data

		# Add logging to inspect response_result
		self.logger.debug(f"Extracted response_result: {_mask_sensitive_info(response_result)}")

		# Create final response based on connection type and format
		final_response = FiscusResponse(success=True, result=response_result, message_id=response.message_id)

		if connection_type == FiscusConnectionType.WEBSOCKET and response_format == FiscusResponseType.TEXT:
			self.logger.debug("Generating final response as TEXT for WebSocket connection.")
			final_response_text = await self.generate_final_response_async(input_text, response_result, response_format)
			return FiscusResponse(success=True, result=final_response_text, message_id=response.message_id)

		elif connection_type == FiscusConnectionType.REST and response_format == FiscusResponseType.JSON:
			self.logger.debug("Returning JSON response for REST connection.")
			return final_response

		elif connection_type == FiscusConnectionType.WEBSOCKET and response_format == FiscusResponseType.JSON:
			self.logger.debug("Returning JSON response for WebSocket connection.")
			return final_response

		elif connection_type == FiscusConnectionType.REST and response_format == FiscusResponseType.TEXT:
			self.logger.debug("Generating final response as TEXT for REST connection.")
			final_response_text = await self.generate_final_response_async(input_text, response_result, response_format)
			return FiscusResponse(success=True, result=final_response_text, message_id=response.message_id)

		# Default case: return JSON format
		self.logger.debug("Defaulting to JSON response format.")
		return final_response

	def generate_final_response(self, input_text: str, api_responses: Any, response_format: FiscusResponseType) -> str:
		"""
		Use _LLMAdapter to generate the final response to the user, incorporating the results from API calls.
		"""
		self.logger.debug("Generating final response using LLM.")

		few_shot_examples = self.few_shot_examples.get('final_response', [])

		# Prepare prompt
		api_response_content = api_responses if response_format == FiscusResponseType.JSON else str(api_responses)
		prompt = (
			f"User Input: {input_text}\n"
			f"API Responses: {api_response_content}\n"
			"Based on the user's request and the API responses, generate a final response to the user."
		)

		# Execute using _LLMAdapter
		result = self.llm_adapter.execute(
			action='generate_final_response',
			prompt=prompt,
			context=None,
			function_schema=None,
			few_shot_examples=few_shot_examples,
			temperature=0.7,
			max_tokens=512,
			response_format=response_format.value.lower(),
			**self.custom_options
		)

		if result is None:
			self.logger.warning("Failed to generate final response using LLM.")
			if self.error_callback:
				self.error_callback(Exception("Failed to generate final response using LLM."))
			return ""

		return result

	async def generate_final_response_async(self, input_text: str, api_responses: Any, response_format: FiscusResponseType) -> str:
		"""
		Asynchronously use _LLMAdapter to generate the final response to the user.
		"""
		# Since _LLMAdapter doesn't have async methods in this design, we'll use the synchronous method
		return self.generate_final_response(input_text, api_responses, response_format)

	def execute_tasks(
		self,
		tasks: List[Dict[str, Any]],
		callbacks: Optional[Dict[str, FiscusCallback]] = None,
		connection_type: Optional[FiscusConnectionType] = None,
		response_format: Optional[FiscusResponseType] = None,
		execution_mode: FiscusExecutionType = FiscusExecutionType.SEQUENTIAL,
	) -> FiscusResponse:
		"""
		Execute the tasks, possibly sequentially or in parallel.
		"""
		responses = []
		self.logger.debug(f"Executing tasks with execution_mode={execution_mode}")

		# Context to pass between tasks
		context = {}

		if execution_mode == FiscusExecutionType.SEQUENTIAL:
			for task in tasks:
				self.logger.debug(f"Executing task: {_mask_sensitive_info(task)}")

				# Pre-execution hook
				if 'pre_execution_hook' in task and callable(task['pre_execution_hook']):
					self.logger.debug("Executing pre-execution hook for task.")
					task = task['pre_execution_hook'](task)

				# Handle conditional logic
				if task.get('conditional_logic') not in [None, '', 'none', 'null', False, 0]:
					condition_result = self.evaluate_conditional_logic(task['conditional_logic'], context)
					if not condition_result:
						self.logger.debug(f"Skipping task due to conditional logic result: {condition_result}")
						continue  # Skip this task
					else:
						self.logger.debug(f"Conditional logic evaluated to: {condition_result}")

				response = self.orchestrator._execute_operation(
					connector_name=task['connector'],
					operation=task['operation'],
					params=task.get('params', {}),
					callbacks=task.get('callbacks', callbacks),
					custom_options=task.get('custom_options', self.custom_options),
					connection_type=connection_type,
					response_format=response_format,
					user=self.user,
				)

				# Add logging here to inspect the response
				self.logger.debug(f"Received response: {response}")
				self.logger.debug(f"Response success: {response.success}")
				self.logger.debug(f"Response data: {_mask_sensitive_info(response.data)}")

				responses.append(response)

				# Update context with the response
				if response.success and response.data:
					if isinstance(response.data, dict):
						context.update(response.data)
					else:
						context['last_result'] = response.data

				# Post-execution hook
				if 'post_execution_hook' in task and callable(task['post_execution_hook']):
					self.logger.debug("Executing post-execution hook for task.")
					response = task['post_execution_hook'](response)

				# Error handling and retry logic
				if not response.success:
					# Implement custom error handling, retries, fallbacks
					retry_attempts = task.get('retry_attempts', 0)
					max_retries = task.get('max_retries', self.client.retries)
					while not response.success and retry_attempts < max_retries:
						retry_attempts += 1
						sleep_time = self.client.backoff_factor * (2 ** retry_attempts)
						self.logger.warning(f"Retrying task '{task['operation']}' after {sleep_time} seconds (Attempt {retry_attempts}).")
						time.sleep(sleep_time)
						response = self.orchestrator._execute_operation(
							connector_name=task['connector'],
							operation=task['operation'],
							params=task.get('params', {}),
							callbacks=task.get('callbacks', callbacks),
							custom_options=task.get('custom_options', self.custom_options),
							connection_type=connection_type,
							response_format=response_format,
							user=self.user,
						)
						responses.append(response)
					if not response.success:
						# Fallback mechanism
						fallback_task = task.get('fallback_task')
						if fallback_task:
							self.logger.warning(f"Executing fallback task for '{task['operation']}'.")
							response = self.orchestrator._execute_operation(
								connector_name=fallback_task['connector'],
								operation=fallback_task['operation'],
								params=fallback_task.get('params', {}),
								callbacks=fallback_task.get('callbacks', callbacks),
								custom_options=fallback_task.get('custom_options', self.custom_options),
								connection_type=connection_type,
								response_format=response_format,
								user=self.user,
							)
							responses.append(response)
						else:
							# Invoke error callback if provided
							if self.error_callback:
								self.logger.error(f"Task '{task['operation']}' failed after retries. Invoking error callback.")
								self.error_callback(Exception(f"Task '{task['operation']}' failed after retries."))
							else:
								self.logger.fatal(f"Task '{task['operation']}' failed after retries with no error callback.")
							break  # Stop execution if no fallback is provided
					else:
						self.logger.info(f"Task '{task['operation']}' succeeded after retries.")

				else:
					# Store memory if necessary
					if self.memory and ('store_memory' not in task or task['store_memory']):
						self.logger.debug("Storing response data into memory.")
						self.store_memory(response.data)

		elif execution_mode == FiscusExecutionType.PARALLEL:
			# Handle parallel execution
			self.logger.debug("Executing tasks in parallel.")
			loop = asyncio.new_event_loop()
			asyncio.set_event_loop(loop)
			tasks_coroutines = [
				self._execute_task_async(
					task=task,
					callbacks=callbacks,
					connection_type=connection_type,
					response_format=response_format,
					context=context,
				)
				for task in tasks
			]
			responses = loop.run_until_complete(asyncio.gather(*tasks_coroutines))
			loop.close()
		else:
			self.logger.error("Invalid execution_mode specified.")
			raise ValueError("Invalid execution_mode. Must be FiscusExecutionType.SEQUENTIAL or FiscusExecutionType.PARALLEL.")

		self.logger.debug(f"All responses collected: {responses}")
		return FiscusResponse(success=True, result=responses)

	async def _execute_task_async(
		self,
		task: Dict[str, Any],
		callbacks: Optional[Dict[str, FiscusCallback]] = None,
		connection_type: Optional[FiscusConnectionType] = None,
		response_format: Optional[FiscusResponseType] = None,
		context: Dict[str, Any] = None,
	) -> FiscusResponse:
		"""
		Helper function to execute a single task asynchronously.
		"""
		context = context or {}
		self.logger.debug(f"Starting async execution of task: {_mask_sensitive_info(task)}")

		# Pre-execution hook
		if 'pre_execution_hook' in task and callable(task['pre_execution_hook']):
			self.logger.debug("Executing pre-execution hook for task.")
			task = task['pre_execution_hook'](task)

		# Handle conditional logic
		if task.get('conditional_logic') not in [None, '', 'none', 'null', False, 0]:
			condition_result = self.evaluate_conditional_logic(task['conditional_logic'], context)
			if not condition_result:
				self.logger.debug(f"Skipping task due to conditional logic result: {condition_result}")
				return FiscusResponse(success=True, result="Task skipped due to conditional logic.")
			else:
				self.logger.debug(f"Conditional logic evaluated to: {condition_result}")

		response = await self.orchestrator._execute_operation_async(
			connector_name=task['connector'],
			operation=task['operation'],
			params=task.get('params', {}),
			callbacks=task.get('callbacks', callbacks),
			custom_options=task.get('custom_options', self.custom_options),
			connection_type=connection_type,
			response_format=response_format,
			user=self.user,
		)

		# Add logging here to inspect the response
		self.logger.debug(f"Received response: {response}")
		self.logger.debug(f"Response success: {response.success}")
		self.logger.debug(f"Response data: {_mask_sensitive_info(response.data)}")

		# Update context with the response
		if response.success and response.data:
			if isinstance(response.data, dict):
				context.update(response.data)
			else:
				context['last_result'] = response.data

		# Post-execution hook
		if 'post_execution_hook' in task and callable(task['post_execution_hook']):
			self.logger.debug("Executing post-execution hook for task.")
			response = task['post_execution_hook'](response)

		# Error handling and retry logic
		if not response.success:
			# Implement custom error handling, retries, fallbacks
			retry_attempts = task.get('retry_attempts', 0)
			max_retries = task.get('max_retries', self.client.retries)
			while not response.success and retry_attempts < max_retries:
				retry_attempts += 1
				sleep_time = self.client.backoff_factor * (2 ** retry_attempts)
				self.logger.warning(f"Retrying task '{task['operation']}' after {sleep_time} seconds (Attempt {retry_attempts}).")
				await asyncio.sleep(sleep_time)
				response = await self.orchestrator._execute_operation_async(
					connector_name=task['connector'],
					operation=task['operation'],
					params=task.get('params', {}),
					callbacks=task.get('callbacks', callbacks),
					custom_options=task.get('custom_options', self.custom_options),
					connection_type=connection_type,
					response_format=response_format,
					user=self.user,
				)
			if not response.success:
				# Fallback mechanism
				fallback_task = task.get('fallback_task')
				if fallback_task:
					self.logger.warning(f"Executing fallback task for '{task['operation']}'.")
					response = await self.orchestrator._execute_operation_async(
						connector_name=fallback_task['connector'],
						operation=fallback_task['operation'],
						params=fallback_task.get('params', {}),
						callbacks=fallback_task.get('callbacks', callbacks),
						custom_options=fallback_task.get('custom_options', self.custom_options),
						connection_type=connection_type,
						response_format=response_format,
						user=self.user,
					)
				else:
					# Invoke error callback if provided
					if self.error_callback:
						self.logger.error(f"Task '{task['operation']}' failed after retries. Invoking error callback.")
						self.error_callback(Exception(f"Task '{task['operation']}' failed after retries."))
					else:
						self.logger.fatal(f"Task '{task['operation']}' failed after retries with no error callback.")
		else:
			# Store memory if necessary
			if self.memory and ('store_memory' not in task or task['store_memory']):
				self.logger.debug("Storing response data into memory.")
				self.store_memory(response.data)

		return response

	async def execute_tasks_async(
		self,
		tasks: List[Dict[str, Any]],
		callbacks: Optional[Dict[str, FiscusCallback]] = None,
		connection_type: Optional[FiscusConnectionType] = None,
		response_format: Optional[FiscusResponseType] = None,
		execution_mode: FiscusExecutionType = FiscusExecutionType.SEQUENTIAL,
	) -> FiscusResponse:
		"""
		Execute the tasks asynchronously.
		"""
		responses = []
		self.logger.debug(f"Executing tasks asynchronously with execution_mode={execution_mode}")

		# Context to pass between tasks
		context = {}

		if execution_mode == FiscusExecutionType.SEQUENTIAL:
			for task in tasks:
				self.logger.debug(f"Executing task asynchronously: {_mask_sensitive_info(task)}")

				response = await self._execute_task_async(
					task=task,
					callbacks=callbacks,
					connection_type=connection_type,
					response_format=response_format,
					context=context,
				)
				responses.append(response)

				if not response.success:
					break  # Stop execution if a task fails and no fallback is provided
		elif execution_mode == FiscusExecutionType.PARALLEL:
			self.logger.debug("Executing tasks in parallel asynchronously.")
			tasks_coroutines = [
				self._execute_task_async(
					task=task,
					callbacks=callbacks,
					connection_type=connection_type,
					response_format=response_format,
					context=context,
				)
				for task in tasks
			]
			responses = await asyncio.gather(*tasks_coroutines)
		else:
			self.logger.error("Invalid execution_mode specified.")
			raise ValueError("Invalid execution_mode. Must be FiscusExecutionType.SEQUENTIAL or FiscusExecutionType.PARALLEL.")

		self.logger.debug(f"All responses collected asynchronously: {responses}")
		return FiscusResponse(success=True, result=responses)
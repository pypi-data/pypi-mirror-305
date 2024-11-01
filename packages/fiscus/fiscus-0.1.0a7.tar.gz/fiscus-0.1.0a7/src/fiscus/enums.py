# fiscus_sdk/enums.py

import logging
import json
from enum import Enum

# Define a custom TRACE level numeric value
TRACE_LEVEL_NUM = 5
logging.addLevelName(TRACE_LEVEL_NUM, "TRACE")

# Add trace logging method to Logger class
def trace(self, message, *args, **kwargs):
    if self.isEnabledFor(TRACE_LEVEL_NUM):
        self._log(TRACE_LEVEL_NUM, message, args, **kwargs)

logging.Logger.trace = trace

# Custom enum class to expose logs through the SDK
class FiscusLogLevel(Enum):
    TRACE = 'Trace'
    DEBUG = 'Debug'
    INFO = 'Info'
    WARNING = 'Warning'
    ERROR = 'Error'
    FATAL = 'Fatal'

    # We only want to pass across helpful logs, but trace and debugging give too much info
    @classmethod
    def public_levels(cls):
        return {cls.INFO, cls.WARNING, cls.ERROR, cls.FATAL}

    def to_logging_level(self):
        level_map = {
            FiscusLogLevel.TRACE: TRACE_LEVEL_NUM,
            FiscusLogLevel.DEBUG: logging.DEBUG,
            FiscusLogLevel.INFO: logging.INFO,
            FiscusLogLevel.WARNING: logging.WARNING,
            FiscusLogLevel.ERROR: logging.ERROR,
            FiscusLogLevel.FATAL: logging.CRITICAL,
        }
        return level_map[self]
    
# Custom class to allow user to choose connection type
class FiscusConnectionType(Enum):
    REST = 'rest'
    WEBSOCKET = 'websocket'
    
# Custom class to allow user to choose who they want a response formatted
class FiscusRestType(Enum):
    GET = 'get'
    POST = 'post'
    PUT = 'put'
    DELETE = 'delete'

# Custom class to allow user to choose who they want a response formatted
class FiscusResponseType(Enum):
    TEXT = 'text'
    JSON = 'json'

# Custom class to handle the initialization logic
class FiscusInitType(Enum):
    LAZY = 'lazy'
    EAGER = 'eager'
    
# Custom class to handle the execution logic
class FiscusExecutionType(Enum):
    PARALLEL = 'parallel'
    SEQUENTIAL = 'sequential'
    
# Custom class to handle the vector memory retrieval logic
class FiscusMemoryRetrievalType(Enum):
    SEMANTIC_SEARCH = 'semantic_search'
    KEYWORD_SEARCH = 'keyword_search'
    HYBRID_SEARCH = 'hybrid_search'
    
# Custom class to handle the vector memory retrieval logic
class FiscusMemoryStorageType(Enum):
    APPEND = 'append'
    UPDATE = 'update'
    UPSERT = 'upsert'
    
# Custom class to handle the WebSocket message type logic
class FiscusActionType(Enum):
    ACTION = 'action'
    USER = 'user'

    def __str__(self):
        return self.value

    def to_json(self):
        return self.value
    
# Custom class to handle the LLM type use for execute_ai logic
class FiscusLLMType(Enum):
    OPENAI = 'openai'
    ANTHROPIC = 'anthropic'
    GEMINI = 'gemini'
    LLAMA = 'llama'
    COHERE = 'cohere'

# Custom class to handle the LLM prompt to use for execute_ai logic 
class FiscusLLMTaskType(Enum):
    CATEGORY_CLASSIFICATION = "classify_input"
    CONNECTOR_SELECTION = "select_connectors"
    TASK_PLANNING = "plan_tasks"
    LOGIC_EVALUATION = "evaluate_conditional_logic"

# Custom class to handle response encoding
class FiscusActionTypeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, FiscusActionType):
            return obj.value  # Convert the enum to its value (string) for serialization
        return super().default(obj)
    
# Custom class to handle the type of callback
class FiscusCallbackType(Enum):
    # SDK callback types
    ON_SUCCESS = "on_success"
    ON_ERROR = "on_error"
    ON_AUTH = "on_auth"
    ON_STREAM = "on_stream"
    ON_LOG = "on_log"
    ON_RESPONSE = "on_response"
    
    # AI-driven process callback types
    AI_FETCH_CATEGORIES = "on_fetch_categories"
    AI_CATEGORY_SELECTION = "on_category_selection"
    AI_FETCH_CONNECTORS = "on_fetch_connectors"
    AI_CONNECTOR_SELECTION = "on_connector_selection"
    AI_FETCH_OPERATIONS = "on_fetch_operations"
    AI_OPERATION_SELECTION = "on_operation_selection"
    AI_FETCH_OPERATION_DETAILS = "on_fetch_operation_details"
    AI_TASK_CREATION = "on_task_creation"
    AI_COMPLETE = "on_ai_complete"


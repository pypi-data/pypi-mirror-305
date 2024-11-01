# fiscus/__init__.py

"""
Fiscus SDK - API Gateway for the AI World
"""

__version__ = '0.1.0-alpha.5'
__version_info__ = (0, 1, 0, 'alpha', 5)
__author__ = "Fiscus Flows, Inc."
__license__ = "Proprietary"
__description__ = "Fiscus is a powerful platform designed to be the API Gateway for the AI World. It enables developers to integrate AI agents and language models with any API or service, without the need for manual mapping or code adjustments"

# Explicit relative imports for better internal structure and control
from fiscus.client import FiscusClient
from fiscus.user import FiscusUser
from fiscus.connector import FiscusConnector
from fiscus.response import FiscusResponse
from fiscus.audit import FiscusAuditTrail
from fiscus.exceptions import (
    FiscusError,
    FiscusAuthenticationError,
    FiscusAuthorizationError,
    FiscusValidationError,
)
from fiscus.callbacks import (
	FiscusCallback,
	FiscusOnSuccess,
	FiscusOnError,
	FiscusOnAuth,
	FiscusOnLog,
	FiscusOnStream,
	FiscusOnResponse,
	FiscusAIFetchCategories,
	FiscusAICategorySelection,
	FiscusAIFetchConnectors,
	FiscusAIConnectorSelection,
	FiscusAIFetchOperations,
	FiscusAIOperationSelection,
	FiscusAIFetchOperationDetails,
	FiscusAITaskCreation,
	FiscusAIComplete
)
from fiscus.enums import (
	FiscusResponseType,
	FiscusConnectionType,
	FiscusExecutionType,
	FiscusInitType,
	FiscusLogLevel,
	FiscusLLMType,
	FiscusMemoryRetrievalType,
	FiscusMemoryStorageType,
	FiscusCallbackType
)

# Only expose essential classes and functions in __all__
__all__ = [
    'FiscusClient',
    'FiscusUser',
    'FiscusConnector',
    'FiscusResponse',
    'FiscusError',
    'FiscusAuthenticationError',
    'FiscusAuthorizationError',
    'FiscusValidationError',
    'FiscusCallback',
    'FiscusOnSuccess',
	'FiscusOnError',
	'FiscusOnAuth',
	'FiscusOnLog',
	'FiscusOnStream',
	'FiscusOnResponse',
	'FiscusAIFetchCategories',
	'FiscusAICategorySelection',
	'FiscusAIFetchConnectors',
	'FiscusAIConnectorSelection',
	'FiscusAIFetchOperations',
	'FiscusAIOperationSelection',
	'FiscusAIFetchOperationDetails',
	'FiscusAITaskCreation',
	'FiscusAIComplete',
    'FiscusAuditTrail',
    'FiscusResponseType',
    'FiscusConnectionType',
	'FiscusExecutionType',
    'FiscusInitType',
    'FiscusLogLevel',
	'FiscusLLMType',
	'FiscusMemoryRetrievalType',
	'FiscusMemoryStorageType',
	'FiscusCallbackType'
]
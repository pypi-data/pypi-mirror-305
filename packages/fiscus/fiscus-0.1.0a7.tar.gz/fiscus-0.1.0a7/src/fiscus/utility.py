# fiscus_sdk/utils.py

from typing import Any

def validate_params(params: dict) -> bool:
    """
    Validate parameters before execution.

    :param params: Parameters to validate.
    :return: True if valid, False otherwise.
    """
    
    # Accept empty params as valid
    # if params is None:
    #     return True
    if not isinstance(params, dict):
        return False
    if not params:
        return False
    # Additional checks can be added here
    # For instance, checking required keys, value types, etc.
    return True

# Helper function to mask sensitive information
def _mask_sensitive_info(data: Any) -> Any:
    """
    Helper function to mask sensitive information in logs.
    """
    if isinstance(data, dict):
        data = data.copy()
        for key in data:
            if any(sensitive_word in key.lower() for sensitive_word in ['token', 'secret', 'password', 'api_key']):
                data[key] = '****'
    return data

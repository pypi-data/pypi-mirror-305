from enum import Enum

class StatusCode(Enum):
    """
    Defines status codes for logging events.
    """
    SUCCESS = 0
    ERROR_GENERIC = 100  # General error
    ERROR_DATABASE = 101 
    ERROR_NETWORK = 102
    ERROR_FILE_IO = 103
    ERROR_VALIDATION = 104 
    NO_DATA_FOUND = 200
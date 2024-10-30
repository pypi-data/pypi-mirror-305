import logging
import datetime
from .status_codes import StatusCode
from .database import log_to_database  # Import the database function

def log_event(country: str, task_name: str, status_code: StatusCode, 
              log_message: str, level=logging.INFO, additional_data=None):
    """
    Logs an event with the provided information.

    Args:
        country (str): The country code (e.g., "US", "GB").
        task_name (str): The name of the task being logged.
        status_code (StatusCode): The status code of the event.
        log_message (str): The message describing the event.
        level (int, optional): The logging level (e.g., logging.INFO, logging.ERROR). 
                               Defaults to logging.INFO.
        additional_data (dict, optional): Any extra data to include in the log. 
                                          Defaults to None.
    """

     # Type checking
    if not isinstance(country, str):
        raise TypeError("country must be a string")
    if not isinstance(task_name, str):
        raise TypeError("task_name must be a string")
    if not isinstance(status_code, StatusCode):
        # Check if the status_code is a valid enum value
        valid_status_codes = [e.value for e in StatusCode]
        if status_code.value not in valid_status_codes:
            raise ValueError(f"Invalid status_code. Must be one of: {valid_status_codes}")
    if not isinstance(log_message, str):
        raise TypeError("log_message must be a string")
    if not isinstance(level, int):
        raise TypeError("level must be an integer (logging level)")
    if additional_data is not None and not isinstance(additional_data, dict):
        raise TypeError("additional_data must be a dictionary or None")
    

    # Format the log message
    log_message = f"{log_message} [Code: {status_code.name} ({status_code.value})]"
    if additional_data:
        log_message += f" - Data: {additional_data}"

    # Log the event using Python's logging module
    logging.log(level, log_message)

    # Log to the database
    try:
        log_to_database(
            datetime.datetime.now(), 
            country, 
            task_name, 
            status_code.value, 
            log_message, 
            additional_data
        )
    except Exception as e:
        logging.error(f"Failed to log to database: {e}")
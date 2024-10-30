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
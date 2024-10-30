# MapAction Logging Module

This module provides a structured and flexible way to log events in your MapAction applications. It includes a Streamlit dashboard for visualizing and filtering log data.

## Features

*   **Status Codes:** Uses an `Enum` to define clear status codes.
*   **Detailed Logging:** Captures timestamps, country, task name, status code, log message, and additional data.
*   **Database Storage:** Logs events to a SQLite database.
*   **Integration with Python's `logging`:** Uses the built-in `logging` module.
*   **Streamlit Dashboard:** Visualize and filter log data.

## Installation

```bash
pip install mapaction-logging-module
```

## Usage

**1. Logging events:**

```python
from mapaction_logging import log_event, StatusCode

log_event(
    country="BLZ",
    task_name="my_task",
    status_code=StatusCode.SUCCESS,
    log_message="Task completed successfully!",
    additional_data={"details": "Some extra information"}
)
```

**2. Running the dashboard:**

```bash
streamlit run mapaction_logging/dashboard/mapaction_logging_app.py
```

## Contributing

Contributions are welcome! See the GitHub repository for more details.

## License

MIT License
import sqlite3

def create_logs_table():
    """
    Creates the 'logs' table in the database if it doesn't exist.
    """
    try:
        conn = sqlite3.connect('mapaction_logging.db')
        cursor = conn.cursor()

        # Create the logs table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TIMESTAMP,
                country VARCHAR(255),
                task_name VARCHAR(255),
                status_code INTEGER,
                log_message TEXT,
                additional_data TEXT
            )
        ''')
        conn.commit()
    except Exception as e:
        # Handle any exceptions that might occur during table creation
        print(f"Error creating logs table: {e}") 
    finally:
        if conn:
            conn.close()

def log_to_database(timestamp, country, task_name, status_code, log_message, additional_data):
    """
    Inserts a log entry into the database.
    """
    try:
        conn = sqlite3.connect('mapaction_logging.db')
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO logs (timestamp, country, task_name, status_code, log_message, additional_data)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (timestamp, country, task_name, status_code, log_message, str(additional_data)))

        conn.commit()
    except Exception as e:
        # Handle database errors (e.g., log the error, raise an exception)
        raise e  # Or handle the error differently
    finally:
        if conn:
            conn.close()

# Create the table when the module is imported
create_logs_table()
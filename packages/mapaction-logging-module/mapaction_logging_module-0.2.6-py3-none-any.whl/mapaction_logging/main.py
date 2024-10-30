import streamlit as st
from mapaction_logging.dashboard import mapaction_logging_app  # Import the app

def main():
    """
    Runs the MapAction logging dashboard.
    """
    mapaction_logging_app.main()  # Call the main function of the app

if __name__ == "__main__":
    main()
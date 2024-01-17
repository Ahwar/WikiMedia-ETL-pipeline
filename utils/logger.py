import logging
from datetime import datetime
import os

# Configure logging
def get_logger():
    # Create log directory if not exists
    if not os.path.exists("logs"):
        os.makedirs("logs")

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(f"logs/wikimedia-log-{datetime.now()}.log"),
            logging.StreamHandler(),
        ],
    )

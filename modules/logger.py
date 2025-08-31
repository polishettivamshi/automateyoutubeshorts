import logging
import os
from datetime import date

LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Create logger
logger = logging.getLogger("YouTubeShortsBot")
logger.setLevel(logging.INFO)

# Create file handler with date-based filename
file_handler = logging.FileHandler(f"{LOG_DIR}/bot_{date.today()}.log", mode="a")
file_handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add only the file handler (no console output)
logger.addHandler(file_handler)

# Usage in other modules:
# from modules.logger import logger
# logger.info("Message here")
# logger.warning("Warning here")
# logger.error("Error here")

import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler

# Create only logs directory
LOG_DIR = os.path.join(os.getcwd(), "logs")

os.makedirs(LOG_DIR, exist_ok=True)

# Single log file
LOG_FILE = "app.log"

LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

handler = RotatingFileHandler(
    LOG_FILE_PATH,
    maxBytes=5 * 1024 * 1024,
    backupCount=3
)

logging.basicConfig(
    handlers=[handler],
    level=logging.INFO,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)
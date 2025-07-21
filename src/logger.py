import logging
import os
from datetime import datetime

# Create logs directory if it doesn't exist
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Create a log file with current timestamp
LOG_FILE = os.path.join(LOG_DIR, f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log")

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Get a logger instance
logger = logging.getLogger(__name__)

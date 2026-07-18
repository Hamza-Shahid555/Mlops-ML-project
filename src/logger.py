import logging
import os

from datetime import datetime

log_file_name = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", log_file_name)
os.makedirs(logs_path, exist_ok=True)

log_file_path = os.path.join(logs_path, log_file_name)

logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

if name__ == "__main__":
    logging.info("Logging setup complete.")
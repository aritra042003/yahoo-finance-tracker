import os
import logging

def setup_logger(log_file="logs/project.log"):
    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger(__name__)

def ensure_dir(path: str):
    """Ensure directory exists before saving a file."""
    if path and not os.path.exists(path):   # check path is not empty
        os.makedirs(path, exist_ok=True)

import logging
from logging.handlers import RotatingFileHandler
import os
from pathlib import Path

def setup_logging():
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            RotatingFileHandler(
                log_dir / "rpg_backend.log",
                maxBytes=1024 * 1024 * 5,  # 5MB
                backupCount=5
            ),
            logging.StreamHandler()
        ]
    )
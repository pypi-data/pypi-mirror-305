import logging
import os
from .config_loader import ConfigLoader

class LoggerManager:
    def __init__(self, DefaultPath):
        self.config = ConfigLoader().get_additional_config().get("logging", {})
        self.log_level = self.config.get("log_level", "FATAL") 
        self.log_path = self.config.get("log_path", DefaultPath)
        self.log_file = self.config.get("log_file", "Docker_Manager.log")

    def configure_logging(self):
        os.makedirs(self.log_path, exist_ok=True)
        
        log_file_path = os.path.join(self.log_path, self.log_file)
        
        handler = logging.FileHandler(log_file_path, mode='a')
        handler.setLevel(self.log_level)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        logger = logging.getLogger()
        logger.setLevel(self.log_level)
        
        logger.handlers = [h for h in logger.handlers if not isinstance(h, logging.StreamHandler)]
        
        logger.addHandler(handler)
        
        logging.info("Logging configured with FileHandler.")
        
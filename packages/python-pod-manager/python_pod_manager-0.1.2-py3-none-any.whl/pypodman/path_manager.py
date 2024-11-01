import os
import sys
import logging

class PathManager:
    @staticmethod
    def set_pythonpath(volume_path):
        """Set the PYTHONPATH environment variable."""
        original_path = os.environ.get('PYTHONPATH', '')
        new_path = f"{volume_path}:{original_path}" if original_path else volume_path
        os.environ['PYTHONPATH'] = new_path
        sys.path.insert(0, volume_path)
        
        logging.info(f"PYTHONPATH updated to include volume path: {volume_path}")
        logging.debug(f"New PYTHONPATH: {new_path}")

    def configure_paths(self, pod_name, base_path):
        """Configure paths for a pod."""
        volume_path = self.get_volume_path(pod_name, base_path)
        self.set_pythonpath(volume_path)
        logging.info(f"Paths configured for pod '{pod_name}' with base path '{base_path}'.")

    def get_volume_path(self, pod_name, base_path):
        """Generate and ensure volume path exists."""
        volume_path = os.path.join(base_path, f"libs/{pod_name}_lib")
        try:
            os.makedirs(volume_path, exist_ok=True)
            logging.info(f"Volume path created or verified: {volume_path}")
        except OSError as e:
            logging.error(f"Failed to create volume path '{volume_path}': {e}")
            raise
        return volume_path

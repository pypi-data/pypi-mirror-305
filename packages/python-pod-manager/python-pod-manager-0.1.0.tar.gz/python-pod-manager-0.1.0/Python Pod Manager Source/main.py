import os
import logging
import threading
from .path_manager import PathManager
from .pod_manager import PodManager
from .service_manager import ServiceManager
from .config_loader import ConfigLoader
from .logger_manager import LoggerManager


class DockerManagerApp:
    """Docker Manager application."""
    DEFAULT_PATH = os.path.expanduser("~/Docker-Manager")
    
    def __init__(self, config_path=None):
        logging.info("Initializing DockerManagerApp")
        
        self.config = ConfigLoader(config_path).config
        self.host_mount_path = self.config.get("mount", {}).get("host_mount_path", self.DEFAULT_PATH)
        self.pod_mount_path = self.config.get("mount", {}).get("pod_mounth_path", "/app")

        self.image_name = self.config.get("docker", {}).get("image_name", "python:latest")
        self.working_dir = self.config.get("docker", {}).get("working_dir", "/app")
        self.version = self.config.get("pod", {}).get("version", "latest")
        self.pod_name = self.config.get("pod", {}).get("custom_pod_name", "default_pod_name")
        self.custom_commands = self.config.get("custom_commands", {})
        self.compose_file = self.config.get("deployment", {}).get("compose_file", "docker-compose.yml")
        
        self.path_manager = PathManager()
        self.pod_manager = PodManager()
        self.service_manager = ServiceManager()
        self.library_names = ConfigLoader().get_library_names()

    def start_pods(self):
        """Start pods based on the configuration."""
        use_single_pod = self.config.get("pod", {}).get("use_single_pod", True)
        logging.info("Starting pods; use_single_pod is set to %s", use_single_pod)
        if use_single_pod:
            self._start_single_pod()
        else:
            self._start_multiple_pods()

    def _start_single_pod(self):
        """Start a single pod."""
        logging.info("Starting a single pod: %s", self.pod_name)
        self._run_pod_threads(
            pod_func=self.pod_manager.build_single_pod,
            service_func=self.service_manager.single_pod_service_config,
            pod_args=(self.library_names, self.image_name, self.working_dir, self.pod_name, self.custom_commands),
            service_args=(self.pod_name, self.version, self.host_mount_path, self.pod_mount_path, self.compose_file)
        )
        self.path_manager.configure_paths(self.pod_name, self.host_mount_path)
        logging.info("Single pod '%s' started successfully.", self.pod_name)

    def _start_multiple_pods(self):
        """Start multiple pods based on the libraries configuration."""
        logging.info("Starting multiple pods for libraries: %s", self.library_names)
        self._run_pod_threads(
            pod_func=self.pod_manager.build_multiple_pods,
            service_func=self.service_manager.multi_pod_service_config,
            pod_args=(self.library_names, self.image_name, self.working_dir, self.custom_commands),
            service_args=(self.library_names, self.version, self.host_mount_path, self.pod_mount_path, self.compose_file)
        )
        for lib_name in self.library_names:
            self.path_manager.configure_paths(lib_name.replace("==", "_"), self.host_mount_path)
            logging.info("Configured paths for library pod '%s'", lib_name)

    def _run_pod_threads(self, pod_func, service_func, pod_args, service_args):
        """Run pod and service functions in threads."""
        logging.info("Starting pod and service threads.")
        threads = [
            threading.Thread(target=pod_func, args=pod_args),
            threading.Thread(target=service_func, args=service_args)
        ]
        for thread in threads:
            thread.start()
            logging.debug("Started thread: %s", thread.name)
        for thread in threads:
            thread.join()
            logging.debug("Thread completed: %s", thread.name)
        logging.info("All pod threads completed.")

    def run(self):
        """Run the DockerManagerApp."""
        LoggerManager(self.DEFAULT_PATH).configure_logging()
        logging.info("DockerManagerApp run started.")
        try:
            self.start_pods()
            logging.info("DockerManagerApp run completed successfully.")
        except Exception as e:
            logging.error("Error during DockerManagerApp run: %s", e)
            raise

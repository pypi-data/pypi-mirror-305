import subprocess
import logging
from .config_loader import ConfigLoader

class AppManager:
    def __init__(self, config_path=None):
        self.config_loader = ConfigLoader(config_path)
        self.config = self.config_loader.get_deployment_config()
        self.stack_name = self.config.get("stack_name", "my_stack")
        self.deployment_mode = self.config.get("deployment_mode", "compose")
        self.compose_file = self.config.get("compose_file", "docker-compose.yml")

    def start_app(self):
        """Start the application using Docker Stack or Docker Compose based on configuration."""
        if self.deployment_mode == "stack":
            # Use Docker Stack to deploy
            try:
                subprocess.run(
                    ["docker", "stack", "deploy", "-c", self.compose_file, self.stack_name],
                    check=True
                )
                logging.info("Application started with Docker Stack successfully.")
            except subprocess.CalledProcessError as e:
                logging.error(f"Failed to start application with Docker Stack: {e}")
        elif self.deployment_mode == "compose":
            # Use Docker Compose to deploy
            try:
                subprocess.run(
                    ["docker-compose", "-f", self.compose_file, "up", "-d"],
                    check=True
                )
                logging.info("Application started with Docker Compose successfully.")
            except subprocess.CalledProcessError as e:
                logging.error(f"Failed to start application with Docker Compose: {e}")

    def stop_app(self):
        """Stop the application using Docker Stack or Docker Compose based on configuration."""
        if self.deployment_mode == "stack":
            try:
                subprocess.run(
                    ["docker", "stack", "rm", self.stack_name],
                    check=True
                )
                logging.info("Application stopped with Docker Stack successfully.")
            except subprocess.CalledProcessError as e:
                logging.error(f"Failed to stop application with Docker Stack: {e}")
        elif self.deployment_mode == "compose":
            try:
                subprocess.run(
                    ["docker-compose", "-f", self.compose_file, "down"],
                    check=True
                )
                logging.info("Application stopped with Docker Compose successfully.")
            except subprocess.CalledProcessError as e:
                logging.error(f"Failed to stop application with Docker Compose: {e}")

    def restart_app(self):
        """Restart the application."""
        self.stop_app()
        self.start_app()

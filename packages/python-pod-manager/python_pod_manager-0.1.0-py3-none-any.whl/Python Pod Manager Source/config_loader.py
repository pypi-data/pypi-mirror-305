import yaml
import logging
import os

class ConfigLoader:
    DEFAULT_CONFIG_PATH = os.path.join(os.getcwd(), "config.yaml")

    def __init__(self, config_path=None):
        self.config_path = config_path or ConfigLoader.DEFAULT_CONFIG_PATH
        self.config = self.load_config(self.config_path)

    def load_config(self, config_path):
        """Load configuration from a YAML file."""
        try:
            with open(config_path, "r") as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            logging.error(f"Configuration file not found: {config_path}")
            return {}
        except yaml.YAMLError as e:
            logging.error(f"Error parsing YAML: {e}")
            return {}

    def get_library_names(self):
        """
        Get library names and versions from the config.
        Handle libraries as either a list of dictionaries or a requirements file.
        """
        names = []
        cwd = os.getcwd()  # Get the current working directory

        libraries = self.config.get("libraries", {})

        # Check if `libraries` is a dictionary
        if isinstance(libraries, dict):
            # Attempt to read libraries from the specified requirements file if provided
            if 'requirements_file' in libraries and 'path' in libraries:
                requirements_file = os.path.join(libraries['path'], libraries['requirements_file'])
                try:
                    with open(requirements_file, "r") as file:
                        names = [
                            line.strip() for line in file 
                            if line.strip() and not line.startswith("#")
                        ]
                    return names  # Return names if successfully read from custom path
                except FileNotFoundError:
                    logging.error(f"Custom requirements file not found: {requirements_file}")

            # Fallback to the default requirements.txt file in the current working directory
            default_requirements_file = os.path.join(cwd, libraries['requirements_file'])
            try:
                with open(default_requirements_file, "r") as file:
                    names = [
                        line.strip() for line in file 
                        if line.strip() and not line.startswith("#")
                    ]
                return names  # Return names if successfully read from the default path
            except FileNotFoundError:
                logging.error(f"Requirements file not found in current working directory: {default_requirements_file}")

        # Process libraries if they are provided as a list of dicts
        if isinstance(libraries, list):
            for lib in libraries:
                if isinstance(lib, dict):  # Only process if lib is a dictionary
                    name = lib.get("name")
                    version = lib.get("version")
                    if name:
                        names.append(f"{name}=={version}" if version else name)
            return names

        # Log a warning if libraries format is unexpected
        logging.warning("Unexpected format for libraries in the config.")
        return names

    def get_deployment_config(self):
        """Get the deployment configuration from the main config."""
        return self.config.get("deployment", {})
    
    def get_additional_config(self):
        """Get the additional configuration from the main config."""
        return self.config.get("additional", {})

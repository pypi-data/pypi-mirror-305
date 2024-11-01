import logging
import yaml
from .path_manager import PathManager

class ServiceManager:
    def __init__(self):
        self.path_manager = PathManager()
        logging.debug("Initialized ServiceManager with PathManager.")

    def create_service_definition(self, pod_name, image_name, volume_name, work_dir):
        """Create a service definition for a pod."""
        service_def = {
            pod_name: {
                "image": image_name,
                "volumes": [f"{volume_name}:{work_dir}"],
                "deploy": {"replicas": 1},  # Default to one replica; adjust as necessary
            }
        }
        logging.debug(f"Service definition created for pod '{pod_name}': {service_def}")
        return service_def

    def create_volume_definition(self, volume_name, base_path):
        """Create a volume definition for a pod."""
        volume_def = {
            volume_name: {
                "driver": "local",
                "driver_opts": {"device": base_path, "o": "bind", "type": "none"},
            }
        }
        logging.debug(f"Volume definition created for volume '{volume_name}': {volume_def}")
        return volume_def

    def build_single_pod_service_config(self, custom_pod_name, version, custom_path, work_dir):
        """Generate Docker Compose config for a single pod."""
        volume_name = f"{custom_pod_name}_lib"
        volume_path = self.path_manager.get_volume_path(custom_pod_name, custom_path)
        logging.info(f"Building single pod service config for '{custom_pod_name}' with volume path '{volume_path}'.")
        
        services = self.create_service_definition(custom_pod_name, f"{custom_pod_name}:{version}", volume_name, work_dir)
        volumes = self.create_volume_definition(volume_name, volume_path)
        
        compose_config = {"version": "3.8", "services": services, "volumes": volumes}
        logging.debug(f"Single pod Docker Compose configuration: {compose_config}")
        return compose_config

    def build_multi_pod_service_config(self, library_names, version, custom_path, work_dir):
        """Generate Docker Compose config for multiple pods."""
        services = {}
        volumes = {}
        logging.info(f"Building multi-pod service config for libraries: {library_names}")

        for pod_name in library_names:
            sanitized_pod_name = pod_name.replace("==", "_")
            volume_name = f"{sanitized_pod_name}_lib"
            volume_path = self.path_manager.get_volume_path(sanitized_pod_name, custom_path)
            
            logging.debug(f"Configuring service and volume for pod '{sanitized_pod_name}' with volume path '{volume_path}'.")
            
            services.update(self.create_service_definition(sanitized_pod_name, f"{sanitized_pod_name}:{version}", volume_name, work_dir))
            volumes.update(self.create_volume_definition(volume_name, volume_path))
        
        compose_config = {"version": "3.8", "services": services, "volumes": volumes}
        logging.debug(f"Multi-pod Docker Compose configuration: {compose_config}")
        return compose_config

    def single_pod_service_config(self, custom_pod_name, version, custom_path, work_dir, compose_file):
        """Create and write Docker Compose config for a single pod."""
        logging.info(f"Creating Docker Compose config for single pod '{custom_pod_name}'.")
        compose_config = self.build_single_pod_service_config(custom_pod_name, version, custom_path, work_dir)
        self.write_compose_file(compose_config, compose_file)

    def multi_pod_service_config(self, library_names, version, custom_path, work_dir, compose_file):
        """Create and write Docker Compose config for multiple pods."""
        logging.info("Creating Docker Compose config for multiple pods.")
        compose_config = self.build_multi_pod_service_config(library_names, version, custom_path, work_dir)
        self.write_compose_file(compose_config, compose_file)

    def write_compose_file(self, compose_config, compose_file):
        """Write Docker Compose configuration to a file."""
        try:
            with open(compose_file, "w") as file:
                yaml.dump(compose_config, file, default_flow_style=False)
            logging.info(f"Docker Compose file successfully written: {compose_file}")
        except (OSError, yaml.YAMLError) as e:
            logging.error(f"Failed to write Docker Compose file: {compose_file}. Error: {e}")

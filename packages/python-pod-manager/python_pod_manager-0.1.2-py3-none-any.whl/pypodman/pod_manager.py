import os
import logging
import subprocess

class PodManager:
    @staticmethod
    def create_dockerfile(pod_name, packages, image_name, working_dir, custom_commands):
        """Create a Dockerfile for a pod."""

        if isinstance(packages, list):
            packages = " ".join(packages)
            
        logging.debug(f"Packages formatted for Dockerfile: {packages}")

        formatted_commands = ""
        for cmd in custom_commands:
            try:
                command = cmd["command"].format(packages=packages, working_dir=working_dir)
                formatted_commands += f"{cmd['name']} {command}\n"
            except KeyError as e:
                logging.error(f"Missing placeholder in command: {cmd}. Error: {e}")
                raise

        dockerfile_content = f"""
        FROM {image_name}
        WORKDIR {working_dir}
        {formatted_commands}
        """
        logging.debug(f"Dockerfile content generated for pod '{pod_name}':\n{dockerfile_content}")

        dockerfile_path = os.path.join(os.getcwd(), pod_name, "Dockerfile")
        os.makedirs(os.path.dirname(dockerfile_path), exist_ok=True)

        try:
            with open(dockerfile_path, "w") as file:
                file.write(dockerfile_content.strip())  # Remove leading/trailing whitespace
            logging.info(f"Dockerfile successfully created at: {dockerfile_path}")
        except (OSError, IOError) as e:
            logging.error(f"Failed to write Dockerfile for pod '{pod_name}' at '{dockerfile_path}': {e}")
            raise

        return dockerfile_path

    def build_single_pod(self, library, image_name, working_dir, pod_name, custom_commands):
        """Build a single pod."""
        try:
            dockerfile_path = self.create_dockerfile(
                pod_name, library, image_name, working_dir, custom_commands
            )
            logging.info(f"Starting Docker build for pod '{pod_name}' with Dockerfile at '{dockerfile_path}'")
            subprocess.run(
                ["docker", "build", "-t", pod_name, "-f", dockerfile_path, "."],
                check=True
            )
            logging.info(f"Docker build completed successfully for pod '{pod_name}'")
        except subprocess.CalledProcessError as e:
            logging.error(f"Docker build failed for pod '{pod_name}'. Error: {e}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error in building pod '{pod_name}': {e}")
            raise

    def build_multiple_pods(self, library_names, image_name, working_dir, custom_commands):
        """Build multiple pods."""
        logging.info("Starting the build process for multiple pods.")
        for library in library_names:
            pod_name = library.replace("==", "_")
            logging.info(f"Building pod '{pod_name}' for library '{library}'")
            try:
                self.build_single_pod(library, image_name, working_dir, pod_name, custom_commands)
            except Exception as e:
                logging.error(f"Failed to build pod '{pod_name}'. Error: {e}")
                continue
        logging.info("Build process for multiple pods completed.")

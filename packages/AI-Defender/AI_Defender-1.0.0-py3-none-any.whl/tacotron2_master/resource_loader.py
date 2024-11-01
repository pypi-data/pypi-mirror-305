import os
import logging

def load_resource(resource_name: str) -> str:
    """
    Loads a resource from the resources directory.

    Args:
        resource_name (str): The absolute path or name of the resource file to load.

    Returns:
        str: The content of the resource file.
    """
    try:
        # Check if the resource_name provided is an absolute path or relative path
        if not os.path.isabs(resource_name):
            resource_path = os.path.join(os.path.dirname(__file__), 'resources', resource_name)
        else:
            resource_path = resource_name

        # Check if the file exists
        if not os.path.exists(resource_path):
            logging.error(f"Resource file does not exist: {resource_path}")
            raise FileNotFoundError(f"No such file or directory: '{resource_path}'")

        # Load the content of the resource file
        with open(resource_path, 'r') as file:
            return file.read()
    except Exception as e:
        logging.error(f"Error loading resource: {e}")
        raise

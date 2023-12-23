import os
import yaml
from typing import Any, Dict, Optional


def load_yaml(path: str, object_hook: Optional[Any] = None) -> Dict:
    """
    Load a YAML file from the given path.

    :param path: Path to the YAML file.
    :param object_hook: Optional function to apply to the loaded data.
    :return: A dictionary containing the data from the YAML file, or an empty dict if the file doesn't exist or an error occurs.
    """
    try:
        if os.path.exists(path):
            with open(path, "r") as yaml_data:
                data = yaml.safe_load(yaml_data)
                if object_hook:
                    return object_hook(data)
                return data or {}
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file {path}: {e}")
    except Exception as e:
        print(f"Unexpected error while reading {path}: {e}")

    return {}


def save_yaml(path: str, data: Dict) -> bool:
    """
    Save a dictionary to a YAML file.

    :param path: Path to save the YAML file.
    :param data: Dictionary to be saved.
    :return: True if the operation was successful, False otherwise.
    """
    try:
        with open(path, "w") as f:
            yaml.dump(data, f)
        return True
    except Exception as e:
        print(f"Failed to save data to {path}: {e}")
        return False

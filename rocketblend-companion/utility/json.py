import json
import os
from typing import Any, Dict, Optional


def load_json(path: str, object_hook: Optional[Any] = None) -> Dict:
    """
    Load a JSON file from the given path.

    :param path: Path to the JSON file.
    :param object_hook: Optional function to apply to the loaded data.
    :return: A dictionary containing the data from the JSON file, or an empty dict if the file doesn't exist.
    """
    try:
        if os.path.exists(path):
            with open(path, "r") as json_data:
                return json.load(json_data, object_hook=object_hook)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from {path}: {e}")
    except Exception as e:
        print(f"Unexpected error while reading {path}: {e}")

    return {}


def save_json(path: str, data: Dict) -> bool:
    """
    Save a dictionary to a JSON file.

    :param path: Path to save the JSON file.
    :param data: Dictionary to be saved.
    :return: True if the operation was successful, False otherwise.
    """
    try:
        with open(path, "w") as f:
            json.dump(data, f)
        return True
    except Exception as e:
        print(f"Failed to save data to {path}: {e}")
        return False

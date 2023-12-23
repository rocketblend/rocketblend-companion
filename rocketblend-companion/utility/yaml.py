import os
import yaml
from typing import Any, Optional, Dict

def load_yaml(path: str, object_hook: Optional[Any] = None) -> Dict:
    if os.path.exists(path):
        with open(path) as yaml_data:
            # Load the YAML file
            data = yaml.safe_load(yaml_data)
            if object_hook:
                # If an object hook is provided, apply it to the data
                return object_hook(data)
            return data
    return {}

def save_yaml(path: str, data: Dict) -> None:
    with open(path, 'w') as f:
        # Dump the data to a YAML file
        yaml.dump(data, f)
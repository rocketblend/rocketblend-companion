import json
import os

def load_json(path, object_hook=None):
    if os.path.exists(path):
        with open(path) as json_data:
            return json.load(json_data, object_hook=object_hook)
    return {}

def save_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f)
    return
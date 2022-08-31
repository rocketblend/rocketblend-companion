import json
import os

def load_json(path):
    if os.path.exists(path):
        with open(path) as json_data:
            return json.load(json_data)
    return {}

def save_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f)
    return
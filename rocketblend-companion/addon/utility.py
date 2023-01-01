import os

from ..utility.json import load_json, save_json

ROCKET_CONFIG_FILE = "rocketfile.json"
BUILD_CONFIG_FILE = "build.json"

def load_build_json(path: str) -> dict:
    return load_json(os.path.join(path, BUILD_CONFIG_FILE))

def load_rocketfile_json(path) -> dict:
    return load_json(os.path.join(path, ROCKET_CONFIG_FILE))

def save_rocketfile_json(path, build: str, args: str) -> None:
    data = load_rocketfile_json(path)
    
    data['build'] = build
    data['args'] = args

    save_json(os.path.join(path, ROCKET_CONFIG_FILE), data)
import os

from ..utility.yaml import load_yaml, save_yaml

ROCKET_CONFIG_FILE = "rocketfile.json"
BUILD_CONFIG_FILE = "build.json"

def load_build_config(path: str) -> dict:
    return load_yaml(os.path.join(path, BUILD_CONFIG_FILE))

def load_rocketfile_config(path) -> dict:
    return load_yaml(os.path.join(path, ROCKET_CONFIG_FILE))

def save_rocketfile_config(path, build: str) -> None:
    data = load_rocketfile_config(path)
    
    data['build'] = build

    save_yaml(os.path.join(path, ROCKET_CONFIG_FILE), data)
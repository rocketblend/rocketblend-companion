import os

from ..utility.json import load_json, save_json

ROCKET_FILE = "rocketfile.json"
BUILD_CONFIG = "build.json"
PACKAGE_CONFIG = "package.json"

def load_rocketfile_json(path):
    return load_json(os.path.join(path, ROCKET_FILE))

def save_rocketfile_json(path, build, args):
    data = {'build': build, 'args': args}
    save_json(os.path.join(path, ROCKET_FILE), data)

def load_build_json(path):
    return load_json(os.path.join(path, BUILD_CONFIG))
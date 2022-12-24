import os

from ..utility.json import load_json, save_json

ROCKET_CONFIG_FILE = "rocketfile.json"

class Rocketfile(object):
    def __init__(self, build: str, args: str, packages: List[str]):
        self.build = build
        self.args = args
        self.packages = packages

    def to_json(self):
        return json.dumps(dict(self), ensure_ascii=False)

    @classmethod
    def from_json(cls, data):
        return cls(**data)

def load_rocketfile_json(path: str) -> Rocketfile:
    return load_json(os.path.join(path, ROCKET_CONFIG_FILE), object_hook=Rocketfile.from_json)

def save_rocketfile_json(path: str, rocketfile: Rocketfile) -> None:
    save_json(os.path.join(path, ROCKET_CONFIG_FILE), rocketfile.to_json())
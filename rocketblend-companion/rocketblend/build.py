import os

from ..utility.json import load_json, save_json

BUILD_CONFIG_FILE = "build.json"

class Build(object):
    def __init__(self, reference: str, args: str):
        self.reference = reference
        self.args = args

    def to_json(self):
        return json.dumps(dict(self), ensure_ascii=False)

    @classmethod
    def from_json(cls, data):
        return cls(**data)

def load_build_json(path: str) -> Build:
    return load_json(os.path.join(path, BUILD_CONFIG_FILE), object_hook=Build.from_json)
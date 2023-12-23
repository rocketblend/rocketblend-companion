import os
import json

from typing import Optional
from ..utility.yaml import load_yaml, save_yaml
from ..utility.json import load_json
from . import RocketBlendConfig, RocketPack, RocketFile, Build, Addon, RocketBlendFeatures

PROJECT_CONFIG_FILE = "rocketfile.yaml"
PACKAGE_CONFIG_FILE = "rocketpack.yaml"

ROCKETBLEND_APP_NAME = "rocketblend"
ROCKETBLEND_CONFIG_FILE = "settings.json"

def load_rocketblend_config(dev_mode: bool = False) -> Optional[RocketBlendConfig]:
    user_config_dir = os.path.expanduser('~/.config')
    app_dir = os.path.join(user_config_dir, ROCKETBLEND_APP_NAME)
    if dev_mode:
        app_dir = os.path.join(app_dir, "dev")

    config_path = os.path.join(app_dir, ROCKETBLEND_CONFIG_FILE)
    config_data = load_json(config_path)

    if config_data:
        return RocketBlendConfig(
            platform=config_data.get('platform'),
            default_build=config_data.get('defaultBuild'),
            log_level=config_data.get('logLevel'),
            installations_path=config_data.get('installationsPath'),
            packages_path=config_data.get('packagesPath'),
            features=RocketBlendFeatures(**config_data.get('features', {}))
        )
    return None

def load_rocketpack_config(path: str) -> Optional[RocketPack]:
    config_data = load_yaml(os.path.join(path, PACKAGE_CONFIG_FILE))
    if config_data:
        build = None
        if 'build' in config_data:
            build_data = config_data['build']
            build = Build(
                args=build_data.get('Args'),
                version=build_data.get('Version'),
                # sources=build_data.get('Sources'),
                # addons=build_data.get('Addons')
            )

        addon = None
        if 'addon' in config_data:
            addon_data = config_data['addon']
            addon = Addon(
                name=addon_data.get('Name'),
                version=addon_data.get('Version'),
                source=addon_data.get('Source')
            )

        return RocketPack(build=build, addon=addon)
    return None

def load_rocketfile_config(path: str) -> Optional[RocketFile]:
    config_data = load_yaml(os.path.join(path, PROJECT_CONFIG_FILE))
    if config_data:
        return RocketFile(
            build=config_data.get('build'), 
            args=config_data.get('args'), 
            version=config_data.get('version'), 
            addons=config_data.get('addons'))
    return None

def save_rocketfile_config(path: str, config: RocketFile) -> None:
    # Save the dictionary as a YAML file
    save_yaml(os.path.join(path, PROJECT_CONFIG_FILE), config_dict.to_dict())
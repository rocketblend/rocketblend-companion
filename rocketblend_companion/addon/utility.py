import os
import platform
import sys
import subprocess
import webbrowser
import bpy
import addon_utils

from typing import Optional, Tuple, List, cast
from ..utility.yaml import load_yaml, save_yaml
from ..utility.json import load_json
from .types import (
    RocketBlendConfig,
    RocketPack,
    RocketFile,
    Build,
    Addon,
    RocketBlendFeatures,
)

ADDON_IDENTIFIER = "RocketBlend Companion"

PROJECT_CONFIG_FILE = "rocketfile.yaml"
PACKAGE_CONFIG_FILE = "rocketpack.yaml"

ROCKETBLEND_APP_NAME = "rocketblend"
ROCKETBLEND_CONFIG_FILE = "settings.json"


def get_user_config_dir() -> str:
    """
    Get the platform-independent user configuration directory.
    Should return the same as golangs os.UserConfigDir().

    Returns:
        str: The path to the user configuration directory.
    """
    system = platform.system()

    if system == "Windows":
        return os.getenv("APPDATA", os.path.expanduser("~"))
    elif system == "Darwin":  # macOS
        return os.path.join(os.path.expanduser("~"), "Library", "Application Support")
    else:  # Linux and other UNIX-like systems
        return os.path.expanduser("~/.config")


def get_addon_version() -> str:
    """
    Gets the version of the specified addon using its identifier.

    :return: A string representation of the addon version.
    """

    for addon in addon_utils.modules():
        if addon.bl_info.get("name") == ADDON_IDENTIFIER:
            version = addon.bl_info.get("version", (0, 0, 0))
            return ".".join(map(str, version))
    return "Unknown"


def get_rocketblend_config_dir(dev_mode: bool = False) -> str:
    user_config_dir = get_user_config_dir()
    app_dir = os.path.join(user_config_dir, ROCKETBLEND_APP_NAME)
    if dev_mode:
        app_dir = os.path.join(app_dir, "dev")

    return app_dir


def get_rocketblend_config_path(dev_mode: bool = False) -> str:
    return os.path.join(get_rocketblend_config_dir(dev_mode), ROCKETBLEND_CONFIG_FILE)


def get_rocketblend_version() -> Optional[str]:
    success, output = run_command("rocketblend", ["--version"])
    if success:
        return output
    return None


def is_none_or_whitespace(s: str | None) -> bool:
    return s is None or not s.strip()


def load_rocketblend_config(config_path: str) -> Optional[RocketBlendConfig]:
    config_data = load_json(config_path)

    if config_data:
        return RocketBlendConfig(
            platform=config_data.get("platform"),
            default_build=config_data.get("defaultBuild"),
            log_level=config_data.get("logLevel"),
            installations_path=config_data.get("installationsPath"),
            packages_path=config_data.get("packagesPath"),
            features=RocketBlendFeatures(**config_data.get("features", {})),
        )
    return None


def load_rocketpack_config(path: str) -> Optional[RocketPack]:
    config_data = load_yaml(os.path.join(path, PACKAGE_CONFIG_FILE))
    if config_data:
        build = None
        if "build" in config_data:
            build_data = config_data["build"]
            build = Build(
                args=build_data.get("args"),
                version=build_data.get("version"),
                # sources=build_data.get('Sources'),
                # addons=build_data.get('Addons')
            )

        addon = None
        if "addon" in config_data:
            addon_data = config_data["addon"]
            addon = Addon(
                name=addon_data.get("name"),
                version=addon_data.get("version"),
                source=addon_data.get("source"),
            )

        return RocketPack(build=build, addon=addon)
    return None


def load_rocketfile_config(path: str) -> Optional[RocketFile]:
    config_data = load_yaml(os.path.join(path, PROJECT_CONFIG_FILE))
    if config_data:
        return RocketFile(
            build=cast(str, config_data.get("build")),
            args=config_data.get("args"),
            version=config_data.get("version"),
            addons=config_data.get("addons"),
        )
    return None


def save_rocketfile_config(path: str, config: RocketFile) -> None:
    save_yaml(os.path.join(path, PROJECT_CONFIG_FILE), config.to_dict())


def open_in_file_explorer(path: str) -> None:
    if sys.platform == "win32":
        os.startfile(path)
    elif sys.platform == "darwin":  # macOS
        subprocess.Popen(["open", path])
    else:  # linux variants
        subprocess.Popen(["xdg-open", path])


def run_command(command: str, args: Optional[List[str]] = None) -> Tuple[bool, str]:
    """
    Runs a command using subprocess and returns the status and output.

    :param command: The command to execute.
    :param args: A list of arguments for the command.
    :return: A tuple containing a boolean indicating success, and the command output or error message.
    """
    if args is None:
        args = []

    try:
        result = subprocess.run(
            [command] + args, check=True, text=True, capture_output=True
        )
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, "Error: " + str(e)
    except FileNotFoundError:
        return (
            False,
            f"Command '{command}' not found. Ensure it's installed and in your PATH.",
        )


def open_in_browser(url: str) -> None:
    """
    Opens a url in the default browser.

    :param url: The url to open.
    """
    webbrowser.open(url)

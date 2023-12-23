from typing import List, Optional, Dict, Any


class SemverVersion:
    def __init__(self, version_str: str):
        self.version_str = version_str


class RocketBlendFeatures:
    def __init__(self, addons: bool):
        self.addons = addons


class RocketBlendConfig:
    def __init__(
        self,
        platform: Optional[str],
        default_build: Optional[str],
        log_level: Optional[str],
        installations_path: Optional[str],
        packages_path: Optional[str],
        features: Optional[RocketBlendFeatures],
    ):
        self.platform = platform
        self.default_build = default_build
        self.log_level = log_level
        self.installations_path = installations_path
        self.packages_path = packages_path
        self.features = features


class RocketFile:
    def __init__(
        self,
        build: str,
        args: Optional[str] = None,
        version: Optional[str] = None,
        addons: Optional[List[str]] = None,
    ):
        self.build = build
        self.args = args
        self.version = version
        self.addons = addons or []

    def to_dict(self) -> Dict[str, Any]:
        """Converts the RocketFile instance to a dictionary."""
        return {
            "build": self.build,
            "args": self.args,
            "version": self.version,
            "addons": self.addons,
        }


class Source:
    def __init__(self, resource: Optional[str] = None, uri: Optional[str] = None):
        self.resource = resource
        self.uri = uri


class Build:
    def __init__(
        self,
        args: Optional[str] = None,
        version: Optional[SemverVersion] = None,
        sources: Optional[List[Source]] = None,
        addons: Optional[List[str]] = None,
    ):
        self.args = args
        self.version = version
        self.sources = sources
        self.addons = addons or []


class Addon:
    def __init__(
        self,
        name: str,
        version: Optional[SemverVersion] = None,
        source: Optional[List[Source]] = None,
    ):
        self.name = name
        self.version = version
        self.source = source


class RocketPack:
    def __init__(self, build: Optional[Build] = None, addon: Optional[Addon] = None):
        self.build = build
        self.addon = addon

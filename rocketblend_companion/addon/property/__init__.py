import bpy
from bpy.props import PointerProperty, StringProperty
from bpy.types import PropertyGroup
from bpy.utils import register_class, unregister_class

from ...utility import addon

from . import preference


class runtime(PropertyGroup):
    build: StringProperty(name="Build", default="Current build reference.")  # type: ignore

    installations_path: StringProperty(  # type: ignore
        name="Installations Path",
        default="Path to the installations folder.",
    )

    packages_path: StringProperty(  # type: ignore
        name="Packages Path",
        description="Path to the packages folder.",
    )

    config_path: StringProperty(  # type: ignore
        name="Config Path",
        description="Path to RocketBlends config folder.",
    )

    version: StringProperty(  # type: ignore
        name="Version",
        description="Version of RocketBlend that is currently installed.",
    )


class project(PropertyGroup):
    build: StringProperty(  # type: ignore
        name="Build", description="Project build reference (Blender verison to use). "
    )


classes = [runtime, project]


def register() -> None:
    for cls in classes:
        register_class(cls)

    bpy.types.WindowManager.rkb = PointerProperty(type=runtime)
    bpy.types.WindowManager.rkf = PointerProperty(type=project)


def unregister() -> None:
    del bpy.types.WindowManager.rkf
    del bpy.types.WindowManager.rkb

    for cls in reversed(classes):
        unregister_class(cls)

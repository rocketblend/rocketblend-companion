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

    package_paths: StringProperty(  # type: ignore
        name="Packages Path",
        description="Path to the packages folder.",
    )


class project(PropertyGroup):
    build: StringProperty(  # type: ignore
        name="Build", description="Project build reference (Blender verison to use). "
    )


classes = [runtime, project]


def register():
    for cls in classes:
        register_class(cls)

    bpy.types.WindowManager.rkb = PointerProperty(type=runtime)
    bpy.types.WindowManager.rkf = PointerProperty(type=project)


def unregister():
    del bpy.types.WindowManager.rkf
    del bpy.types.WindowManager.rkb

    for cls in reversed(classes):
        unregister_class(cls)

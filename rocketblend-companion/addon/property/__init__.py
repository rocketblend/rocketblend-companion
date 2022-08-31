import bpy
from bpy.props import PointerProperty, StringProperty
from bpy.types import PropertyGroup
from bpy.utils import register_class, unregister_class

from ... utility import addon

from . import preference

class option(PropertyGroup):
    addon: StringProperty(default=addon.name)

class install(PropertyGroup):
    install: StringProperty(default="unknown")

class config(PropertyGroup):
    build: StringProperty(
        name="Build",
        description="Blender verison to use. Requires restart to take effect."
    )

    launchArgs: StringProperty(
        name = "Launch args",
        description = "Define a launcher arguments to be run when project is launched"
    )

classes = [
    option,
    install,
    config
]

def register():
    for cls in classes:
        register_class(cls)

    bpy.types.WindowManager.rkc = PointerProperty(type=option)
    bpy.types.WindowManager.rki = PointerProperty(type=install)
    bpy.types.WindowManager.rkf = PointerProperty(type=config)


def unregister():
    del bpy.types.WindowManager.rkf
    del bpy.types.WindowManager.rki
    del bpy.types.WindowManager.rkc

    for cls in reversed(classes):
        unregister_class(cls)
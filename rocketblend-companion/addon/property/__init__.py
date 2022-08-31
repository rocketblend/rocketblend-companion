import bpy
from bpy.types import PropertyGroup

from .... utility import addon

class Option(PropertyGroup):
    addon: StringProperty(default=addon.name)

class Build(PropertyGroup):
    build: StringProperty(default="unknown")

class Config(PropertyGroup):
    build: props.StringProperty(
        name="Build",
        description="Blender verison to use. Requires restart to take effect."
    )

    launchArgs: props.StringProperty(
		name = "Launch args",
		description = "Define a launcher arguments to be run when project is launched"
    )

classes = [
    Option,
    Build,
    Config
]

def register():
    for cls in classes:
        register_class(cls)

    bpy.types.WindowManager.rkc = PointerProperty(type=Option)
    bpy.types.WindowManager.rkb = PointerProperty(type=Build)
    bpy.types.WindowManager.rkf = PointerProperty(type=Config)


def unregister():
    del bpy.types.WindowManager.rf

    for cls in reversed(classes):
        unregister_class(cls)
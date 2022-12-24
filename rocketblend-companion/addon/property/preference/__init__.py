import bpy
import os

from pathlib import Path
from bpy.utils import register_class, unregister_class
from bpy.types import AddonPreferences
from bpy.props import StringProperty

from ....utility import addon

class RocketBlend(AddonPreferences):
    bl_idname = addon.name

    # installationPath: StringProperty(
    #     name = "Installation Path",
    #     default = os.path.join(Path.home(), ".rocketblend", "installations"), # Move out
    #     description = "Default installation path for new versions of blender."
    # )

    def draw(self, context):
        layout = self.layout
        # layout.prop(self, "installationPath")

classes = [
    RocketBlend,
]

def register():
    for cls in classes:
        register_class(cls)


def unregister():
    for cls in reversed(classes):
        unregister_class(cls)
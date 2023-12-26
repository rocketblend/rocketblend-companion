import bpy
import os

from pathlib import Path
from bpy.utils import register_class, unregister_class
from bpy.types import AddonPreferences
from bpy.props import BoolProperty

from ....utility import addon


class RocketBlend(AddonPreferences):
    bl_idname = addon.name

    dev_mode: BoolProperty(  # type: ignore
        name="Development Mode",
        description="Enable development mode.",
        default=False,
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "dev_mode")


classes = [
    RocketBlend,
]


def register() -> None:
    for cls in classes:
        register_class(cls)


def unregister() -> None:
    for cls in reversed(classes):
        unregister_class(cls)

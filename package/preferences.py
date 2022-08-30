import os
import logging
log = logging.getLogger(__name__)

import bpy
from bpy import props
from bpy import types

from pathlib import Path

PKG = __package__

class ROCKETBLEND_AP_preferences(types.AddonPreferences):
    bl_idname = PKG

    # TODO - Load values from config.

    installationPath: props.StringProperty(
		name = "Installation Path",
        default = os.path.join(Path.home(), ".rocketblend", "installations"),
		description = "Default installation path for new versions of blender.")

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "installationPath")


class ROCKETBLEND_PT_property(types.PropertyGroup):
    build: props.StringProperty(
        name="Build",
        description="Blender verison to use. Requires restart to take effect.")

    launchArgs: props.StringProperty(
		name = "Launch args",
		description = "Define a launcher arguments to be run when project is launched")
        

class ROCKETBLEND_PT_panel(types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Project Settings"
    bl_idname = "SCENE_PT_layout"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    def draw(self, context):
        rocketfile = context.window_manager.rocketfile

        layout = self.layout

        layout.prop(rocketfile, "build")
        layout.prop(rocketfile, "launchArgs")
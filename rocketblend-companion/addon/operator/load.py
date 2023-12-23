import bpy
from bpy.types import Operator
from pathlib import Path

from .. import utility

import logging
log = logging.getLogger(__name__)

class RKB_OT_load(bpy.types.Operator):
    """Loads all the configurations for the current project"""
    bl_idname = "rkb.load"
    bl_label = "Loader"

    def execute(self, context):
        runtime_build = utility.load_build_config(Path(bpy.app.binary_path).resolve().parent.parent)

        bpy.context.window_manager.rkb.build = runtime_build.get("build", "unknown")

        rocketfile = utility.load_rocketfile_config(bpy.path.abspath("//"))

        bpy.context.window_manager.rkf.build = rocketfile.get("build", bpy.context.window_manager.rkb.reference)

        if bpy.context.window_manager.rkb.build != bpy.context.window_manager.rkf.build:
            self.report({'ERROR'}, "This project is not compatible with the current build (RocketBlend)")

        return {'FINISHED'}
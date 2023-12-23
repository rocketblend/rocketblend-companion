import bpy
from bpy.types import Operator

from .. import utility

import logging
log = logging.getLogger(__name__)

class RKB_OT_save(bpy.types.Operator):
    """Saves all the configurations for the current project"""
    bl_idname = "rkb.save"
    bl_label = "Save configuration"

    def execute(self, context):
        rocketfile = bpy.context.window_manager.rkf
        utility.save_rocketfile_config(bpy.path.abspath("//"), rocketfile.build)

        self.report({'INFO'}, "Saved rocketfile")

        return {'FINISHED'}

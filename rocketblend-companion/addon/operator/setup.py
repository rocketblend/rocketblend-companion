import bpy
from bpy.types import Operator

import logging
log = logging.getLogger(__name__)

class RKB_OT_setup(bpy.types.Operator):
    """Setups the current window per configuration"""
    bl_idname = "rkb.setup"
    bl_label = "Setup"

    def execute(self, context):
        reference = bpy.context.window_manager.rkb.reference
        build = bpy.context.window_manager.rkf.build

        if reference != build:
            self.report({'ERROR'}, "This project is not compatible with the current build (RocketBlend)")

        # TODO: Refresh packages

        return {'FINISHED'}

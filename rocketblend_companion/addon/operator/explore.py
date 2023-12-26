import bpy
from bpy.types import Operator

from .. import utility


class RKB_OT_explore(bpy.types.Operator):
    """Open a file explorer window at the given path"""

    bl_idname = "rkb.explore"
    bl_label = "Open in File Explorer"
    bl_options = {"REGISTER"}

    path: bpy.props.StringProperty()  # type: ignore

    def execute(self, context):
        utility.open_in_file_explorer(self.path)
        return {"FINISHED"}

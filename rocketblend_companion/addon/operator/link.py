import bpy
from bpy.types import Operator

from .. import utility


class RKB_OT_link(bpy.types.Operator):
    bl_idname = "rkb.link"
    bl_label = "Open a link in your browser"

    url: bpy.props.StringProperty()  # type: ignore

    def execute(self, context):
        utility.open_in_browser(self.url)
        return {"FINISHED"}

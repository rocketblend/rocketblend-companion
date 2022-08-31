
from bpy.utils import register_class, unregister_class
from bpy.types import Panel

class RKB_PT_panel(Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Project Settings"
    bl_idname = "SCENE_PT_layout"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    def draw(self, context):
        rocketfile = context.window_manager.rkf
        layout = self.layout
        layout.prop(rocketfile, "build")
        layout.prop(rocketfile, "launchArgs")

classes = [
    RKB_PT_panel,
]

def register():
    for cls in classes:
        register_class(cls)

def unregister():
    for cls in reversed(classes):
        unregister_class(cls)

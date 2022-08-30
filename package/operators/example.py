import bpy
from bpy.types import Operator

import logging
log = logging.getLogger(__name__)

class ObjectMoveX(Operator):
    """My Object Moving Script"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "object.move_x"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Move X by One"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def execute(self, context):        # execute() is called when running the operator.

        # The original script
        scene = context.scene
        for obj in scene.objects:
            obj.location.x += 1.0

        return {'FINISHED'}            # Lets Blender know the operator finished successfully.

classes = [
	ObjectMoveX,
]

def menu_func(self, context):
    self.layout.operator(ObjectMoveX.bl_idname)

def register():
    try:
        bpy.utils.register_class(ObjectMoveX)
    except ValueError as e:
        log.warning('{} is already registered, now unregister and retry... '.format(ObjectMoveX))
        bpy.utils.unregister_class(ObjectMoveX)
        bpy.utils.register_class(ObjectMoveX)

def unregister():
    bpy.utils.unregister_class(ObjectMoveX)

from bpy.utils import register_class, unregister_class

from . import project

classes = [
    project.RKB_PT_panel,
]

def register():
    for cls in classes:
        register_class(cls)

def unregister():
    for cls in reversed(classes):
        unregister_class(cls)
from bpy.utils import register_class, unregister_class

from . import load, save

classes = [
    load.RKB_OT_load,
    save.RKB_OT_save,
]


def register():
    for cls in classes:
        register_class(cls)


def unregister():
    for cls in reversed(classes):
        unregister_class(cls)

from bpy.utils import register_class, unregister_class

from . import load, explore

classes = [
    load.RKB_OT_load,
    explore.RKB_OT_explore,
    # save.RKB_OT_save,
]


def register() -> None:
    for cls in classes:
        register_class(cls)


def unregister() -> None:
    for cls in reversed(classes):
        unregister_class(cls)

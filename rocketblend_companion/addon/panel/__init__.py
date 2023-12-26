from bpy.utils import register_class, unregister_class

from . import project

classes = [
    project.RKB_PT_panel,
    project.RKB_PT_project_panel,
]


def register() -> None:
    for cls in classes:
        register_class(cls)


def unregister() -> None:
    for cls in reversed(classes):
        unregister_class(cls)

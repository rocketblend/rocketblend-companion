import bpy
from . import panel, operator, property, handler, utility

def register():
    property.preference.register()
    property.register()

    operator.register()
    panel.register()

    bpy.app.handlers.load_post.append(handler.build_load_handler)
    bpy.app.handlers.load_post.append(handler.rocketfile_load_handler)
    bpy.app.handlers.save_post.append(handler.rocketfile_save_handler)

def unregister():
    bpy.app.handlers.save_post.remove(handler.rocketfile_save_handler)
    bpy.app.handlers.load_post.remove(handler.rocketfile_load_handler)
    bpy.app.handlers.load_post.remove(handler.build_load_handler)

    panel.unregister()
    operator.unregister()

    property.unregister()
    property.preference.unregister()
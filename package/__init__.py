import bpy
import os
import json
from bpy.app.handlers import persistent

ROCKET_FILE = "rocketfile.json"

bl_info = {
	'name': 'RocketBlend Companion',
	'description': 'Various tools to aid working with RocketBlend',
	'author': 'lazercube',
	'license': 'GPL',
	'version': (0, 1, 0),
	'blender': (2, 83, 0),
	'location': 'System > RocketBlend > Core',
	'category': 'System'
}

class BlenderVersionError(Exception):
	pass

if bl_info['blender'] > bpy.app.version:
	raise BlenderVersionError(f"This addon requires Blender >= {bl_info['blender']}")

from . import preferences

classes = [
    preferences.ROCKETBLEND_AP_preferences,
    preferences.ROCKETBLEND_PT_panel,
]

@persistent
def rocketfile_save_handler(dummy):
    rocketfile = bpy.context.window_manager.rocketfile

    data = {
        'build': rocketfile.build,
        'args': rocketfile.launchArgs,
        'packages': [], # TODO: Add packages.
    }
    with open(os.path.join(bpy.path.abspath("//"), ROCKET_FILE), 'w') as f:
       json.dump(data, f)

@persistent
def rocketfile_load_handler(dummy):
    path = os.path.join(bpy.path.abspath("//"), ROCKET_FILE)
    data = {}
    if os.path.exists(path):
        with open(path) as json_data:
            data = json.load(json_data)

    bpy.context.window_manager.rocketfile.build = data.get("build","example/3.2.2")
    bpy.context.window_manager.rocketfile.args = data.get("args","")


def register():
    # Manually register properties.
    bpy.utils.register_class(preferences.ROCKETBLEND_PT_property)
    bpy.types.WindowManager.rocketfile = bpy.props.PointerProperty(type=preferences.ROCKETBLEND_PT_property)

    for cls in classes:
        try:
            bpy.utils.register_class(cls)
        except ValueError as e:
            log.warning('{} is already registered, now unregister and retry... '.format(cls))
            bpy.utils.unregister_class(cls)
            bpy.utils.register_class(cls)

    bpy.app.handlers.load_post.append(rocketfile_load_handler)
    bpy.app.handlers.save_post.append(rocketfile_save_handler)

def unregister():
    bpy.app.handlers.save_post.remove(rocketfile_save_handler)
    bpy.app.handlers.load_post.remove(rocketfile_load_handler)

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    del(bpy.types.WindowManager.rocketfile)
    bpy.utils.unregister_class(preferences.ROCKETBLEND_PT_property)

if __name__ == "__main__":
	register()
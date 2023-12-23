import bpy
import os
import json
from bpy.app.handlers import persistent

bl_info = {
	'name': 'RocketBlend Companion',
	'description': 'Various tools to aid working with RocketBlend',
	'author': 'RocketBlend',
	'license': 'GPL',
	'version': (0, 1, 1),
	'blender': (2, 83, 0),
	'location': 'System > RocketBlend > Companion',
	'category': 'System'
}

class BlenderVersionError(Exception):
	pass

if bl_info['blender'] > bpy.app.version:
	raise BlenderVersionError(f"This addon requires Blender >= {bl_info['blender']}")

from . import addon

def register():
    addon.register()

def unregister():
    addon.unregister()

if __name__ == "__main__":
	register()
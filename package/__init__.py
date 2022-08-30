import bpy

bl_info = {
	'name': 'RocketBlend',
	'description': 'Various tweaks to work with RocketBlend',
	'author': 'lazercube',
	'license': 'GPL',
	'deps': '',
	'version': (0, 1, 0),
	'blender': (2, 83, 0),
	'location': 'RocketBlend > Tools > Core',
	'warning': '',
	'link': '',
	'support': 'COMMUNITY',
	'category': 'RocketBlend'
	}

class BlenderVersionError(Exception):
	pass

if bl_info['blender'] > bpy.app.version:
	raise BlenderVersionError(f"This addon requires Blender >= {bl_info['blender']}")

from .operators import example

classes = [
	ObjectMoveX,
]

def menu_func(self, context):
    self.layout.operator(ObjectMoveX.bl_idname)

def register():
    for cls in classes:
        try:
            bpy.utils.register_class(cls)
        except ValueError as e:
            log.warning('{} is already registered, now unregister and retry... '.format(cls))
            bpy.utils.unregister_class(cls)
            bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
	    bpy.utils.unregister_class(cls)

if __name__ == "__main__":
	register()
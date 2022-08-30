import bpy

bl_info = {
	'name': 'RocketBlend',
	'description': 'Various tweaks to work with RocketBlend',
	'author': 'lazercube',
	'license': 'GPL',
	'version': (0, 1, 0),
	'blender': (2, 83, 0),
	'location': 'RocketBlend > Tools > Core',
	'category': 'RocketBlend'
	}

class BlenderVersionError(Exception):
	pass

if bl_info['blender'] > bpy.app.version:
	raise BlenderVersionError(f"This addon requires Blender >= {bl_info['blender']}")

from .operators import example

classes = [
	example.ObjectMoveX,
]

def menu_func(self, context):
     self.layout.operator(example.ObjectMoveX.bl_idname)

def register():
    for cls in classes:
        try:
            bpy.utils.register_class(cls)
        except ValueError as e:
            log.warning('{} is already registered, now unregister and retry... '.format(cls))
            bpy.utils.unregister_class(cls)
            bpy.utils.register_class(cls)
    bpy.types.VIEW3D_MT_object.append(menu_func)  # Adds the new operator to an existing menu.

def unregister():
    classes_reverse = classes
    classes_reverse.reverse()
    for cls in classes_reverse:
	    bpy.utils.unregister_class(cls)
    bpy.types.VIEW3D_MT_object.remove(menu_func)

if __name__ == "__main__":
	register()
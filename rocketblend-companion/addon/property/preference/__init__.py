import bpy

from bpy.utils import register_class, unregister_class
from bpy.types import AddonPreferences
from .... utility import addon

class RocketBlend(AddonPreferences):
    bl_idname = addon.name

    installationPath: props.StringProperty(
	      name = "Installation Path",
        default = os.path.join(Path.home(), ".rocketblend", "installations"),
		    description = "Default installation path for new versions of blender.")

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "installationPath")
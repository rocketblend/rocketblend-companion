import bpy

from pathlib import Path
from bpy.app.handlers import persistent

from . import utility

@persistent
def current_build_load_handler(_):
    data = utility.load_build_json(Path(bpy.app.binary_path).resolve().parent.parent)
    bpy.context.window_manager.rkb.build = data.get("reference", "unknown")

@persistent
def rocketfile_load_handler(_):
    data = utility.load_rocketfile_json(bpy.path.abspath("//"))
    default = bpy.context.window_manager.rkb.build
    bpy.context.window_manager.rkf.build = data.get("build", default)
    bpy.context.window_manager.rkf.args = data.get("args","")

@persistent
def rocketfile_save_handler(_):
    rocketfile = bpy.context.window_manager.rkf
    utility.save_rocketfile_json(
        bpy.path.abspath("//"),
        rocketfile.build,
        rocketfile.launchArgs)
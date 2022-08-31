import bpy

from pathlib import Path
from bpy.app.handlers import persistent

from . import utility

@persistent
def current_install_load_handler(_):
    install_path = utility.load_build_json(Path(bpy.app.binary_path).resolve().parent.parent)
    data = {}
    bpy.context.window_manager.rkb.build = data.get("build", "unknown")

@persistent
def rocketfile_load_handler(_):
    data = utility.load_rocketfile_json(bpy.path.abspath("//"))
    bpy.context.window_manager.rkf.build = data.get("build", "unknown")
    bpy.context.window_manager.rkf.args = data.get("args","")

@persistent
def rocketfile_save_handler(_):
    rocketfile = bpy.context.window_manager.rocketfile
    utility.save_rocketfile(
        bpy.path.abspath("//"),
        rocketfile.build,
        rocketfile.launchArgs)
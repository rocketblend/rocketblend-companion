import bpy

from pathlib import Path
from bpy.app.handlers import persistent

from . import utility

@persistent
def build_load_handler(_) -> None:
    build = utility.load_build_json(Path(bpy.app.binary_path).resolve().parent.parent)

    bpy.context.window_manager.rkb.reference = build.get("reference", "unknown")
    bpy.context.window_manager.rkb.args = build.get("args", "")

@persistent
def rocketfile_load_handler(_) -> None:
    rocketfile = utility.load_rocketfile_json(bpy.path.abspath("//"))

    bpy.context.window_manager.rkf.build = rocketfile.get("build", bpy.context.window_manager.rkb.reference)
    bpy.context.window_manager.rkf.args = rocketfile.get("args", "")

@persistent
def rocketfile_save_handler(_) -> None:
    rocketfile = bpy.context.window_manager.rkf
    rocketblend.save_rocketfile_json(bpy.path.abspath("//"), rocketfile.build, rocketfile.args)
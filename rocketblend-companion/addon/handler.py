import bpy

from pathlib import Path
from bpy.app.handlers import persistent

from .. import rocketblend

@persistent
def build_load_handler(_) -> None:
    build = rocketblend.load_build_json(Path(bpy.app.binary_path).resolve().parent.parent)
    bpy.context.window_manager.rkb.build = build

@persistent
def rocketfile_load_handler(_) -> None:
    rocketfile = rocketblend.load_rocketfile_json(bpy.path.abspath("//"))
    build = bpy.context.window_manager.rkb

    if not rocketfile.build:
        rocketfile.build = build.reference

    bpy.context.window_manager.rkf = rocketfile

@persistent
def rocketfile_save_handler(_) -> None:
    rocketfile = bpy.context.window_manager.rkf
    rocketblend.save_rocketfile_json(bpy.path.abspath("//"), rocketfile)
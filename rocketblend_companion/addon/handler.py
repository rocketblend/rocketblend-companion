import bpy

from pathlib import Path
from bpy.app.handlers import persistent

from . import utility


@persistent
def load_handler(_):
    bpy.ops.rkb.load()


@persistent
def rocketfile_save_handler(_):
    bpy.ops.rkb.save()

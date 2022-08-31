import os

import bpy

from . import new_type

name = __name__.partition('.')[0]
path = new_type(default=lambda new: os.path.abspath(os.path.join(__file__, '..', '..')))
path.icon = os.path.join(path(), 'addon', 'icons')

def preference():
    return bpy.context.preferences.addons[name].preferences

def rkb():
    wm = bpy.context.window_manager

    if hasattr(wm, 'rkb'):
        return bpy.context.preferences.addons[wm.rkb.addon].preferences

    return False
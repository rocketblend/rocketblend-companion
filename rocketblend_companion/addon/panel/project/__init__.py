import bpy
import os

from bpy.utils import register_class, unregister_class
from bpy.types import Panel

from ... import utility

PANEL_CATEGORY = "RocketBlend"


class RKB_PT_panel(Panel):
    bl_label = "RocketBlend"
    bl_idname = "RKB_PT_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = PANEL_CATEGORY

    def draw(self, context):
        layout = self.layout
        wm = context.window_manager

        if utility.is_none_or_whitespace(wm.rkb.version):
            layout.label(text="RocketBlend is not installed.", icon="ERROR")
            return

        layout.label(text=f"Version: {wm.rkb.version}", icon="INFO")

        layout.separator()

        layout.operator(
            "rkb.link", text="Open Documentation", icon="DOCUMENTS"
        ).url = "https://docs.rocketblend.io"

        layout.operator(
            "rkb.link", text="Open Github", icon="DOCUMENTS"
        ).url = "https://github.com/rocketblend/rocketblend"

        layout.separator()

        layout.operator(
            "rkb.explore", text="Explore Config Directory", icon="FILE_FOLDER"
        ).path = wm.rkb.config_path

        layout.operator(
            "rkb.explore", text="Explore Installations Directory", icon="FILE_FOLDER"
        ).path = wm.rkb.installations_path

        layout.operator(
            "rkb.explore", text="Explore Packages Directory", icon="FILE_FOLDER"
        ).path = wm.rkb.packages_path

        layout.separator()

        layout.operator("rkb.load", text="Refresh", icon="FILE_REFRESH")


class RKB_PT_project_panel(Panel):
    bl_label = "Project"
    bl_idname = "RKB_PT_project_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = PANEL_CATEGORY

    def draw(self, context):
        layout = self.layout
        wm = context.window_manager

        error = False
        if utility.is_none_or_whitespace(wm.rkf.build):
            error = True
            layout.label(text="Project build not found!", icon="ERROR")

        if utility.is_none_or_whitespace(wm.rkb.build):
            error = True
            layout.label(text="Current build not found!", icon="ERROR")

        if wm.rkb.build != wm.rkf.build:
            error = True
            layout.label(
                text="This project is not compatible with the current build!",
                icon="ERROR",
            )
            layout.prop(wm.rkf, "build", text="Want", emboss=False)
            layout.prop(wm.rkb, "build", text="Have", emboss=False)

        if error:
            return

        layout.prop(wm.rkf, "build", text="Current Build", emboss=False)
        layout.operator(
            "rkb.explore", text="Explore Project Directory", icon="FILE_FOLDER"
        ).path = os.path.dirname(bpy.data.filepath)


class RKB_PT_companion_panel(Panel):
    bl_label = "Companion"
    bl_idname = "RKB_PT_companion_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = PANEL_CATEGORY

    def draw(self, context):
        layout = self.layout
        wm = context.window_manager

        addon_version = utility.get_addon_version()
        layout.label(text=f"Version: {addon_version}", icon="INFO")

        layout.separator()

        layout.operator(
            "rkb.link", text="Open Documentation", icon="DOCUMENTS"
        ).url = "https://docs.rocketblend.io/v/companion"

        layout.operator(
            "rkb.link", text="Open Github", icon="DOCUMENTS"
        ).url = "https://github.com/rocketblend/rocketblend-companion"


classes = [RKB_PT_panel, RKB_PT_project_panel, RKB_PT_companion_panel]


def register():
    for cls in classes:
        register_class(cls)


def unregister():
    for cls in reversed(classes):
        unregister_class(cls)

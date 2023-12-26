from bpy.utils import register_class, unregister_class
from bpy.types import Panel

PANEL_CATEGORY = "Rocketblend"


class RKB_PT_panel(Panel):
    bl_label = "RocketBlend"
    bl_idname = "RKB_PT_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = PANEL_CATEGORY

    def draw(self, context):
        layout = self.layout
        wm = context.window_manager

        row = layout.row()
        row.operator(
            "rkb.explore", text="Explore Config Directory", icon="FILE_FOLDER"
        ).path = wm.rkb.config_path

        row = layout.row()
        row.operator(
            "rkb.explore", text="Explore Installations Directory", icon="FILE_FOLDER"
        ).path = wm.rkb.installations_path

        row = layout.row()
        row.operator(
            "rkb.explore", text="Explore Packages Directory", icon="FILE_FOLDER"
        ).path = wm.rkb.packages_path

        layout.separator()

        layout.operator("rkb.load", text="Refresh", icon="FILE_REFRESH")


class RKB_PT_runtime_panel(Panel):
    bl_label = "Runtime"
    bl_idname = "RKB_PT_runtime_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = PANEL_CATEGORY

    def draw(self, context):
        layout = self.layout
        wm = context.window_manager

        col = layout.column(align=True)
        col.prop(wm.rkb, "build", text="Build", emboss=False)


class RKB_PT_project_panel(Panel):
    bl_label = "Project"
    bl_idname = "RKB_PT_project_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = PANEL_CATEGORY

    def draw(self, context):
        layout = self.layout
        wm = context.window_manager

        col = layout.column(align=True)
        col.prop(wm.rkf, "build", text="Build", emboss=False)


classes = [RKB_PT_panel, RKB_PT_project_panel, RKB_PT_runtime_panel]


def register():
    for cls in classes:
        register_class(cls)


def unregister():
    for cls in reversed(classes):
        unregister_class(cls)

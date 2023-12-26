import bpy
import os

from bpy.types import Operator
from pathlib import Path

from .. import utility

import logging

log = logging.getLogger(__name__)


class RKB_OT_load(bpy.types.Operator):
    """Loads all the configurations for the current project"""

    bl_idname = "rkb.load"
    bl_label = "Reload RocketBlend Configurations"
    bl_options = {"REGISTER"}

    def execute(self, context):
        log.info("Loading RocketBlend configurations...")

        rocketblend_config_path = utility.get_rocketblend_config_path(True)
        rocketblend_config = utility.load_rocketblend_config(rocketblend_config_path)
        if not rocketblend_config:
            self.report({"ERROR"}, "RocketBlend configuration not found.")
            return {"CANCELLED"}

        if utility.is_none_or_whitespace(rocketblend_config.installations_path):
            self.report({"ERROR"}, "RocketBlend installation path not found.")
            return {"CANCELLED"}

        current_exec_path = Path(bpy.app.binary_path).resolve().parent.parent

        build_reference = (
            str(current_exec_path)
            .replace(rocketblend_config.installations_path, "")  # type: ignore
            .lstrip("\\")
        )

        if utility.is_none_or_whitespace(rocketblend_config.packages_path):
            self.report({"ERROR"}, "Rocketblend package path not found.")
            return {"CANCELLED"}

        # runtime_config_path = str(
        #     Path(rocketblend_config.packages_path) / build_reference  # type: ignore
        # )
        # runtime_config = utility.load_rocketpack_config(runtime_config_path)

        # if not runtime_config:
        #     self.report({"ERROR"}, "Runtime package configuration not found.")
        #     return {"CANCELLED"}

        bpy.context.window_manager.rkb.build = build_reference
        bpy.context.window_manager.rkb.installations_path = (
            rocketblend_config.installations_path
        )
        bpy.context.window_manager.rkb.packages_path = rocketblend_config.packages_path
        bpy.context.window_manager.rkb.config_path = os.path.dirname(
            rocketblend_config_path
        )

        rocketfile = utility.load_rocketfile_config(bpy.path.abspath("//"))
        if not rocketfile:
            self.report({"ERROR"}, "Project configuration not found.")
            return {"CANCELLED"}

        bpy.context.window_manager.rkf.build = rocketfile.build

        # if bpy.context.window_manager.rkb.build != bpy.context.window_manager.rkf.build:
        #     self.report(
        #         {"ERROR"},
        #         "This project is not compatible with the current build (RocketBlend)",
        #     )

        return {"FINISHED"}

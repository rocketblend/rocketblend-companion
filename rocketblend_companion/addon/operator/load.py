import bpy
from bpy.types import Operator
from pathlib import Path

from .. import utility

import logging

log = logging.getLogger(__name__)


class RKB_OT_load(bpy.types.Operator):
    """Loads all the configurations for the current project"""

    bl_idname = "rkb.load"
    bl_label = "Loader"

    def execute(self, context):
        log.info("Loading RocketBlend configurations...")

        rocketblend_config = utility.load_rocketblend_config(True)
        if not rocketblend_config:
            self.report({"ERROR"}, "RocketBlend configurations not found.")
            return {"CANCELLED"}

        if utility.is_none_or_whitespace(rocketblend_config.installations_path):
            self.report({"ERROR"}, "RocketBlend configurations not found.")
            return {"CANCELLED"}

        current_exec_path = Path(bpy.app.binary_path).resolve().parent.parent

        build_reference = str(current_exec_path).replace(
            rocketblend_config.installations_path, ""  # type: ignore
        )

        if utility.is_none_or_whitespace(rocketblend_config.packages_path):
            self.report({"ERROR"}, "RocketPack configurations not found.")
            return {"CANCELLED"}

        runtime_config = utility.load_rocketpack_config(
            str(Path(rocketblend_config.packages_path) / build_reference)  # type: ignore
        )

        if not runtime_config:
            self.report({"ERROR"}, "RocketPack configurations not found.")
            return {"CANCELLED"}

        bpy.context.window_manager.rkb.build = build_reference

        rocketfile = utility.load_rocketfile_config(bpy.path.abspath("//"))
        if not rocketfile:
            self.report({"ERROR"}, "RocketFile configurations not found.")
            return {"CANCELLED"}

        bpy.context.window_manager.rkf.build = rocketfile.build

        if bpy.context.window_manager.rkb.build != bpy.context.window_manager.rkf.build:
            self.report(
                {"ERROR"},
                "This project is not compatible with the current build (RocketBlend)",
            )

        return {"FINISHED"}

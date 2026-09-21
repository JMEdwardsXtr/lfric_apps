import sys

from metomi.rose.upgrade import MacroUpgrade  # noqa: F401

from .version31_32 import *


class UpgradeError(Exception):
    """Exception created when an upgrade fails."""

    def __init__(self, msg):
        self.msg = msg

    def __repr__(self):
        sys.tracebacklimit = 0
        return self.msg

    __str__ = __repr__


"""
Copy this template and complete to add your macro

class vnXX_txxx(MacroUpgrade):
    # Upgrade macro for <TICKET> by <Author>

    BEFORE_TAG = "vnX.X"
    AFTER_TAG = "vnX.X_txxx"

    def upgrade(self, config, meta_config=None):
        # Add settings
        return config, self.reports
"""

class vn32_t797(MacroUpgrade):
    # Upgrade macro for #797 by J. M. Edwards

    BEFORE_TAG = "vn3.2"
    AFTER_TAG = "vn3.2_t797"

    def upgrade(self, config, meta_config=None):

        # N.B. This upgrades to the version on the trunk of JULES, not to the
        # version that has been used in developing GC6.
        l_fix_neg_snow = (
            self.get_setting_value(
                config, ["namelist:jules_temp_fixes", "l_fix_neg_snow"], no_ignore=False
            )
        ) == ".true."
        if l_fix_neg_snow:
            self.add_setting(
                config, ["namelist:jules_temp_fixes", "i_fix_neg_snow"], "2"
            )
        else:
            self.add_setting(
                config, ["namelist:jules_temp_fixes", "i_fix_neg_snow"], "0"
            )
        self.remove_setting(config, ["namelist:jules_temp_fixes", "l_fix_neg_snow"])


        return config, self.reports

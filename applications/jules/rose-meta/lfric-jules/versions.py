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


class vn22_t619(MacroUpgrade):
    # Upgrade macro for ticket 619 by J. M. Edwards.

    BEFORE_TAG = "vn2.2"
    AFTER_TAG = "vn2.2_t619"

    def upgrade(self, config, meta_config=None):
        self.add_setting(config, ["namelist:jules_snow", "l_rhofresh_extern"], ".false.")
        self.add_setting(config, ["namelist:jules_snow", "wind_compaction_sqrt"], "0.0")
        return config, self.reports


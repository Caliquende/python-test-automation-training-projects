"""
Configuration values for the UI automation suite.

This module keeps environment-level values away from test and page object code.
"""

import os


BASE_URL = "https://www.saucedemo.com/"
DEFAULT_TIMEOUT = 10

HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
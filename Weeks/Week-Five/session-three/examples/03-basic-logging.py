"""
Example: Using Python standard logging module.
Week Five — Session Three
"""

import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logging.info("Application started successfully.")
logging.warning("Low disk space warning.")

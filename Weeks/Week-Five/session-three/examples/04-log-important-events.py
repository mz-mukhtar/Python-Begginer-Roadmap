"""
Example: Logging errors and important workflow events.
Week Five — Session Three
"""

import logging

logging.basicConfig(level=logging.ERROR)

try:
    x = 10 / 0
except ZeroDivisionError as e:
    logging.error(f"Division failed: {e}")

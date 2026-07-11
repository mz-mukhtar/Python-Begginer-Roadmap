"""
Example: Integrating layered calls.
Week Seven — Session One
"""

def ui_layer():
    print("User requests student list...")
    service_layer()

def service_layer():
    print("Service fetching records...")

ui_layer()

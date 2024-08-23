import sys
import os
import bpy
from .ui import AI_PT_Panel
from .operators import AI_OT_SubmitPrompt

# Dynamically determine the site-packages path relative to the script
venv_path = os.path.dirname(os.path.abspath(__file__))
site_packages_path = os.path.join(venv_path, 'venv', 'Lib', 'site-packages')

if site_packages_path not in sys.path:
    sys.path.append(site_packages_path)

bl_info = {
    "name": "AI Blender Add-on",
    "blender": (2, 80, 0),
    "category": "3D View",
    "version": (1, 0, 0),
    "author": "Sekou Oumar Brehima Keita",
    "description": "Add-on to prompt AI commands within Blender.",
}

# List of classes to register
classes = [AI_PT_Panel, AI_OT_SubmitPrompt]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.ai_prompt = bpy.props.StringProperty(name="AI Prompt")

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.ai_prompt

if __name__ == "__main__":
    unregister()
    register()

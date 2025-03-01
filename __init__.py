# __init__.py
bl_info = {
    "name": "Icosa Listener",
    "blender": (4, 0, 0),
    "description": "Allows Icosa Gallery to import models into Blender",
    "version": (1, 0),
    "author": "@icosa.gallery",
}

import bpy
from bpy.app.handlers import persistent
import threading
import os

# Import the server module
from .server import ModelImportServer

# Global reference to server instance
server_instance = None

@persistent
def load_handler(dummy):
    """Restart server when loading new blend files"""
    global server_instance
    if server_instance:
        server_instance.restart()

def register():
    global server_instance
    server_instance = ModelImportServer()
    server_instance.start()
    bpy.app.handlers.load_post.append(load_handler)

def unregister():
    global server_instance
    if server_instance:
        server_instance.stop()
    bpy.app.handlers.load_post.remove(load_handler)

if __name__ == "__main__":
    register()

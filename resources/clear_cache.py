# Import required packages and modules
# from __future__ import annotations
import sys as sys
import os as os
import shutil as shutil
import importlib as importlib
# from decouple import config
# import asyncio as asyncio

def clear_cache():
    # Step 1: Delete compiled Python files (.pyc and .pyo)
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith(('.pyc', '.pyo')):
                os.remove(os.path.join(root, file))

    # Step 2: Clear sys.modules cache
    for module in list(sys.modules):
        if module not in sys.builtin_module_names:
            del sys.modules[module]

    # Step 3: Invalidate caches
    importlib.invalidate_caches()

    # Step 4: Set PYTHONDONTWRITEBYTECODE environment variable
    os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

def remove_pycache():
    # Walk through all directories and subdirectories
    for root, dirs, files in os.walk('.'):
        for dir in dirs:
            # Check if the directory is __pycache__
            if dir == '__pycache__':
                # Construct the full path to the __pycache__ directory
                pycache_dir = os.path.join(root, dir)
                # Remove the __pycache__ directory and its contents
                shutil.rmtree(pycache_dir)

def clear_venv_cache(venv_path):
    # Walk through all directories and subdirectories within the venv
    for root, dirs, files in os.walk(venv_path):
        for dir in dirs:
            # Check if the directory is __pycache__
            if dir == '__pycache__':
                # Construct the full path to the __pycache__ directory
                pycache_dir = os.path.join(root, dir)
                # Remove the __pycache__ directory and its contents
                shutil.rmtree(pycache_dir)
        for file in files:
            # Check if the file is a compiled Python file (.pyc)
            if file.endswith('.pyc'):
                # Remove the compiled Python file
                os.remove(os.path.join(root, file))

if __name__ == "__main__":
    clear_cache()
    remove_pycache()
    print("Cache cleared and all __pycache__ directories removed successfully.")
    # Specify the path to your virtual environment
    venv_path = '.venv'
    clear_venv_cache(venv_path)
    print("Cache within the virtual environment cleared successfully.")

# __init__.py

# Import primary functions for external use
from .epik8s_gen import main, render_template, load_values_yaml, create_directory_tree

__all__ = [
    "main",
    "render_template",
    "load_values_yaml",
    "create_directory_tree"
]

# Optional: Define package metadata
__version__ = "0.1.0"
__author__ = "Andrea Michelotti"

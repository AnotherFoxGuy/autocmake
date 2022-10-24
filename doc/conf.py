# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
import os
import time

sys.path.insert(0, os.path.abspath("."))
import extract_rst

sys.path.insert(0, os.path.abspath(".."))
from autocmake import __version__ as _version

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Autocmake"
copyright = f'2015-{time.strftime("%Y")}, Radovan Bast, Roberto Di Remigio, Jonas Juselius, and contributors'
author = "Radovan Bast, Roberto Di Remigio, Jonas Juselius, and contributors"

# The full version, including alpha/beta/rc tags.
release = _version
# The short X.Y version.
version = ".".join(release.split(".")[0:2])

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.todo",
]
todo_include_todos = True

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

root_doc = "index"
pygments_style = "sphinx"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "classic"
html_theme_options = {"body_max_width": "none", "sidebarwidth": "16%"}
html_static_path = ["_static"]
html_sidebars = {"**": ["globaltoc.html", "sourcelink.html", "searchbox.html"]}

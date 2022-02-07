# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
from os import environ
from pathlib import Path
import sys
from typing import Any, Dict

on_rtd = environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:
    import sphinx_theme

sys.path.insert(0, str(Path('../../src')))


about: Dict[str, Any] = {}
with open(
    Path(__file__).resolve().parents[2] / 'src/design_pytterns/_about.py',
    'r',
    encoding='utf-8'
) as about_file:
    exec(about_file.read(), about)  # nosec

# -- Project information -----------------------------------------------------

project = about['__title__']
copyright = f"2020-2022, {about['__author__']}"
author = about['__author__']

# The full version, including alpha/beta/rc tags
release = about['__version__']


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}
# ---sphinx-themes-----
if not on_rtd:  # only import and set the theme if we're building docs locally
    html_theme = 'neo_rtd_theme'
    html_theme_path = [sphinx_theme.get_html_theme_path('neo_rtd_theme')]

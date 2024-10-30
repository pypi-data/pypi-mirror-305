# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Zen Mapper"
description = "Mapper without the noise"
copyright = "2023, Ethan Rooke"
author = "Ethan Rooke"
release = "0.1.5"


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "myst_parser",
    "autoapi.extension",
    "sphinx_gallery.gen_gallery",
]

templates_path = ["_templates"]
exclude_patterns = []

# -- Other documentation -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#confval-intersphinx_mapping
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("http://docs.scipy.org/doc/numpy/", None),
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_theme_options = {
    "github_user": "zen-mapper",
    "github_repo": "zen-mapper",
}
html_static_path = ["_static"]
html_sidebars = {
    "**": [
        "about.html",
        "searchfield.html",
        "navigation.html",
    ]
}

# -- Options for Api documentation --------------------------------------------
autoapi_dirs = ["../../src/zen_mapper"]
autoapi_ignore = ["**/test*.py"]

# -- Options for example gallery ----------------------------------------------
sphinx_gallery_conf = {
    "examples_dirs": "../../examples",
    "gallery_dirs": "examples",
    "filename_pattern": "/*.py",
}

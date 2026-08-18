# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'DuIvyProcedures'
copyright = '2024, Charles Hahn'
author = 'Charles Hahn'
release = '1.0.3'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx.ext.mathjax',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['../docs/static']

# -- Options for Markdown files ----------------------------------------------
# MyST parser configuration
myst_heading_anchors = 3
myst_enable_extensions = [
    'dollarmath',
    'amsmath',
    'deflist',
    'html_admonition',
    'html_image',
    'colon_fence',
    'smartquotes',
    'replacements',
]

# -- Internationalization settings -------------------------------------------
locale_dirs = ['locale/']
gettext_compact = False

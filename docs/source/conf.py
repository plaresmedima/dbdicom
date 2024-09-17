# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
project = 'dbdicom'
copyright = '2022, QIB-Sheffield'
author = 'QIB-Sheffield'
release = '1.0'

# -- Path setup --------------------------------------------------------------
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here
import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones
extensions = [
    'sphinx.ext.napoleon', # parsing of NumPy and Google style docstrings
    'sphinx.ext.autodoc', # sphinx autodocumentation generation
    'sphinx.ext.autosummary', # generates function/method/attribute summary lists
    'sphinx.ext.viewcode', # viewing source code
    'sphinx.ext.intersphinx', # generate links to the documentation of objects in external projects
    'autodocsumm',
    'myst_parser', # parser for markdown language
    'sphinx_copybutton', # copy button for code blocks
    'sphinx_design', # sphinx web design components
    'sphinx_remove_toctrees', # selectively remove toctree objects from pages
    'sphinx_gallery.gen_gallery',
]

# Settings for sphinx-gallery, see
# https://sphinx-gallery.github.io/stable/getting_started.html#create-simple-gallery
sphinx_gallery_conf = {
    # path to the example scripts relative to conf.py
    'examples_dirs': '../examples',   

    # path to where to save gallery generated output
    'gallery_dirs': 'generated/examples',  
    
    # directory where function/class granular galleries are stored
    'backreferences_dir': 'generated/backreferences',

    # Modules for which function/class level galleries are created. 
    'doc_module': ('dbdicom', ),

    # objects to exclude from implicit backreferences. The default option
    # is an empty set, i.e. exclude nothing.
    'exclude_implicit_doc': {},

    # thumbnail for examples that do not generate any plot
    'default_thumb_file': '_static/dbd.png',

    # Disabling download button of all scripts
    'download_all_examples': False,

    # Settings for use of binder
    "binder": {
        "org": "QIB-Sheffield",
        "repo": "dbdicom",
        "binderhub_url": "https://mybinder.org",
        "branch": "main",
        "dependencies": "./binder/requirements.txt",
        "use_jupyter_lab": True,
    },

}

# This way a link to other methods, classes, or modules can be made with back ticks so that you don't have to use qualifiers like :class:, :func:, :meth: and the likes
default_role = 'obj'

# Add any paths that contain templates here, relative to this directory
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path
exclude_patterns = []

# -- Extension configuration -------------------------------------------------
# Map intersphinx to pre-existing documentation from other projects used in this project
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'matplotlib': ('https://matplotlib.org/stable/', None),
    'pydicom': ('https://pydicom.github.io/pydicom/stable/', None),
    'nibabel': ('https://nipy.org/nibabel/', None),
    'pandas': ('https://pandas.pydata.org/docs/', None),
    'skimage': ('https://scikit-image.org/docs/stable/', None),
}

# generate autosummary even if no references
autosummary_generate = True 

# Tell sphinx-autodoc-typehints to generate stub parameter annotations including types, even if the parameters aren't explicitly documented.
always_document_param_types = True

# Remove auto-generated API docs from sidebars.
remove_from_toctrees = ["_autosummary/*"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# The theme to use for HTML and HTML Help pages.  See the documentation for a list of builtin themes
html_theme = 'pydata_sphinx_theme'

html_theme_options = {
    "github_url": "https://github.com/QIB-Sheffield/dbdicom",
    "collapse_navigation": True,
    }

# Add any paths that contain custom static files (such as style sheets) here, relative to this directory. They are copied after the builtin static files, so a file named "default.css" will overwrite the builtin "default.css"
html_static_path = ['_static']

# The suffix(es) of source filenames.
source_suffix = ['.rst', '.md']

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '_static/dbd.png'



# #### THIS CODE BLOCK ADDED TO FIX pandoc INSTALLATION ISSUES #####
# #### Pandoc is needed to render jupyter notebooks with nbsphinx

# # For details see:
# # https://stackoverflow.com/questions/62398231/building-docs-fails-due-to-missing-pandoc

# import os
# from inspect import getsourcefile

# # Get path to directory containing this file, conf.py.
# DOCS_DIRECTORY = os.path.dirname(os.path.abspath(getsourcefile(lambda: 0)))

# def ensure_pandoc_installed(_):
#     import pypandoc

#     # Download pandoc if necessary. If pandoc is already installed and on
#     # the PATH, the installed version will be used. Otherwise, we will
#     # download a copy of pandoc into docs/bin/ and add that to our PATH.
#     pandoc_dir = os.path.join(DOCS_DIRECTORY, "bin")
#     # Add dir containing pandoc binary to the PATH environment variable
#     if pandoc_dir not in os.environ["PATH"].split(os.pathsep):
#         os.environ["PATH"] += os.pathsep + pandoc_dir
#     pypandoc.ensure_pandoc_installed(
#         #quiet=True,
#         targetfolder=pandoc_dir,
#         delete_installer=True,
#     )

# def setup(app):
#     app.connect("builder-inited", ensure_pandoc_installed)

# #### END OF CODE BLOCK ADDED TO FIX pandoc INSTALLATION ISSUES #####
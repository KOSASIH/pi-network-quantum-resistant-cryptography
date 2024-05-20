#!/usr/bin/env python3

import os
import sys
import subprocess

# Add the parent directory to the path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

# Import the PiQuantum module
import piquantum

# Get the version number from the PiQuantum module
version = piquantum.__version__

# Get the Sphinx version
sphinx_version = subprocess.check_output(['sphinx-build', '-v'], universal_newlines=True).split()[1]

# Set the project information
project = 'PiQuantum'
copyright = 'PiQuantum Team, 2023'
author = 'PiQuantum Team'

# Set the HTML builder options
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': True,
    'display_version': True,
}
html_static_path = ['_static']

# Set theintersphinx options
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'cryptography': ('https://cryptography.io/en/latest/', None),
}

# Set the autodoc options
autodoc_member_order = 'bysource'
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'inherited-members': True,
    'special-members': True,
}

# Set the napoleon options
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True

# Set the sphinx-autobuild options
autobuild = False
if '--autobuild' in sys.argv:
    autobuild = True
    sys.argv.remove('--autobuild')

if autobuild:
    import time
    import subprocess

    def build():
        print('Building documentation...')
        subprocess.check_call(['sphinx-build', '-b', 'html', '-d', 'build/doctrees', '.', 'build/html'])
        print('Documentation built.')

    def watch():
        print('Watching for changes...')
        while True:
            time.sleep(1)
            if '--autobuild' not in sys.argv:
                break
            if os.path.exists('.buildlock'):
                continue
            build()

    build()
    watch()

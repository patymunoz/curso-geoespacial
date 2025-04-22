import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Automatización de procesos con datos geoespaciales en Python'
author = 'MCD. Patricia Muñoz'
release = '0.1'

extensions = ['myst_parser', 'nbsphinx']

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
source_suffix = {
    '.md': 'markdown',
}

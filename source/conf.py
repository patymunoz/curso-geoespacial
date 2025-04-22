import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Manejo de datos geoespaciales en Python'
author = 'MCD. Patricia Muñoz'
release = '0.1'

extensions = ['myst_parser', 'nbsphinx']

myst_enable_extensions = [
    "colon_fence"
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_book_theme'

html_theme_options = {
    "repository_url": "https://github.com/patymunoz/curso-geoespacial",
    "use_repository_button": True,
    "use_edit_page_button": False,
    "use_issues_button": False,
    "home_page_in_toc": True,
}

html_title = "Manejo de datos geoespaciales en Python"
html_logo = "_static/codigo.png"

html_static_path = ['_static']
source_suffix = {
    '.md': 'markdown',
}

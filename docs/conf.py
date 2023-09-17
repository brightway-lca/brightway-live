### path setup ####################################################################################

from glob import glob
import datetime
import os
 
###################################################################################################
### Project Information ###########################################################################
###################################################################################################

project = 'Brightway'
copyright = datetime.date.today().strftime("%Y") + ' Brightway Developers'
version: str = 'latest' # required by the version switcher

###################################################################################################
### Project Configuration #########################################################################
###################################################################################################

needs_sphinx = '7.2.6'

extensions = [
    # core extensions
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    'sphinx.ext.inheritance_diagram',
    # iPython extensions
    'IPython.sphinxext.ipython_directive',
    'IPython.sphinxext.ipython_console_highlighting',
    # Markdown support
    'myst_parser', # do not enable separately if using myst_nb, compare https://github.com/executablebooks/MyST-NB/issues/421#issuecomment-1164427544
    # responsive web component support
    'sphinx_design',
    # custom 404 page
    'notfound.extension',
    # custom favicons
    'sphinx_favicon',
    # copy button on code blocks
    "sphinx_copybutton",
    # wasm
    "jupyterlite_sphinx",
]

root_doc = 'index'
html_static_path = ['_static']
templates_path = ['_templates']
exclude_patterns = ['_build']
html_theme = "pydata_sphinx_theme"

suppress_warnings = [
    "myst.header" # suppress warnings of the kind "WARNING: Non-consecutive header level increase; H1 to H3"
]

####################################################################################################
### Theme html Configuration #######################################################################
####################################################################################################

html_show_sphinx = False
html_show_copyright = True

html_css_files = [
    "css/custom.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css" # for https://fontawesome.com/ icons
]

html_sidebars = {
    "**": [
        "search-field.html",
        "sidebar-nav-bs.html",
    ],
}

footcent = str('test')

html_theme_options = {
    "announcement": "<p>⚠️ Brightway Live is in Public Beta ⚠️</p>",
    # page elements
    "navbar_start": ["navbar-logo"],
    "navbar_end": ["navbar-icon-links.html"],
    "footer_start": ["copyright"],
    "footer_center": ["footer_center"],
    "footer_end": ["footer_end"],
    "secondary_sidebar_items": ["page-toc"],
    "header_links_before_dropdown": 7,
    # page elements content
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/brightway-lca",
            "icon": "fab fa-brands fa-github",
        },
        {
            "name": "Matrix",
            "url": "https://app.element.io/#/room/#brightway/community:matrix.org",
            "icon": "fab fa-regular fa-comments",
        }
    ],
    # various settings
    "collapse_navigation": True,
    "show_prev_next": False,
    "use_edit_page_button": True,
    "navigation_with_keys": True,
    "logo": {
        "text": "Brightway Live",
        "image_light": "BW_all_black_transparent_landscape.svg",
        "image_dark": "BW_all_white_transparent_landscape.svg"
    },
}

# required by html_theme_options: "use_edit_page_button"
html_context = {
    "github_user": "brightway-lca",
    "github_repo": "brightway-documentation",
    "github_version": "main",
    "doc_path": "source",
}

####################################################################################################
### Extension Configuration ########################################################################
####################################################################################################

# linkcheck Configuration ###############################################
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-the-linkcheck-builder

linkcheck_retries = 1
linkcheck_workers = 20
linkcheck_exclude_documents = []

# notfound Configuration ################################################
# https://sphinx-notfound-page.readthedocs.io

notfound_context = {
    'title': 'Page Not Found',
    'body': '''                                                                                                                                           
        <h1>🍂 Page Not Found (404)</h1>
        <p>
        Oops! It looks like you've stumbled upon a page that's been recycled into the digital abyss.
        But don't worry, we're all about sustainability here.
        Why not take a moment to reduce, reuse, and recycle your clicks by heading back to the main page?
        And remember, every little bit counts in the grand scheme of things.
        </p>
    ''',
}

# myst_parser Configuration ############################################
# https://myst-parser.readthedocs.io/en/latest/configuration.html

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown'
}

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_image",
    "linkify",
]

# sphinx-favicon configuration #########################################
# https://github.com/tcmetzger/sphinx-favicon

favicons = [
    {
        "rel": "icon",
        "sizes": "100x100",
        "href": "logo/BW_favicon_100x100.png",
    },
    {
        "rel": "apple-touch-icon",
        "sizes": "500x500",
        "href": "logo/BW_favicon_500x500.png"
    },
]

try:
    import tomllib
except ImportError:
    import tomli as tomllib

from jupyterlite_pyodide_kernel import __version__

from pathlib import Path


project = "Brightway Live"
copyright = '© 2023 Brightway Developers'
exclude_patterns = []

extensions = [
    "myst_parser",
    "sphinx_copybutton",
]

# myst
autosectionlabel_prefix_document = True
myst_heading_anchors = 3
suppress_warnings = ["autosectionlabel.*"]
master_doc = "index"
source_suffix = ".md"

# theme
html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "github_url": P["urls"]["Homepage"],
    "use_edit_page_button": False,
    "pygment_light_style": "github-light",
    "pygment_dark_style": "github-dark"
}

# rely on the order of these to patch json, labextensions correctly
html_static_path = [
    # as-built assets for testing "hot" downstreams against a PR without rebuilding
    "../dist",
    # as-built application, extensions, contents, and patched jupyter-lite.json
    "../build/docs-app",
]
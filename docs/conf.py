project   = "TwinCat Dynamic Collections"
author    = "FisoThemes"
copyright = "2026, FisoThemes"
version   = "1.0.9"
release   = "1.0.9"

extensions = ["sphinx.ext.autosectionlabel"]
autosectionlabel_prefix_document = True
suppress_warnings = ["autosectionlabel.*"]

html_theme = "sphinx_rtd_theme"
html_title = f"{project} v{release}"
html_theme_options = {
    "navigation_depth": -1,
}
html_show_sourcelink = False
html_copy_source = False
highlight_language = "none"

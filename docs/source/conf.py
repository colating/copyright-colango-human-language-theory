# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Colating General Human Language'
copyright = '2021, David'
author = 'David'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
#    'python': ('https://docs.python.org/3/', None),
#    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
# 在此添加包含自定义静态文件（如样式表）的任何路径，
# 相对于当前目录。它们在内置静态文件之后被复制，
# 因此，一个名为“default.css”的文件将覆盖内置的“default.css”。

## https://docs.readthedocs.io/en/stable/guides/adding-custom-css.html?highlight=font#adding-custom-css-or-javascript-to-sphinx-documentation
## font ng doing....
#html_style = 'css/clgo-theme.css'
html_css_files = ['css/colango_custom.css']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'





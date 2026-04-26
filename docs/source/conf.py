# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Colango Human Language Theory'
copyleft = '2026, David'
author = 'David'

release = '0.1'
version = '0.1.0'

####
# The copyright holder and year(s)
copyright = '>2K~2026, Colango'

# -- General configuration

extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    "myst_parser",
    'sphinxcontrib.mermaid',
    
]

##"myst_parser",


# 指定支持的源文件后缀
#source_suffix = {
#    '.rst': 'restructuredtext',
#    '.md': 'markdown',
#    '.ipynb': 'jupyter_notebook',
#}
source_suffix = {
    '.md': 'markdown',
    '.rst': 'restructuredtext',
}


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
html_css_files = ['css/clgo_sphinx_rtd_theme.css']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
#html_theme = "pydata_sphinx_theme"
#html_theme = "sphinx_book_theme"
####
# 在 conf.py 中添加或修改。关闭显示默认的“View page source ” 显示
html_show_sourcelink = False

#html_theme_options = {
#### https://sphinx-book-theme.readthedocs.io/en/stable/tutorials/get-started.html
#    ...
#    "repository_url": "https://github.com/{your-docs-url}",
#    "use_repository_button": True,
#    ...
    ## pydate
##    "use_download_button": False,
#}


html_title = "Colating Language"

# -- Options for EPUB output
epub_show_urls = 'footnote'

####
todo_include_todos = True
todo_emit_warnings = True
## todo_link_only True: .. todolist:: 生成的列表仅包含链接，不包含文件路径和行号。

myst_enable_extensions = [
    # 用于解析美元$和$$封装的数学和LaTeX 数学公式解析
    "dollarmath","amsmath",
    # 定义列表
    "deflist",
    # 冒号的代码围栏
    "colon_fence",
    # HTML 警告
    "html_admonition",
    # HTML 图像
    "html_image",
    # 智能引号与替换件
    "smartquotes","replacements",
    # 链接
    "linkify",
    # 替换
    "substitution",
    # 任务列表
    "tasklist"
]


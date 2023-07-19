project = 'PMEAL Homepage'
copyright = '2021, PMEAL Team'
author = 'PMEAL Team'

extensions = [
    "ablog",
    "sphinx.ext.intersphinx",
    "sphinx_panels",
    "myst_nb",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'pydata_sphinx_theme'
html_logo = '_static/logo.png'
html_static_path = ['_static']
html_css_files = [
    'css/custom.css',
]
html_theme_options = {
    "github_url": "https://github.com/PMEAL",
    "show_prev_next": False,
    "collapse_navigation": False,
    "navbar_align": "left",
}

blog_path = "blog"
blog_baseurl = "https://www.pmeal.com"
blog_title = "PMEAL Homepage"
fontawesome_included = True
blog_post_pattern = "posts/*/*"
html_sidebars = {
    "blog": ['ablog/recentposts.html', 'ablog/archives.html', ],
}

jupyter_execute_notebooks = "off"

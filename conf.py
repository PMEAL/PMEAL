project = 'PMEAL'
copyright = '2021, PMEAL Team'
author = 'PMEAL Team'

extensions = [
    "ablog",
    "sphinx.ext.intersphinx",
    "sphinx_panels",
#     "myst_parser",
    "myst_nb",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'pydata_sphinx_theme'

html_static_path = ['_static']

blog_path = "blog"
fontawesome_included = True
blog_post_pattern = "posts/*/*"
html_sidebars = {
   '**': ['recentposts.html']
}

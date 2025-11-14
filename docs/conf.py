project = 'Trend Micro Login'
author = 'Trend Micro Login'
release = '1.0'

# Sphinx Extensions
extensions = [
    'sphinx_sitemap',
]

# Templates & Patterns
templates_path = ['_templates']
exclude_patterns = []

# ReadTheDocs Friendly Theme (Highly Recommended)
html_theme = 'sphinx_rtd_theme'

# Static Files
html_static_path = ['_static']

# Optional JS script
html_js_files = [
    'chatbot.js',
]

# Favicon
html_favicon = '_static/favicon.png'

# Important for Sitemap
html_baseurl = 'https://microtrendinfoguide.readthedocs.io/en/latest/'

# Bing Verification
html_context = {
    'bing_verification_code': '739245F5D54BCBF40AC056DC0CBF5710'
}

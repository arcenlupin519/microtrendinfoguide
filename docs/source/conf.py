.. code-block:: python


# conf.py — minimal configuration for ReadTheDocs
import os
import sys
sys.path.insert(0, os.path.abspath('.'))


project = 'Total Defense Activation Guide'
author = 'Documentation Team'
extensions = []
templates_path = ['_templates']
exclude_patterns = []
html_theme = 'sphinx_rtd_theme'

# -*- coding: utf-8 -*-
import os
import re
import sys

import sphinx_rtd_theme

sys.path.insert(0, os.path.abspath('../'))


def get_version():
    """
    Read the version from the package __init__.py file
    :return:
    """
    VERSIONFILE = os.path.join('..', 'django_icons', '__init__.py')
    initfile_lines = open(VERSIONFILE, 'rt').readlines()
    VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
    for line in initfile_lines:
        mo = re.search(VSRE, line, re.M)
        if mo:
            return mo.group(1)
    raise RuntimeError('Unable to find version string in %s.' % (VERSIONFILE,))


project = 'django-icons'
version = get_version()
release = version

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.ifconfig',
]

source_suffix = '.rst'

master_doc = 'index'

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']

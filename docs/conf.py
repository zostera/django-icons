import os
import sys
from pkg_resources import get_distribution

project = "django-icons"

SRC_ROOT = os.path.join(os.path.dirname(__file__), "..", "src")
sys.path.append(SRC_ROOT)

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tests.app.settings')

# import django
# django.setup()
#
extensions = ["sphinx.ext.autodoc", "sphinx.ext.viewcode"]

# The full version, including alpha/beta/rc tags, in x.y.z.misc format
release = get_distribution(project).version
# The short X.Y version.
version = ".".join(release.split(".")[:2])

pygments_style = "sphinx"
htmlhelp_basename = f"{project}-doc"

on_rtd = os.environ.get("READTHEDOCS", None) == "True"

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme

    html_theme = "sphinx_rtd_theme"
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

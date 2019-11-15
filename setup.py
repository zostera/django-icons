#!/usr/local/bin/python


import os
import re

from setuptools import setup, setuptools

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# Read version from app
with open("django_icons/__init__.py", "rb") as f:
    VERSION = str(re.search('__version__ = "(.+?)"', f.read().decode("utf-8")).group(1))

with open(os.path.join(os.path.dirname(__file__), "README.rst")) as readme_file:
    readme = readme_file.read()

with open(os.path.join(os.path.dirname(__file__), "CHANGELOG.rst")) as changelog_file:
    changelog = changelog_file.read().replace(".. :changelog:", "")

setup(
    name="django-icons",
    version=VERSION,
    description="""Icons for Django""",
    long_description=readme + "\n\n" + changelog,
    long_description_content_type="text/x-rst",
    author="Dylan Verheul",
    author_email="dylan@zostera.nl",
    url="https://github.com/zostera/django-icons",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=["Django >= 1.8"],
    license="BSD-3-Clause",
    zip_safe=False,
    keywords="django-icons",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Environment :: Web Environment",
        "Framework :: Django",
    ],
)

#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os
import re
import sys

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

if sys.argv[-1] == "publish":
    os.system("cd docs && make html")
    os.system("python setup.py sdist")
    os.system("twine upload dist/django-icons-{}.tar.gz".format(VERSION))
    message = "\nreleased [{version}](https://pypi.python.org/pypi/django-icons/{version})"
    print(message.format(version=VERSION))
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (VERSION, VERSION))
    print("  git push --tags")
    sys.exit()

if sys.argv[-1] == "test":
    os.system("pip install -U -r requirements.txt")
    os.system("pip install -U coverage")
    os.system("coverage run ./manage.py test && coverage report --include=./*")
    sys.exit()

setup(
    name="django-icons",
    version=VERSION,
    description="""Icons for Django""",
    long_description=readme + "\n\n" + changelog,
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
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Environment :: Web Environment",
        "Framework :: Django",
    ],
)

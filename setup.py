#!/usr/local/bin/python


import os

from setuptools import setup, setuptools

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

PROJECT_ROOT = os.path.dirname(__file__)

with open(os.path.join(PROJECT_ROOT, "README.rst")) as readme_file:
    readme = readme_file.read()

with open(os.path.join(PROJECT_ROOT, "CHANGELOG.rst")) as changelog_file:
    changelog = changelog_file.read().replace(".. :changelog:", "")

setup(
    name="django-icons",
    description="""Icons for Django""",
    long_description=readme + "\n\n" + changelog,
    long_description_content_type="text/x-rst",
    author="Dylan Verheul",
    author_email="dylan@zostera.nl",
    url="https://github.com/zostera/django-icons",
    license="BSD-3-Clause",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    keywords="django-icons",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
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

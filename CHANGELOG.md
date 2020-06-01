# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2020-06-01
### Changed
- Use [poetry](https://python-poetry.org) for managing dependencies and packaging.
- Update tox and Travis config to work with poetry.
- Rewrite CHANGELOG in MarkDown.

### Removed
- Drop support for Python 3.5 and Django 2.1.

## [1.1.2] - 2020-03-21
### Changed
- Fix bug that could change icon settings in run-time.

## [1.1.1] - 2019-12-13
### Changed
- Update Makefile, tox and Travis.

## [1.1.0] - 2019-12-05
### Changed
- Mark Development Status as Stable in setup.py.
- Fix several issues in Makefile.
- Remove test and publish tasks from setup.py.
- Improve reformat and lint tasks.
- Use `requirements.scm`.

## [1.0.0] - 2019-11-15
### Added
- Add support for Django 3.
- Add support for Python 3.8.
- Add test for custom ``ImageRenderer``.
- Add Makefile for common tasks.

### Removed
- Drop support for Python < 3.5.
- Drop support for Django < 2.2.

## [0.2.1] - 2018-07-01
### Changed
- Bug fixes and improvements to ``ImageRenderer`` (@mbourqui).

## [0.2.0] - 2018-06-30
### Changed
- Add icons from images, contribution by @mbourqui.
- Adopt black code style (https://github.com/ambv/black).

## [0.1.0] - 2018-01-11
### Added
- Add ``MaterialRenderer`` for [Material icons](http://google.github.io/material-design-icons/).

### Changed
- Set default branch to master.
- Make ``icon`` function available as import from django_icons (fixes).

## [0.0.5] - 2017-12-21
### Changed
- Fix typo's.
- Adjust tox matrix to currently supported Django versions.
- Fixed names of tests.
- Add tests for ``BaseRenderer``.

## [0.0.4] - 2017-06-22
### Changed
- Autogenerate docs for ``icon`` template tag.
- Fix typo in README.

## [0.0.3] - 2017-06-22
### Changed
- Bug fixes.
- More tests.
- More documentation.

## [0.0.2] - 2017-06-19
### Added
- Demo of custom SVG renderer included.
- FontAwesome and Bootstrap3 renderers included.
- New structure for settings dict.
- First documentation, linked to ReadTheDocs.
- First tests.
- Introducing the ``icon`` template tag.

### Changed
- Updated docs and tests.

## [0.0.1] - 2017-06-15
### Added
- First publication on GitHub and PyPI.
- Non-functional, just names and tests.

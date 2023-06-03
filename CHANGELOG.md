# Changelog

## 23.3 (2023-06-03)

- Switch to Hatch for builds and environments (#403).
- Improve and fix CI on GitHub Actions (#403).
- Reinstate coveralls (#403).
- Update Sphinx and switch to Furo theme (#403).

## 23.2 (2023-04-28)

- Add changelog to documentation (#358).
- Fix documentation (#355).
- Use production version of Django in tox (#357).
- Fix README.md (#373).
- Update packaging, reduce dependencies (#356, #368, #374).
- Drop support for Django 4.0 (#374).
- Fix example app (#377).
- Update example app (#379).
- Add support for nested icons and content in icon definitions (#378).
- Update documentation and examples (#381).

## 23.1 (2023-04-02)

- Update requirements, support Django 4.2, remove coveralls (#352).

## 22.1 (2022-08-08)

- Drop support for Django 2.2 (EOL) (#240).
- Add support for Django 4.1 (#240).

## 21.3 (2021-12-27)

- Fix documentation issues that snuck into 21.2.

## 21.2 (2021-12-27)

- Deprecate `icon` because of name collisions, use `render_icon` (#150).
- Fix CI (#148).
- Drop support for Django 3.1 (EOL) (#148).
- Drop support for Python 3.6 (EOL) (#148).
- Switch to stable Django 4.0 (#148).

## 21.1 (2021-11-03)

- Switch to a CalVer YY.MINOR versioning scheme. MINOR is the number of the release in the given year. This is the first release in 2021 using this scheme, so its version is 21.1. The next version this year will be 21.2. The first version in 2022 will be 22.1.
- Add support for Django 4 and Python 3.10 (#193).
## 4.0.0 (2021-05-20)

- Set `IconRenderer` as default renderer (#58).
- Defer evaluation of strings (#53).
- Stop using `mark_safe` (#57).
- Merge `extra-classes` (#55).
- Fix example app (#49).
- Rename `FontAwesomeRenderer` to `FontAwesome4Renderer` (#48).
- Fix PyPI description.
- Fix PyPI classifiers.

## 3.0.0 (2021-04-09)

- Add Dependabot.
- Revert to setuptools for packaging.
- Drop support for Django 3.0, extended support stopped on 2021-04-01).
- Add support for Django 3.2.

## 2.2.1 (2020-11-07)

- Update dependencies.
- Reformat CHANGELOG.
- Add docs and tests to sdist.
- Use GitHub Actions for CI.
- Use production version of Django 3.1 in tox matrix.

## 2.2.0 (2020-10-12)

- Add support for Python 3.9.
- Use build system poetry-core instead of poetry.
- Accept importlib-metadata 2.x.x.
- Update test settings to prevent Django 3.1 warning.
- Replace `m2r` with `m2r2` to support Sphinx3.

## 2.1.1 (2020-07-14)

- Remove dependency on sphinx_rtd_theme (fixes #21).

## 2.1.0 (2020-07-02)

- Add Django 3.1 to test matrix.
- Fix readthedocs configuration.
- Update tox configuration.
- Use Markdown for README.
- Update Makefile, tox.ini and README to support renaming `master` branch to `main`.
- Rename branch `master` to `main`.

## 2.0.0 (2020-06-01)

- Use [poetry](https://python-poetry.org) for managing dependencies and packaging.
- Update tox and Travis config to work with poetry.
- Rewrite CHANGELOG in Markdown.
- Drop support for Python 3.5 and Django 2.1.

## 1.1.2 (2020-03-21)

- Fix bug that could change icon settings in run-time.

## 1.1.1 (2019-12-13)

- Update Makefile, tox and Travis.

## 1.1.0 (2019-12-05)

- Mark Development Status as Stable in setup.py.
- Fix several issues in Makefile.
- Remove test and publish tasks from setup.py.
- Improve reformat and lint tasks.
- Use `requirements.scm`.

## 1.0.0 (2019-11-15)

- Add support for Django 3.
- Add support for Python 3.8.
- Add test for custom ``ImageRenderer``.
- Add Makefile for common tasks.
- Drop support for Python < 3.5.
- Drop support for Django < 2.2.

## 0.2.1 (2018-07-01)

- Bug fixes and improvements to ``ImageRenderer`` (@mbourqui).

## 0.2.0 (2018-06-30)

- Add icons from images, contribution by @mbourqui.
- Adopt black code style (https://github.com/ambv/black).

## 0.1.0 (2018-01-11)

- Add ``MaterialRenderer`` for [Material icons](http://google.github.io/material-design-icons/).
- Set default branch to `master`.
- Make ``icon`` function available as import from django_icons (fixes).

## 0.0.5 (2017-12-21)

- Fix typo's.
- Adjust tox matrix to currently supported Django versions.
- Fixed names of tests.
- Add tests for ``BaseRenderer``.

## 0.0.4 (2017-06-22)

- Autogenerate docs for ``icon`` template tag.
- Fix typo in README.

## 0.0.3 (2017-06-22)

- Bug fixes.
- More tests.
- More documentation.

## 0.0.2 (2017-06-19)

- Demo of custom SVG renderer included.
- FontAwesome 4 and Bootstrap3 renderers included.
- New structure for settings dict.
- First documentation, linked to ReadTheDocs.
- First tests.
- Introducing the ``icon`` template tag.
- Updated docs and tests.

## 0.0.1 (2017-06-15)

- First publication on GitHub and PyPI.
- Non-functional, just names and tests.

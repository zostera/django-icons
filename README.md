# django-icons

Icons for Django

[![image](https://travis-ci.org/zostera/django-icons.svg?branch=main)](https://travis-ci.org/zostera/django-icons)
[![image](https://coveralls.io/repos/github/zostera/django-icons/badge.svg?branch=main)](https://coveralls.io/github/zostera/django-icons?branch=main)
[![Latest PyPI version](https://img.shields.io/pypi/v/django-icons.svg)](https://pypi.python.org/pypi/django-icons)
[![Any color you like](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Why should I use this?

- Define your icons in your settings, with defaults for name, title and other attributes.
- Generate icons using template tags.
- Supports Font Awesome, Material, Bootstrap 3 and images out of the box.
- Add other (custom) icon sets by subclassing a renderer.

## How do I use this?

Define an icon in your `settings.py`, for example like this:

```python
DJANGO_ICONS = {
    "ICONS": {
        "edit": {"name": "far fa-pencil"},
    },
}
```
The basic usage in a Django template:

```djangotemplate
{% load icons %}
{% icon 'edit' %}
```

This will generate the FontAwesome 5 pencil icon in regular style:

```html
<i class="far fa-pencil"></i>
```

Add extra classes and attributes to your predefined icon like this:

```djangotemplate
{% load icons %}
{% icon 'edit' extra_classes='fa-fw my-own-icon' title='Update' %}
```

This will generate:

```html
<i class="far fa-pencil fa-fw my-own-icon" title="Update"></i>
```

## Requirements

This package requires a Python 3.6 or newer and Django 2.2 or newer.

The combination must be supported by the Django Project. See "Supported Versions" on <https://www.djangoproject.com/download/>.

## Local installation

`django-icons` adopts [Poetry](https://python-poetry.org) to manage its dependencies. This is the recommended way to do a local installation for development or to run the demo.

Assuming Python>=3.6 is available on your system, the development dependencies are installed with Poetry as follows:

```shell script
$ git clone git://github.com/zostera/django-icons.git
$ cd colour
$ poetry install
```

### Running the demo

You can run the small demo app that is part of the test suite:

```shell script
poetry run python manage.py runserver
```

### Running the tests

The test suite requires [tox](https://tox.readthedocs.io/) to be installed. Run the complete test suite like this:

```shell script
tox
```

Test for the current (virtual) environment can be run with the Django `manage.py` command. If you need to do this, you will need to have an understanding of Python virtual environments. Explaining those is beyong the scope of this README.

```shell script
python manage.py test
```

## Origin

Our plans at Zostera for an icon tool originate in <https://github.com/dyve/django-bootstrap3>. We isolated this into a Font Awesome tool in <https://github.com/zostera/django-fa>. When using our own product, we felt that the icon tool provided little improvement over plain HTML. Also, Font Awesome's icon names did not match the the intended function of the icon.

This is how we came to think of a library that:

- Took a limited number of arguments
- Converted those arguments into an icon
- Was able to support multiple icon libraries
- And could easily be extended by users

This is how we came to write and use `django-icons`.

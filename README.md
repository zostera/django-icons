# django-icons

[![CI](https://github.com/zostera/django-icons/workflows/CI/badge.svg?branch=main)](https://github.com/zostera/django-icons/actions?workflow=CI)
[![Coverage Status](https://coveralls.io/repos/github/zostera/django-icons/badge.svg?branch=main)](https://coveralls.io/github/zostera/django-icons?branch=main)
[![Latest PyPI version](https://img.shields.io/pypi/v/django-icons.svg)](https://pypi.python.org/pypi/django-icons)
[![Any color you like](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

### Icons for Django

- Define your icons in your settings, with defaults for name, title and other attributes.
- Generate icons using template tags.
- Supports Font Awesome, Material, Bootstrap 3 and images.
- Add other libraries and custom icon sets by subclassing IconRenderer.
  
### More information

- [PyPI (django-icons)](https://pypi.python.org/pypi/django-icons)
- [Documentation](https://django-icons.readthedocs.io/en/latest/)
- [Bug tracker](http://github.com/zostera/django-icons/issues)

## Installation


Install using pip.

```shell
pip install django-icons
```

Define an icon in your `settings.py`.

```python
DJANGO_ICONS = {
    "ICONS": {
        "edit": {"name": "far fa-pencil"},
    },
}
```

Render an icon in a Django template.

```djangotemplate
{% load icons %}
{% icon 'edit' %}
```

This will generate the FontAwesome 5 pencil icon in regular style.

```html
<i class="far fa-pencil"></i>
```

Add extra classes and attributes to your predefined icon.

```djangotemplate
{% load icons %}
{% icon 'edit' extra_classes='fa-fw my-own-icon' title='Update' %}
```

These will be added to the HTML output.

```html
<i class="far fa-pencil fa-fw my-own-icon" title="Update"></i>
```

## Requirements

This package requires a combination of Python and Django that is currently supported.

See "Supported Versions" on <https://www.djangoproject.com/download/>.

## Local installation

**This section assumes you know about local Python versions and virtual environments.**

To clone the repository and install the requirements for local development:

```shell
$ git clone git://github.com/zostera/django-icons.git
$ cd django-icons
$ pip install -U pip -r requirements-dev.txt
```

### Running the demo

You can run the example app:

```shell
cd example && run python manage.py runserver
```

### Running the tests

The test suite requires [tox](https://tox.readthedocs.io/) to be installed. Run the complete test suite like this:

```shell
tox
```

Test for the current environment can be run with the Django `manage.py` command.

```shell
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

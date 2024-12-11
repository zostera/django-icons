# django-icons

[![Tests](https://github.com/zostera/django-icons/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/zostera/django-icons/actions?query=workflow%3Atest+branch%3Amain)
[![Coverage Status](https://coveralls.io/repos/github/zostera/django-icons/badge.svg?branch=main)](https://coveralls.io/github/zostera/django-icons?branch=main)
[![Latest PyPI version](https://img.shields.io/pypi/v/django-icons.svg)](https://pypi.python.org/pypi/django-icons)

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

In your `settings.py`, add `django_icons` to `INSTALLED_APPS` and define an icon.

```python

INSTALLED_APPS = (
    # ...
    "django_icons",
    # ...
)

DJANGO_ICONS = {
    "ICONS": {
        "edit": {"name": "fa-solid fa-pencil"},
    },
}
```

Render an icon in a Django template.

```djangotemplate
{% load icons %}

<!-- Include your icon library. This example uses Font Awesome 6 through cdnjs.  -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

{% icon 'edit' %}
```

This will generate the FontAwesome 6 pencil icon in regular style.

```html
<i class="fa-solid fa-pencil"></i>
```

Add extra classes and attributes to your predefined icon.

```djangotemplate
{% load icons %}
{% icon 'edit' extra_classes='fa-2xs my-extra-class' title='Update' %}
```

These will be added to the HTML output.

```html
<i class="fa-solid fa-pencil fa-2xs my-extra-class" title="Update"></i>
```

## Requirements

This package requires a combination of Python and Django that is currently supported.

See "Supported Versions" on <https://www.djangoproject.com/download/>.

## Local installation

### Local installation

This package uses [uv](https://github.com/astral-sh/uv) and [just](https://github.com/casey/just).

To clone the repository and install the requirements for local development:

```console
git clone git://github.com/zostera/django-icons.git
cd django-icons
just bootstrap
```

### Running the demo

You can run the example app:

```shell
just example
```

### Running the tests

The test suite requires [tox](https://tox.readthedocs.io/) to be installed. Run the complete test suite like this:

```shell
tox
```

Test for the current environment can be run with the Django `manage.py` command.

```shell
just test
```

## Origin

Our plans at Zostera for an icon tool originate in <https://github.com/dyve/django-bootstrap3>. We isolated this into a Font Awesome tool in <https://github.com/zostera/django-fa>. When using our own product, we felt that the icon tool provided little improvement over plain HTML. Also, Font Awesome's icon names did not match the intended function of the icon.

This is how we came to think of a library that:

- Took a limited number of arguments
- Converted those arguments into an icon
- Was able to support multiple icon libraries
- Could bind an icon definition to a preset name for easy reuse
- Could easily be extended by users

This is how we came to write and use `django-icons`.

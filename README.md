# django-icons

[![CI](https://github.com/zostera/django-icons/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/zostera/django-icons/actions/workflows/ci.yml)
[![Coverage Status](https://coveralls.io/repos/github/zostera/django-icons/badge.svg?branch=main)](https://coveralls.io/github/zostera/django-icons?branch=main)
[![Latest PyPI version](https://img.shields.io/pypi/v/django-icons.svg)](https://pypi.python.org/pypi/django-icons)

Icons for Django.

## Goal

The goal of this project is to provide a single, simple template tag for rendering icons from any icon library in Django templates.

- Define your icons in your settings, with defaults for name, title and other attributes.
- Generate icons using template tags.
- Supports Font Awesome, Material, Bootstrap 3 and images.
- Add other libraries and custom icon sets by subclassing `IconRenderer`.

## Status

Ready for production. Issues and pull requests welcome, see [CONTRIBUTING.md](CONTRIBUTING.md).

## Requirements

This package requires a combination of Python and Django that is currently supported.

See "Supported Versions" on https://www.djangoproject.com/download/.

This package uses [uv](https://github.com/astral-sh/uv) and [just](https://github.com/casey/just) for local development.

## Documentation

The full documentation is at https://django-icons.readthedocs.io/en/latest/

## Installation

1. Install using pip:

    ```console
    pip install django-icons
    ```

2. Add to `INSTALLED_APPS` in your `settings.py`:

   ```python
   INSTALLED_APPS = (
       # ...
       "django_icons",
       # ...
   )
   ```

3. Define an icon:

   ```python
   DJANGO_ICONS = {
       "ICONS": {
           "edit": {"name": "fa-solid fa-pencil"},
       },
   }
   ```

4. In your templates, load the `icons` library and use the `{% icon %}` tag. See example below.

## Example template

```djangotemplate
{% load icons %}

<!-- Include your icon library. This example uses Font Awesome 6 through cdnjs. -->
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

## Example app

An example app is provided in the folder `example`. You can run the example app with this command:

```console
just example
```

## Bugs and suggestions

If you have found a bug or if you have a request for additional functionality, please use the issue tracker on GitHub.

https://github.com/zostera/django-icons/issues

## License

You can use this under BSD-3-Clause. See [LICENSE](LICENSE) file for details.

## Author

Developed and maintained by [Zostera](https://zostera.nl).

Original author: [Dylan Verheul](https://github.com/dyve).

Thanks to everybody that has contributed pull requests, ideas, issues, comments and kind words.

Please see [AUTHORS](AUTHORS) for a list of contributors.

## Origin

Our plans at Zostera for an icon tool originate in <https://github.com/dyve/django-bootstrap3>. We isolated this into a Font Awesome tool in <https://github.com/zostera/django-fa>. When using our own product, we felt that the icon tool provided little improvement over plain HTML. Also, Font Awesome's icon names did not match the intended function of the icon.

This is how we came to think of a library that:

- Took a limited number of arguments
- Converted those arguments into an icon
- Was able to support multiple icon libraries
- Could bind an icon definition to a preset name for easy reuse
- Could easily be extended by users

This is how we came to write and use `django-icons`.

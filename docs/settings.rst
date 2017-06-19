Settings
========

In your Django `settings.py` file, make a dictionary for `DJANGO_ICONS` like this:

.. code:: Python

    # Settings for django-icons
    DJANGO_ICONS = {

        'DEFAULTS': {
            'renderer': 'fontawesome',
        },

        'RENDERERS': {
            'fontawesome': 'FontAwesomeRenderer',
            'bootstrap3': 'Bootstrap3Renderer',
        },

        'ICONS': {

            'delete': 'trash',
            'edit': {
                'name': 'pencil',
                'title': 'Edit',
            },
            'feather': {
                'renderer': 'tests.app.renderers.CustomSvgRenderer',
            },
            'paperplane': {
                'renderer': 'tests.app.renderers.CustomSvgRenderer',
            }
        },

    }

The `DJANGO_ICONS` dictionary has 3 sections, all of which are optional.


DEFAULTS
--------

The `DEFAULTS` section is for settings default values for all icons.
All values can be overwritten on renderer and icon level.

.. code:: Python

    # Settings for django-icons
    DJANGO_ICONS = {

        'DEFAULTS': {
            'renderer': 'fontawesome',
        },

        ...

    }

`renderer`
  The default renderer to use for icons.
  This can be a path to a class or a name from the `RENDERERS` dict.


RENDERERS
---------

A mapping of renderer names to paths to Renderer classses.


ICONS
-----

A mapping of icon names to `icon` kwargs dict. If a single string is specified instead of a dict,
this is assumed to be the `name` parameter for the icon.


Settings
========

In your Django ``settings.py`` file, make a dictionary for ``DJANGO_ICONS``.

.. code:: Python

    # Settings for django-icons
    DJANGO_ICONS = {

        "DEFAULTS": {
            "renderer": "icon",
        },

        "RENDERERS": {
            "custom-svg": "tests.app.renderers.CustomSvgRenderer",
        },

        "ICONS": {

            "delete": "trash",
            "edit": {
                "name": "pencil",
                "title": "Edit",
            },
            "feather": {
                "renderer": "tests.app.renderers.CustomSvgRenderer",
            },
            "paperplane": {
                "renderer": "custom-svg",
            }
        },

    }

The ``DJANGO_ICONS`` dictionary has 3 sections, all of which are optional.

DEFAULTS
--------

The ``DEFAULTS`` section is for settings default values for all icons.
All values can be overwritten on renderer and icon level.

.. code:: Python

    # Settings for django-icons
    DJANGO_ICONS = {

        "DEFAULTS": {
            "renderer": "fontawesome4",
        },

        ...

    }

``renderer``
  The default renderer to use for icons.
  This can be a path to a class or a name from the ``RENDERERS`` dict.


RENDERERS
---------

A mapping of renderer names to paths to Renderer classes.


ICONS
-----

A mapping of icon names to ``icon`` kwargs dict. If a single string is specified instead of a dict,
this is assumed to be the ``name`` parameter for the icon.

The ``content`` parameter can specify content for the icon. If the content is a ``dict``, it will
be considered a nested icon definition. If the content is a ``list``, it will be considered content
that should be concatenated. This can be used to create stacked icons.

.. code:: Python

    # Settings for django-icons
    DJANGO_ICONS = {

        "ICONS": {
            "no-pictures-please": {
                "name": "fa-stack",
                "tag": "span",
                "extra_classes": "fa-2x",
                "content": [
                    {"name": "fa-solid fa-camera fa-stack-1x"},
                    {"name": "fa-solid fa-ban fa-stack-2x", "attrs": {"style": "color:Tomato"}},
                ],
            },
        },
    }

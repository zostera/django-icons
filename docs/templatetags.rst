=========================
Template Tags and Filters
=========================


.. note::

 To use these template tags, you should have already loaded the ``icons`` template tag library,
 and made sure that the necessary media for the icons is available to your template (e.g.
 the FontAwesome CSS).
 Read the :doc:`installation` and :doc:`quickstart` sections on how to accomplish this.


icon
~~~~

.. autofunction:: django_icons.templatetags.icons.icon


Renderers
=========

Some renderers support additional parameters.


ImageRenderer & Icons8PngCdnRenderer
------------------------------------

To get a variant representation of an icon (assuming that variant exists), you can specify:

size : int
    The size for this icon, if different from the default value. When using the ImageRenderer, the icon file name must contain that value.

color : str
    The color for this icon, if different from the default value. When using the ImageRenderer, the icon file name must contain that value.

format : str
    The format (file extension) for this icon, if different from the default value. When using the ImageRenderer, the icon file name must have that extension.

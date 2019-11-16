from django import template

from .. import icon

register = template.Library()


@register.simple_tag(name="icon")
def do_icon(name, *args, **kwargs):
    """
    Render an icon.

    This template is an interface to the `icon` function from `django_icons`

    **Tag name**::

        icon

    **Parameters**:

        name
            The name of the icon to be rendered

        title
            The title attribute for the icon

            :default: None (no title attribute rendered)

        renderer
            The renderer to use for the icon

            :default: The default renderer as per ``settings.py``, or ultimately `FontAwesomeRenderer`.

    **Usage**::

        {% icon name %}

    **Example**::

        {% icon 'pencil' %}
        {% icon 'pencil' 'fa-big' %}
        {% icon 'trash' title='Delete' %}
    """
    return icon(name, *args, **kwargs)

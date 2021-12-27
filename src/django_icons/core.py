import warnings

from django.utils.functional import keep_lazy_text

from .utils import get_icon_kwargs, get_icon_renderer


def icon(name, *args, **kwargs):
    """
    Render an icon.

    Deprecated because of frequent name collisions.
    """
    warnings.warn("The `icon` function is deprecated, user `render_icon` instead.", DeprecationWarning)
    return render_icon(name, *args, **kwargs)


@keep_lazy_text
def render_icon(name, *args, **kwargs):
    """
    Render an icon.

    **Parameters**:

        name
            The name of the icon to be rendered

        title
            The title attribute for the icon

            :default: None (no title attribute rendered)

        renderer
            The renderer to use for the icon

            :default: The default renderer as per ``settings.py``, or ultimately `IconRenderer`.

    **Usage**::

        render_icon(name)

    **Example**::

        render_icon('pencil')
        render_icon('trash', title='Delete')
    """
    icon_kwargs = get_icon_kwargs(name, *args, **kwargs)
    renderer_class = get_icon_renderer(icon_kwargs.get("renderer", None))
    renderer = renderer_class(**icon_kwargs)
    return renderer.render()

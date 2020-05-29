from .__about__ import __version__
from .utils import get_icon_kwargs, get_icon_renderer

__all__ = ["__version__", "icon"]


def icon(name, *args, **kwargs):
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

            :default: The default renderer as per ``settings.py``, or ultimately `FontAwesomeRenderer`.

    **Usage**::

        icon(name)

    **Example**::

        icon('pencil')
        icon('trash', title='Delete')
    """
    icon_kwargs = get_icon_kwargs(name, *args, **kwargs)
    renderer_class = get_icon_renderer(icon_kwargs.get("renderer", None))
    renderer = renderer_class(**icon_kwargs)
    return renderer.render()

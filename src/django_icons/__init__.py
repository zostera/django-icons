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


def icon_attribution(renderer=None, *args, **kwargs):
    """
    Render an attribution text, to be used as a citation for the source.

    **Parameters**:

        renderer
            The renderer for which to generate a copyright text

            :default: The default renderer as per ``settings.py``, or ultimately `FontAwesomeRenderer`.

    **Usage**::

        icon_copyright(renderer)

    **Example**::

        icon_attribution()
        icon_attribution('Icons8PngCdnRenderer')
        icon_attribution('Icons8PngCdnRenderer', extra_classes='my-css')
    """
    renderer_class = get_icon_renderer(renderer)
    tag_kwargs = get_icon_kwargs(renderer_class.__name__, *args, **kwargs)
    renderer = renderer_class(**tag_kwargs)
    return renderer.render_attribution()

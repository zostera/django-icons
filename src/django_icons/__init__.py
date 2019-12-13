from .utils import get_icon_kwargs, get_icon_renderer

try:
    from ._version import version
except ImportError:
    try:
        from setuptools_scm import get_version

        version = get_version()
    except ImportError:
        version = "???"
__version__ = version


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

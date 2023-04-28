import warnings
from copy import deepcopy

from django.conf import settings
from django.utils.functional import keep_lazy_text
from django.utils.module_loading import import_string
from django.utils.safestring import mark_safe

from django_icons.css import merge_css_list
from django_icons.renderers import Bootstrap3Renderer, FontAwesome4Renderer, IconRenderer, ImageRenderer
from django_icons.renderers.material import MaterialRenderer

DEFAULT_RENDERERS = {
    "icon": IconRenderer,
    "fontawesome4": FontAwesome4Renderer,
    "bootstrap3": Bootstrap3Renderer,
    "material": MaterialRenderer,
    "image": ImageRenderer,
}


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
            The name of the icon to be rendered.

        title
            The title attribute for the icon

            :default: None (no title attribute rendered).

        renderer
            The renderer to use for the icon

            :default: The default renderer as per ``settings.py``, or ultimately `IconRenderer`.

        tag
            The tag to use for the icon

            :default: Each renderer has a default tag set. This parameter overrides the renderer's default tag.

    **Usage**::

        render_icon(name)

    **Example**::

        render_icon("pencil")
        render_icon("trash", title="Delete")
    """
    icon_kwargs = get_icon_kwargs(name, *args, **kwargs)
    renderer_class = get_icon_renderer(icon_kwargs.get("renderer", None))
    renderer = renderer_class(**icon_kwargs)
    return renderer.render()


def _get_setting(section, name, default=None):
    """Return a setting from a section, optionally provide default."""
    try:
        # Read from settings
        setting = deepcopy(settings.DJANGO_ICONS[section][name])
    except (AttributeError, KeyError, TypeError):
        # Set to default
        setting = default

    return setting


def _render_settings_content(content):
    """Render content from icon settings."""
    if not isinstance(content, list):
        content = [content]
    result = mark_safe("")
    for item in content:
        result += render_icon(**item) if isinstance(item, dict) else str(item)
    return result


def get_icon_kwargs_from_settings(name):
    """Return the kwargs from settings, return a dict with at least a `name` key."""
    kwargs_from_settings = _get_setting("ICONS", name, {})
    if isinstance(kwargs_from_settings, str):
        kwargs_from_settings = {"name": kwargs_from_settings}
    kwargs_from_settings.setdefault("name", name)
    if "content" in kwargs_from_settings:
        kwargs_from_settings["content"] = _render_settings_content(kwargs_from_settings["content"])
    return kwargs_from_settings


def get_icon_kwargs(name, *args, **kwargs):
    """Build the kwargs for the icon function based on args and kwargs of the template tag."""
    icon_kwargs = get_icon_kwargs_from_settings(name)
    extra_classes = icon_kwargs.get("extra_classes", "")

    icon_kwargs.update(kwargs)

    extra_classes = merge_css_list(extra_classes, args, kwargs.get("extra_classes", ""))
    if extra_classes:
        icon_kwargs["extra_classes"] = extra_classes

    return icon_kwargs


def _get_icon_renderer_by_name(name):
    """Return class or dotted path to renderer class with this name from dict in settings."""
    default = DEFAULT_RENDERERS.get(name, None)
    renderer_class = _get_setting("RENDERERS", name, default)
    return renderer_class if renderer_class else name


def get_icon_renderer(renderer=None):
    """Return the default icon renderer."""
    renderer_class = renderer or _get_setting("DEFAULTS", "renderer", IconRenderer)

    if isinstance(renderer_class, str):
        renderer_class = _get_icon_renderer_by_name(renderer_class)
        if isinstance(renderer_class, str):
            if "." not in renderer_class:
                renderer_class = f"django_icons.renderers.{renderer_class}"
            renderer_class = import_string(renderer_class)

    return renderer_class

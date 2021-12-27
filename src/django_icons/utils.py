from copy import deepcopy

from django.conf import settings
from django.utils.module_loading import import_string

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


def _get_setting(section, name, default=None):
    """Return a setting from a section, optionally provide default."""

    try:
        # Read from settings
        setting = deepcopy(settings.DJANGO_ICONS[section][name])
    except (AttributeError, KeyError, TypeError):
        # Set to default
        setting = default

    return setting


def get_icon_kwargs_from_settings(name):
    """Return the kwargs from settings, return a dict with at least a `name` key."""

    kwargs_from_settings = _get_setting("ICONS", name, {})
    if isinstance(kwargs_from_settings, str):
        kwargs_from_settings = {"name": kwargs_from_settings}
    kwargs_from_settings.setdefault("name", name)
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

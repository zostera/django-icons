from copy import deepcopy

from django.conf import settings
from django.utils.module_loading import import_string

from django_icons.css import merge_css_list
from django_icons.renderers import Bootstrap3Renderer, FontAwesomeRenderer, ImageRenderer
from django_icons.renderers.material import MaterialRenderer

DEFAULT_RENDERERS = {
    "fontawesome": FontAwesomeRenderer,
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

    # Read dict from settings, default is an empty dict
    kwargs_from_settings = _get_setting("ICONS", name, {})

    # Settings might return single string, convert to dict with key `name`
    if isinstance(kwargs_from_settings, str):
        kwargs_from_settings = {"name": kwargs_from_settings}

    # If no name is set, set the name
    kwargs_from_settings.setdefault("name", name)

    # Return the dict
    return kwargs_from_settings


def get_icon_kwargs(name, *args, **kwargs):
    """Build the kwargs for the icon function based on args and kwargs of the template tag."""

    # Get kwargs from settings, name will always be set
    icon_kwargs = get_icon_kwargs_from_settings(name)

    # Remember the name, we do not allow this to be overwritten
    remember_name = icon_kwargs["name"]

    # Update with kwargs
    icon_kwargs.update(kwargs)

    # Merge args with extra_classes
    extra_classes = merge_css_list(args, kwargs.get("extra_classes", ""))
    if extra_classes:
        icon_kwargs["extra_classes"] = extra_classes

    # Check the name
    assert icon_kwargs["name"] == remember_name, "Overwriting the icon name is not allowed"

    # Return the dict
    return icon_kwargs


def _get_icon_renderer_by_name(name):
    """Return class or dotted path to renderer class with this name from dict in settings."""

    # Get the default value
    default = DEFAULT_RENDERERS.get(name, None)

    # Fetch the value from the settings dict
    renderer_class = _get_setting("RENDERERS", name, default)

    # If no result is found, return the original argument
    if renderer_class is None:
        renderer_class = name

    # Return result
    return renderer_class


def get_icon_renderer(renderer=None):
    """Return the default icon renderer."""

    # Renderer from parameter or default renderer
    renderer_class = renderer if renderer else _get_setting("DEFAULTS", "renderer", FontAwesomeRenderer)

    # Translate a name to a full path
    if isinstance(renderer_class, str):

        # Note that a dotted path remains a dotted path if it is not a name
        renderer_class = _get_icon_renderer_by_name(renderer_class)

        # If we still have a string, it has to be a dotted path to the class
        if isinstance(renderer_class, str):
            # Be kind to our own Renderers
            if "." not in renderer_class:
                renderer_class = "django_icons.renderers.{}".format(renderer_class)
            # Import the class with a Django shortcut
            renderer_class = import_string(renderer_class)

    # Done
    return renderer_class

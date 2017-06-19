import importlib

from django.conf import settings
from django.utils import six

from django_icons.css import merge_css_list
from django_icons.renderers import FontAwesomeRenderer, BaseRenderer


def _get_setting(section, name, default=None):
    """
    Read a setting from a section, optionally provide default
    """
    try:
        # Read from settings
        setting = settings.DJANGO_ICONS[section][name]
    except (AttributeError, KeyError):
        # Set to default
        setting = default
    return setting


def get_icon_kwargs_from_settings(name):
    """
    Get the kwargs from settings, return a dict with at least a `name` key
    """
    # Read dict from settings, default is an empty dict
    kwargs_from_settings = _get_setting('ICONS', name, {})
    # Settings might return dingle string, convert to dict with key `name`
    if isinstance(kwargs_from_settings, six.string_types):
        kwargs_from_settings = {'name': kwargs_from_settings}
    # If no name is set, set the name
    kwargs_from_settings.setdefault('name', name)
    # Return the dict
    return kwargs_from_settings


def get_icon_kwargs(name, *args, **kwargs):
    """
    Build the kwargs for the icon function based on args and kwargs of the template tag
    """
    # Get kwargs from settings, name will always be set
    icon_kwargs = get_icon_kwargs_from_settings(name)
    # Remember the name, we do not allow this to be overwritten
    remember_name = icon_kwargs['name']
    # Update with kwargs
    icon_kwargs.update(kwargs)
    # Merge args with extra_classes
    icon_kwargs['extra_classes'] = merge_css_list(args, kwargs.get('extra_classes', ''))
    # Check the name
    assert icon_kwargs['name'] == remember_name, 'Overwriting the icon name is not allowed'
    # Return the dict
    return icon_kwargs


def get_default_icon_renderer():
    """
    Get the default icon renderer
    """
    return _get_setting('DEFAULTS', 'renderer', FontAwesomeRenderer)


def get_icon_renderer(renderer):
    """
    Default to Font Awesome
    """

    # Get the default if no renderer is given
    renderer_class = renderer if renderer else get_default_icon_renderer()

    # Translate a name to a class
    renderer_class = _get_setting('RENDERERS', renderer_class, renderer_class)

    # If this is not an actual BaseRenderer, it
    # must be a string with the path to the class
    if not isinstance(renderer_class, BaseRenderer):
        parts = '{}'.format(renderer_class).split('.')
        renderer_class_name = parts.pop()
        path_to_module = '.'.join(parts)
        if not path_to_module:
            path_to_module = 'django_icons.renderers'
        module = importlib.import_module(path_to_module)
        renderer_class = getattr(module, renderer_class_name)

    # Return the result
    return renderer_class

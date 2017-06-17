import importlib

from django.conf import settings
from django.utils import six

from django_icons.css import merge_css_list
from django_icons.renderers import FontAwesomeRenderer


def get_icon_kwargs_from_settings(name):
    """
    Get the kwargs from settings, return a dict with at least a `name` key
    """
    try:
        # Read from settings
        kwargs_from_settings = settings.ICONS.get(name, {})
    except AttributeError:
        # Set to empty dict
        kwargs_from_settings = {}
    else:
        # If settings only provides a string, set that as name
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


def get_icon_renderer(renderer):
    """
    Default to Font Awesome
    """
    if renderer:
        parts = renderer.split('.')
        renderer_class_name = parts.pop()
        path_to_module = '.'.join(parts)
        if not path_to_module:
            path_to_module = 'django_icons.renderers'
        module = importlib.import_module(path_to_module)
        renderer_class = getattr(module, renderer_class_name)
        return renderer_class
    return FontAwesomeRenderer

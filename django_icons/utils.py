from django_icons.renderers import FontAwesomeRenderer


def get_css_classes(classes_list, extra_classes=None):
    """
    Join a list of CSS classes with a space separated string of CSS classes
    """
    css_classes = [c for c in classes_list]
    for c in extra_classes.split(' '):
        if c and c not in css_classes:
            css_classes.append(c)
    return ' '.join(css_classes)


def get_icon_kwargs(name, *args, **kwargs):
    icon_kwargs = dict()
    icon_kwargs.update(kwargs)
    icon_kwargs['extra_classes'] = get_css_classes(args, kwargs.get('extra_classes', ''))
    icon_kwargs['name'] = name
    return icon_kwargs


def get_icon_renderer(renderer):
    return FontAwesomeRenderer

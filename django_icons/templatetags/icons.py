# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

from ..utils import get_icon_kwargs, get_icon_renderer

register = template.Library()


@register.simple_tag
def icon(name, *args, **kwargs):
    """
    Render an icon
    """
    icon_kwargs = get_icon_kwargs(name, *args, **kwargs)
    renderer_class = get_icon_renderer(icon_kwargs.get('renderer', None))
    renderer = renderer_class(**icon_kwargs)
    return renderer.render()

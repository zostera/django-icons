import os
from django.conf import settings
from django.forms.utils import flatatt
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from django_icons.css import merge_css_text
from django_icons.renderers.base import BaseRenderer


class ImageRenderer(BaseRenderer):
    """
    Render an icon from a local file

    <img src="/static/icons/icon.png' %}">
    """

    def get_icon_prefix(self):
        return ''

    def get_prefix(self):
        return 'icons'

    def get_size(self):
        return None

    def get_format(self):
        return 'png'

    def get_path(self):
        basename = self.get_prefix()
        filename = self.get_icon_prefix() + self.name
        if self.get_size():
            filename += '-' + str(self.get_size())
        filename += '.' + self.get_format()
        return os.path.join(settings.STATIC_URL, basename, filename)

    def render(self):
        """
        Render the icon
        """
        builder = '<img src="{path}"{attrs}>'
        attrs = self.get_attrs()
        attrs['class'] = merge_css_text(self.get_css_classes())
        attrs = self.clean_attrs(attrs)
        return format_html(
            builder,
            path=self.get_path(),
            attrs=mark_safe(flatatt(attrs)) if attrs else '',
        )

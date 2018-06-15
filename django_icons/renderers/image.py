from django.forms.utils import flatatt
from django.templatetags.static import static
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from django_icons.css import merge_css_text
from django_icons.renderers.base import BaseRenderer


class ImageRenderer(BaseRenderer):
    """
    Render an icon from a local file.

    For example, calling in a template:
        {% icons 'myicon' %}

    will produce the following tag:
        <img src="/static/icons/myicon.png'" class="icon icon-myicon" %}">

    """

    def get_class(self):
        """
        First class, usually defines the icon
        """
        return 'icon icon-{name}'.format(name=self.name)

    def get_icon_prefix(self):
        """
        Filename prefix. For example, Icons8 icons are all prefixed with `icons8-`, so that you can call your icons
        without repeating the prefix in the name.
        """
        return ''

    def get_icons_dirname(self):
        """
        Relative path to the icons folder, starting from the static folder. Do not include the trailing '/'.
        """
        return 'icons'

    def get_size(self):
        """
        Icon size, in case several sizes are available (assumed postfixed with `-XX` where XX is the size)
        """
        return None

    def get_format(self):
        """
        Icon format, without dot

        For example: 'png'.
        """
        return 'png'

    def get_path(self):
        """
        Relative path to the icon
        """
        dirname = self.get_icons_dirname()
        filename = self.get_icon_prefix() + self.name
        if self.get_size():
            filename += '-' + str(self.get_size())
        filename += '.' + self.get_format()
        return static('{}/{}'.format(dirname, filename))

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

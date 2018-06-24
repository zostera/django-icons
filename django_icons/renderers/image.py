import re

from django.forms.utils import flatatt
from django.templatetags.static import static
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from django_icons.css import merge_css_text
from django_icons.renderers.base import BaseRenderer


class ImageRenderer(BaseRenderer):
    """
    Render an icon from a local file, each icon being a single file. The icon will be rendered using an <img> tag.

    All the icons must have the same extensions. Variants of an icon can be saved under variants (color, size) of the
    filename, following a pre-defined pattern (customizable).

    For each rendered icon, the default CSS classes will be 'icon' and a composed name class 'icon-{name}' where
    {name} is the name of the icon.
    If color and/or size variants are defined, by default composed name classes will be added, following the
    'icon-{variant}' pattern. There will be one class per variant.

    By default, icons are assumed to be located in the 'static/icons' folder. But this can be customized, to have for
    example one folder for each color and/or size.

    For example, to support different colors of an icon, you could postfix the color code as '-c:w' for white or '-c:r'
    for red. Or supporting different sizes like '-s:48' for 48 pixels or '-s:96' for 96 pixels.

    For example, calling in a template:
        {% icon 'myicon' %}

    will produce the following tag:
        <img src="/static/icons/myicon.png'" class="icon icon-myicon" %}">

    To customize the default behaviours, create you own ImageRenderer by subclassing this one and override the methods
    to suit you needs.

    """

    from collections import namedtuple

    VariantPattern = namedtuple('VariantPattern', ['key', 'pattern'])
    _variant_patterns = dict()

    def __init__(self, *args, **kwargs):
        super(ImageRenderer, self).__init__(*args, **kwargs)
        # 'alt' is a mandatory tag attribute
        self.kwargs.setdefault('alt', _('{} icon'.format(self.name.title())))
        self.variant = dict()

    @classmethod
    def get_image_root(cls):
        """
        The root path to the images folder. By default, returns the path to a 'icons' folder inside the static folder.

        Returns
        -------
        str or callable

        """
        return static('icons')

    @classmethod
    def get_image_prefix(cls):
        """
        Filename prefix. For example, Icons8 icons are all prefixed with `icons8-`, so that you can call your icons
        without repeating the prefix in the name.
        """
        return ''

    @classmethod
    def get_image_variant_patterns(cls):
        """

        Returns
        -------

        """
        return [cls.VariantPattern('color', '-c:(?P<{}>\w+)'), cls.VariantPattern('size', '-s:(?P<{}>\w+)')]

    @classmethod
    def get_image_format(cls):
        """
        Icon format, without dot

        For example: 'png'.
        """
        return 'png'

    @classmethod
    def _get_image_v_p_regex(cls):
        """
        Compile the variant regular expression patterns into a regular expression object

        Returns
        -------
        Regular expression object

        """

        if not cls._variant_patterns:
            for v in cls.get_image_variant_patterns():
                cls._variant_patterns[v.key] = re.compile(v.pattern.format(v.key))
        return cls._variant_patterns

    def get_variant(self):
        """

        Returns
        -------
        dict : dict containing the variant values

        """
        if not self.variant:
            for key, pattern in self._get_image_v_p_regex().items():
                variant = pattern.search(self.name)
                if variant:
                    self.variant[key] = variant.group(key)
                    self.name = pattern.sub('', self.name)
        return self.variant

    def render_variant(self):
        """

        Returns
        -------
        str : The string representing the variant to be appended to the icon name to build the path to the file in the
                file system

        """
        variant = self.get_variant()
        v_s = ''
        if variant:
            for v in self.get_image_variant_patterns():
                if v.key in variant:
                    v_s += '-{}'.format(variant[v.key])
        return v_s

    def get_path(self):
        """
        Relative path to the icon.

        By default, the icon filename is built as '{name}[-{color}][-{size}][-{variantX}]' where '-{color}' '-{size}'
        and '-{variantX}'s are only added if there are defined (if several are defined, they are added in that order).
        """
        filename = self.get_image_prefix() + self.name + self.render_variant() + '.' + self.get_image_format()
        return '{}/{}'.format(self.get_image_root(), filename)

    def get_class(self):
        """
        First CSS classes: 'icon' and 'icon-{name}' where {name} is the given name of the icon in the templatetag.

        If the icon defines a color and/or size, 'icon-{color}' and/or 'icon-{size}' classes will be added as well.
        """
        css_classes = 'icon'
        if self.get_image_prefix():
            css_classes += ' icon-{prefix}'.format(prefix=self.name)
        for v_p in self.get_image_variant_patterns():
            if v_p.key in self.get_variant():
                css_classes += ' icon-{variant}-{value}'.format(variant=v_p.key, value=self.get_variant()[v_p.key])
        css_classes += ' icon-{name}'.format(name=self.name)
        return css_classes

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

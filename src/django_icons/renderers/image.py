import re
from collections import namedtuple

from django.forms.utils import flatatt
from django.templatetags.static import static
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from django_icons.css import merge_css_text
from django_icons.renderers.base import BaseRenderer


class ImageRenderer(BaseRenderer):
    """
    Render an icon from a local file, each icon being a single file rendered with an <img> tag.

    All the icons must have the same extensions. Variants of an icon can be saved under variants (color, size) of the
    filename, following a pre-defined pattern.

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

    To customize the default behaviour, create a custom ``ImageRenderer``::

        # app/renderers.py
        from django_icons.renderers import ImageRenderer

        class CustomImageRenderer(ImageRenderer):
            def get_image_root(cls):
                return "special-icons"

        DJANGO_ICONS = {
            "DEFAULTS": {"renderer": "fontawesome", "attrs": {"aria-hidden": True}},
            "RENDERERS": {
                "image": "app.renderers.CustomImageRenderer",
            },
            "ICONS": {
                "edit": {"renderer": "image"},
            }
        }

    The template tag supports settings keyword parameters to define the variant attributes and/or set the format. The
    keyword must be the key of the variant attribute. Please note that using keyword parameters will supersede the
    parsing of the name. That is, the variant attributes are set from the keyword parameters and the file name is not
    parsed.
    The format can be defined by the 'format' keyword parameter without altering the definition of variant attributes.
    """

    r"""
    The VariantAttributePattern must contain a named grouped, where the name must be specified as `{}` as it will be
    injected from the key. That is, the pattern used here to match a color specification looks like `-c:(?P<{}>\\w+)`,
    where `-c:` is arbitrary, `<{}>` represents the matching group name and `\\w+` matches for at least one
    alphanumeric character (color code be a name or a code).
    """
    VariantAttributePattern = namedtuple("VariantAttributePattern", ["key", "pattern", "default"])
    _variant_attributes_regex = dict()  # Used to store the compiled regexes of the individual variant attributes

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Dict used to store the variant attributes extracted from icon name
        self.variant_attributes = dict()
        # If variant attributes are set by keyword arguments, they are set here
        # Using keyword arguments supersedes the parsing from the icon name
        vapatterns = self.get_image_variant_attributes_pattern()
        if True in [vap.key in self.kwargs for vap in vapatterns]:
            for vap in vapatterns:
                k = vap.key
                if k in kwargs:
                    self.variant_attributes[k] = kwargs[k]
                elif vap.default:
                    self.variant_attributes[k] = vap.default

    @classmethod
    def get_image_root(cls):
        """
        Return the root path to the images folder.

        By default, returns the path to a 'icons' folder inside the static folder.

        :return: str or callable
        """
        return "icons"

    @classmethod
    def get_image_prefix(cls):
        """
        Return filename prefix.

        For example, Icons8 icons are all prefixed with `icons8-`, so that you can call your icons
        without repeating the prefix in the name.
        """
        return ""

    @classmethod
    def get_image_variant_attributes_pattern(cls):
        """
        Return list of patterns to match the available variant attributes.

        :return: list Contains the patterns to match the available variant attributes.
        """
        return [
            cls.VariantAttributePattern("color", r"-c:(?P<{}>\w+)", None),
            cls.VariantAttributePattern("size", r"-s:(?P<{}>\w+)", None),
        ]

    @classmethod
    def get_image_format(cls):
        """
        Return icon format, without dot.

        For example: 'png'.
        """
        return "png"

    @classmethod
    def _get_image_variant_attributes_regex(cls):
        """
        Compile the regular expression pattern of the variant attributes into regular expression objects.

        :return: dict Key is the variant attribute name and value is a tuple of compiled regex and default value
        """

        if not cls._variant_attributes_regex:
            for v in cls.get_image_variant_attributes_pattern():
                cls._variant_attributes_regex[v.key] = (
                    re.compile(v.pattern.format(v.key)),
                    v.default,
                )
        return cls._variant_attributes_regex

    def get_variant_attributes(self):
        """
        Return the variant attributes.

        :return: dict The variant attributes.
        """
        if not self.variant_attributes:
            for key, pattern in self._get_image_variant_attributes_regex().items():
                regex, default = pattern
                variant = regex.search(self.name)
                if variant:
                    self.variant_attributes[key] = variant.group(key)  # We fetch the matched group by its name
                    self.name = regex.sub("", self.name)  # Remove the parsed variant specifier from the icon name
                elif default:
                    self.variant_attributes[key] = default
        return self.variant_attributes

    def render_variant(self):
        """
        Alter the name of the icon by removing the variant attribute definitions.

        :return: str The variant to be appended to the icon name to build the path to the file in the file system.
        """
        variant_attributes = self.get_variant_attributes()
        variant = ""
        if variant_attributes:
            for v in self.get_image_variant_attributes_pattern():
                if v.key in variant_attributes:
                    variant += "-{}".format(variant_attributes[v.key])
        return variant

    def get_path(self):
        """
        Return the relative path to the icon.

        By default, the icon filename is built as '{name}[-{color}][-{size}][-{variantX}]' where '-{color}' '-{size}'
        and '-{variantX}'s are only added if there are defined (if several are defined, they are added in that order).
        """
        variant = self.render_variant()  # Alters the name
        filename = (
            self.get_image_prefix()
            + self.name
            + variant
            + "."
            + (self.kwargs.get("format", None) or self.get_image_format())
        )
        return "{}/{}".format(static(self.get_image_root()), filename)

    def get_class(self):
        """
        Return CSS class string for the icons.

        First CSS classes: 'icon' and 'icon-{name}' where {name} is the given name of the icon in the templatetag.

        If the icon defines a color and/or size, 'icon-{color}' and/or 'icon-{size}' classes will be added as well.
        """
        css_classes = "icon"
        if self.get_image_prefix():
            css_classes += " icon-{prefix}".format(prefix=self.name)
        for v_p in self.get_image_variant_attributes_pattern():
            if v_p.key in self.get_variant_attributes():
                css_classes += " icon-{variant}-{value}".format(
                    variant=v_p.key, value=self.get_variant_attributes()[v_p.key]
                )
        css_classes += " icon-{name}".format(name=self.name)
        return css_classes

    def get_attrs(self):
        attrs = super(ImageRenderer, self).get_attrs()
        # 'alt' is a mandatory img tag attribute
        cleaned_name = self.name.replace("-", " ").replace("_", " ").title()
        attrs["alt"] = self.kwargs.get("alt", _("Icon of {}").format(cleaned_name))
        return attrs

    def render(self):
        """Render the icon."""
        builder = '<img src="{path}"{attrs}>'
        src = self.get_path()  # Alters the name
        attrs = self.get_attrs()
        attrs["class"] = merge_css_text(self.get_css_classes())
        attrs = self.clean_attrs(attrs)
        return format_html(builder, path=src, attrs=mark_safe(flatatt(attrs)) if attrs else "")

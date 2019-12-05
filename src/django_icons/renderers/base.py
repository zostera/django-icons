from django.forms.utils import flatatt
from django.utils.encoding import force_text
from django.utils.html import escape, format_html
from django.utils.safestring import mark_safe

from django_icons.css import merge_css_list, merge_css_text


class BaseRenderer(object):
    """Basic renderer to i tag with a few attributes."""

    def __init__(self, name, **kwargs):
        """Set name and kwargs."""
        super(BaseRenderer, self).__init__()
        self.name = name
        self.content = ""
        self.kwargs = kwargs

    def get_tag(self):
        """Return default tag for HTML builder."""
        return "i"

    def get_class(self):
        """
        Return primary CSS class for this icon.

        This is usually the icon's name.
        """
        return self.name

    def get_extra_classes(self):
        """Return list of other classes for this icon."""
        return merge_css_list(self.kwargs.get("extra_classes", None))

    def get_css_classes(self):
        """Return list of all CSS classes for this icon."""
        return merge_css_list(self.get_class(), self.get_extra_classes())

    def get_attrs(self):
        """Return HTML attributes for this icons."""
        attrs = {}
        # The `title` attribute is a string
        try:
            attrs["title"] = self.kwargs["title"]
        except KeyError:
            pass
        return attrs

    def clean_attrs(self, attrs):
        """
        Return cleaned dictionary of HTML attributes.

        This applies `escape` to everything except `id` and `class` per HTML 5 specification.
        """
        return {k: escape(v) if k not in ("id", "class") else v for k, v in attrs.items()}

    def get_content(self):
        """Return tag content for the icon."""
        return self.content

    def render(self):
        """Render the icon."""
        builder = "<{tag}{attrs}>{content}</{tag}>"
        tag = self.get_tag()
        attrs = self.get_attrs()
        attrs["class"] = merge_css_text(self.get_css_classes())
        attrs = self.clean_attrs(attrs)
        content = self.get_content()
        return format_html(
            builder,
            tag=tag,
            attrs=mark_safe(flatatt(attrs)) if attrs else "",
            content=mark_safe(force_text(content) if content else ""),
        )

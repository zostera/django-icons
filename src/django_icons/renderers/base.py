from django.forms.utils import flatatt
from django.utils.html import format_html

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
        """Return HTML attributes for this icon."""
        attrs = {}
        title = self.kwargs.get("title")
        if title:
            attrs["title"] = title
        css_classes = merge_css_text(self.get_css_classes())
        if css_classes:
            attrs["class"] = css_classes
        return attrs

    def get_content(self):
        """Return tag content for the icon."""
        return self.content or ""

    def get_format_string(self):
        return "<{tag}{attrs}>{content}</{tag}>"

    def get_format_context(self):
        return {
            "tag": self.get_tag(),
            "attrs": flatatt(self.get_attrs()),
            "content": self.get_content(),
        }

    def render(self):
        """Render the icon."""
        return format_html(self.get_format_string(), **self.get_format_context())

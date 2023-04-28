from django.forms.utils import flatatt
from django.utils.html import format_html

from django_icons.css import merge_css_list, merge_css_text


class IconRenderer:
    """Render an icon as an HTML element."""

    tag = "i"
    format_string = "<{tag}{attrs}>{content}</{tag}>"

    def __init__(self, name, content="", tag=None, **kwargs):
        """Set name and kwargs."""
        super().__init__()
        self.name = name
        self.content = content
        self.kwargs = kwargs
        if tag:
            self.tag = tag

    def get_tag(self):
        """Return default tag for HTML builder."""
        return self.tag

    def get_class(self):
        """Return primary CSS class for this icon."""
        return self.name

    def get_extra_classes(self):
        """Return list of other classes for this icon."""
        return merge_css_list(self.kwargs.get("extra_classes", None))

    def get_css_classes(self):
        """Return list of all CSS classes for this icon."""
        return merge_css_list(self.get_class(), self.get_extra_classes())

    def get_attrs(self):
        """Return HTML attributes for this icon."""
        attrs = self.kwargs.get("attrs", {})
        title = self.kwargs.get("title")
        if title:
            attrs["title"] = title
        css_classes = merge_css_text(self.get_css_classes())
        if css_classes:
            attrs["class"] = css_classes
        return attrs

    def get_content(self):
        """Return content for the HTML element."""
        return self.content or ""

    def get_format_string(self):
        """Return format string for HTML output."""
        return self.format_string

    def get_format_context(self):
        """Return context for HTML output."""
        return {
            "tag": self.get_tag(),
            "attrs": flatatt(self.get_attrs()),
            "content": self.get_content(),
        }

    def render(self):
        """Return HTML output for icon."""
        return format_html(self.get_format_string(), **self.get_format_context())

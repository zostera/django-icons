from django.utils.html import format_html

from django_icons.renderers import IconRenderer


class CustomSvgRenderer(IconRenderer):
    """
    Render an SVG.

    <svg class="svg-icon" viewBox="0 0 32 32"><use xlink:href="#icon-feather"></use></svg>
    """

    def get_tag(self):
        return "svg"

    def get_class(self):
        return "svg-icon"

    def get_attrs(self):
        attrs = super().get_attrs()
        attrs["viewBox"] = "0 0 32 32"
        return attrs

    def get_content(self):
        return format_html('<use xlink:href="#icon-{name}"></use>', name=self.name)

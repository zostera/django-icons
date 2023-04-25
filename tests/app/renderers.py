from django_icons.renderers import IconRenderer, ImageRenderer


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
        return f'<use xlink:href="#icon-{self.name}"></use>'


class CustomImageRenderer(ImageRenderer):
    def get_image_root(cls):
        return "hd-icons"


class CustomIcons8Renderer(ImageRenderer):
    def get_image_prefix(self):
        return "icons8-"

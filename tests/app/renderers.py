from django_icons.renderers import BaseRenderer, ImageRenderer


class CustomSvgRenderer(BaseRenderer):
    """
    Render an SVG.

    <svg class="svg-icon" viewBox="0 0 32 32"><use xlink:href="#icon-feather"></use></svg>
    """

    def get_tag(self):
        return "svg"

    def get_class(self):
        return "svg-icon"

    def get_attrs(self):
        attrs = super(CustomSvgRenderer, self).get_attrs()
        attrs["viewBox"] = "0 0 32 32"
        return attrs

    def get_content(self):
        return '<use xlink:href="#icon-{name}"></use>'.format(name=self.name)


class CustomImageRenderer(ImageRenderer):
    def get_image_root(cls):
        return "hd-icons"


class CustomIcons8Renderer(ImageRenderer):
    def get_image_prefix(self):
        return "icons8-"

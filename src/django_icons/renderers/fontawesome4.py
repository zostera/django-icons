from django_icons.renderers.icon import IconRenderer


class FontAwesome4Renderer(IconRenderer):
    """
    Render a Font Awesome 4 icon.

    For FontAwesome 5, use IconRenderer.
    """

    def get_size(self):
        size = self.kwargs.get("size", None)
        return f"fa-{size}" if size else ""

    def get_class(self):
        return f"fa fa-{self.name} {self.get_size()}"

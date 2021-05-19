from django_icons.renderers.icon import IconRenderer


class Bootstrap3Renderer(IconRenderer):
    """Render a Bootstrap 3 icon."""

    def get_class(self):
        return f"glyphicon glyphicon-{self.name}"

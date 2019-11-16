from django_icons.renderers.base import BaseRenderer


class Bootstrap3Renderer(BaseRenderer):
    """Render a Font Awesome icon."""

    def get_class(self):
        """Return the primary CSS class for the icon."""
        return "glyphicon glyphicon-{name}".format(name=self.name)

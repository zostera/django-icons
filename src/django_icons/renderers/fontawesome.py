from django_icons.renderers.base import BaseRenderer


class FontAwesomeRenderer(BaseRenderer):
    """Render a Font Awesome icon."""

    def get_size(self):
        """Return the CSS class for a given size."""
        try:
            return "fa-{size}".format(size=self.kwargs["size"])
        except KeyError:
            return ""

    def get_class(self):
        """Return the primary CSS class for the icon."""
        return "fa fa-{name}".format(name=self.name)

    def get_extra_classes(self):
        """Return the extra CSS classes for the icon."""
        extra_classes = [
            super(FontAwesomeRenderer, self).get_extra_classes(),
            self.get_size(),
        ]
        return extra_classes

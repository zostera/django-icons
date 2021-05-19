from django_icons.renderers.icon import IconRenderer


class MaterialRenderer(IconRenderer):
    """
    Render a Material Design icon.

    <i class="material-icons md-light md-inactive">face</i>
    """

    def get_content(self):
        return self.name

    def get_class(self):
        return "material-icons"

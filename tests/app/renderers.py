from django_icons.renderers import BaseRenderer


class CustomSvgRenderer(BaseRenderer):
    """
    <svg class="svg-icon" viewBox="0 0 32 32"><use xlink:href="#icon-feather"></use></svg>
    """

    def get_tag(self):
        return 'svg'

    def get_class(self):
        return 'svg-icon'

    def get_attrs(self):
        attrs = super(CustomSvgRenderer, self).get_attrs()
        attrs['viewBox'] = '0 0 32 32'
        return attrs

    def get_content(self):
        return '<use xlink:href="#icon-{name}"></use>'.format(name=self.name)

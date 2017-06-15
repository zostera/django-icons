from django.utils.html import format_html


class BaseRenderer(object):
    def __init__(self, name, **kwargs):
        self.name = name
        self.kwargs = kwargs

    def get_tag(self):
        return 'i'

    def render(self):
        tag = self.get_tag()
        format_string = '<' + tag + ' class="{css_classes}"></' + tag + '>'
        name = 'fa-{name}'.format(name=self.name)
        fa_args = ['fa', name]
        return format_html(
            format_string,
            css_classes=u' '.join(fa_args),
        )


class FontAwesomeRenderer(BaseRenderer):
    pass

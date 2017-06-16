from django.forms.utils import flatatt
from django.utils.encoding import force_text
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from django_icons.css import merge_css_list


class BaseRenderer(object):
    def __init__(self, name, **kwargs):
        self.name = name
        self.kwargs = kwargs

    def get_tag(self):
        return 'i'

    def get_class(self):
        return self.name

    def get_extra_classes(self):
        return self.kwargs.get('extra_classes', None)

    def get_css_classes(self):
        css_classes = merge_css_list(self.get_class(), self.get_extra_classes())
        return ' '.join(css_classes)

    def get_attrs(self):
        attrs = {}
        try:
            attrs['title']=self.kwargs['title']
        except KeyError:
            pass
        return attrs

    def get_content(self):
        return ''

    def render(self):
        """
        Render the icon
        """
        builder = '<{tag}{attrs}>{content}</{tag}>'
        tag = self.get_tag()
        attrs = self.get_attrs()
        attrs['class'] = self.get_css_classes()
        content = self.get_content()
        return format_html(
            builder,
            tag=tag,
            attrs=mark_safe(flatatt(attrs)) if attrs else '',
            content=force_text(content) if content else '',
        )

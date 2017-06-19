from django.forms import MediaDefiningClass
from django.forms.utils import flatatt
from django.utils.encoding import force_text
from django.utils.html import format_html, escape
from django.utils.safestring import mark_safe

from django_icons.css import merge_css_list


class BaseRenderer(object):
    """
    Basic renderer to i tag with a few attributes
    """

    def __init__(self, name, **kwargs):
        super(BaseRenderer, self).__init__()
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
        # The `title` attribute is a string
        try:
            attrs['title'] = self.kwargs['title']
        except KeyError:
            pass
        return attrs

    def clean_attrs(self, attrs):
        """
        Takes a dict of attrs and cleans it
        NOTE: This applies `escape` to everything except `id` and `class` per HTML 5 spec
        """
        return {k: escape(v) if k not in ('id', 'class') else v for k, v in attrs.items()}

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
        attrs = self.clean_attrs(attrs)
        content = self.get_content()
        return format_html(
            builder,
            tag=tag,
            attrs=mark_safe(flatatt(attrs)) if attrs else '',
            content=mark_safe(force_text(content) if content else ''),
        )

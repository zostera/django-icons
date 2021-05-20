from django.template import Context, Template
from django.test import TestCase


def render_template(content, **context_args):
    """Create a template with content ``content`` that first loads the font-awesome tags."""
    template = Template("{% load icons %}" + content)
    return template.render(Context(context_args))


class TemplateTagsTest(TestCase):
    """Test all template tags."""

    def test_load_icons(self):
        # Loading the template should not generate an error
        self.assertEqual(render_template(""), "")

    def test_default_renderer(self):
        self.assertEqual(render_template('{% icon "name" %}'), '<i class="name"></i>')

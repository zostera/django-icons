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

    def test_icons(self):
        """Note the ICON settings in test/app/settings.py."""

        # FontAwesome without a mapping
        self.assertEqual(render_template('{% icon "user" %}'), '<i class="fa fa-user"></i>')

        # FontAwesome without a mapping, with extra class
        self.assertEqual(
            render_template('{% icon "user" "fa-big" %}'), '<i class="fa fa-user fa-big"></i>',
        )

        # FontAwesome with a mapping
        self.assertEqual(render_template('{% icon "delete" %}'), '<i class="fa fa-trash"></i>')

        # FontAwesome with a mapping, with extra class
        self.assertEqual(
            render_template('{% icon "delete" "foo bar" "end" %}'), '<i class="fa fa-trash foo bar end"></i>',
        )

        # FontAwesome with a mapping to a dict with a `title`
        self.assertEqual(
            render_template('{% icon "edit" %}'), '<i class="fa fa-pencil" title="Edit"></i>',
        )

        # FontAwesome with a mapping to a dict with a `title`, overwriting the `title` and testing UTF-8 char escaping
        self.assertIn(
            render_template('{% icon "edit" title="Edit\'" %}'),
            ('<i class="fa fa-pencil" title="Edit&#39;"></i>', '<i class="fa fa-pencil" title="Edit&#x27;"></i>',),
        )

        self.assertEqual(
            render_template("{% icon 'edit' title='Edit\"' %}"), '<i class="fa fa-pencil" title="Edit&quot;"></i>',
        )
        self.assertEqual(
            render_template('{% icon "edit" title="<Edit>" %}'), '<i class="fa fa-pencil" title="&lt;Edit&gt;"></i>',
        )

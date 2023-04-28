from django.test import TestCase

from .test_template_tags import render_template


class FontAwesome4Test(TestCase):
    """Test the FontAwesome 4 Renderer."""

    def test_icons(self):
        self.assertEqual(
            render_template('{% icon "user" size="lg" renderer="FontAwesome4Renderer" %}'),
            '<i class="fa fa-user fa-lg"></i>',
        )

        # FontAwesome without a mapping, with extra class
        self.assertEqual(
            render_template('{% icon "user" "fa-big" renderer="FontAwesome4Renderer" %}'),
            '<i class="fa fa-user fa-big"></i>',
        )

        # FontAwesome with a mapping
        self.assertEqual(render_template('{% icon "delete" %}'), '<i class="fa fa-trash"></i>')

        # FontAwesome with a mapping, with extra class
        self.assertEqual(
            render_template('{% icon "delete" "foo bar" "end" %}'),
            '<i class="fa fa-trash foo bar end"></i>',
        )

        # FontAwesome with a mapping to a dict with a `title`
        self.assertEqual(
            render_template('{% icon "edit" %}'),
            '<i class="fa fa-pencil" title="Edit"></i>',
        )

        # FontAwesome with a mapping to a dict with a `title`, overwriting the `title` and testing UTF-8 char escaping
        self.assertIn(
            render_template('{% icon "edit" title=title %}', title="Edit'"),
            (
                '<i class="fa fa-pencil" title="Edit&#39;"></i>',
                '<i class="fa fa-pencil" title="Edit&#x27;"></i>',
            ),
        )
        self.assertEqual(
            render_template('{% icon "edit" title=title %}', title='Edit"'),
            '<i class="fa fa-pencil" title="Edit&quot;"></i>',
        )
        self.assertEqual(
            render_template('{% icon "edit" title=title %}', title="<Edit>"),
            '<i class="fa fa-pencil" title="&lt;Edit&gt;"></i>',
        )

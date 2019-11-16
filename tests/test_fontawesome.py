from django.test import TestCase

from .test_template_tags import render_template


class FontAwesomeTest(TestCase):
    """Test the Font Awesome Renderer."""

    def test_icons(self):
        self.assertEqual(
            render_template('{% icon "user" size="lg" renderer="FontAwesomeRenderer" %}'),
            '<i class="fa fa-user fa-lg"></i>',
        )

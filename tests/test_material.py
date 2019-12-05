from django.test import TestCase

from .test_template_tags import render_template


class MaterialTest(TestCase):
    """Test the Material Design Renderer."""

    def test_icons(self):
        self.assertEqual(
            render_template('{% icon "user" renderer="MaterialRenderer" %}'), '<i class="material-icons">user</i>',
        )

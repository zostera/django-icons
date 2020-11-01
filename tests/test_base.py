from django.test import TestCase

from .test_template_tags import render_template


class BaseTest(TestCase):
    """Test the Font Awesome Renderer."""

    def test_version(self):
        from django_icons import __version__

        parts = __version__.split(".")
        self.assertEqual(len(parts), 3)

    def test_icons(self):
        self.assertEqual(
            render_template('{% icon "user" size="lg" renderer="BaseRenderer" %}'),
            '<i class="user"></i>',
        )
        self.assertEqual(
            render_template('{% icon "fas fa-user fa-2x" size="lg" renderer="BaseRenderer" %}'),
            '<i class="fas fa-user fa-2x"></i>',
        )

from django.test import TestCase

from .test_template_tags import render_template


class IconRendererTest(TestCase):
    """Test the IconRenderer."""

    def test_stacked_icon(self):
        self.assertEqual(
            render_template('{% icon "no-pictures-please" %}'),
            (
                '<span class="fa-stack fa-2x">'
                '<i class="fa-solid fa-camera fa-stack-1x"></i>'
                '<i class="fa-solid fa-ban fa-stack-2x" style="color:Tomato"></i>'
                "</span>"
            ),
        )

    def test_icons(self):
        self.assertEqual(
            render_template('{% icon "" %}'),
            "<i></i>",
        )
        self.assertEqual(
            render_template('{% icon "user" %}'),
            '<i class="user"></i>',
        )
        self.assertEqual(
            render_template('{% icon "fas fa-user fa-2x" %}'),
            '<i class="fas fa-user fa-2x"></i>',
        )

    def test_extra_classes(self):
        self.assertEqual(
            render_template('{% icon "extra-triangle" %}'),
            '<i class="fas fa-triangle fa-fw extra"></i>',
        )
        self.assertEqual(
            render_template('{% icon "extra-triangle" extra_classes="and more" %}'),
            '<i class="fas fa-triangle fa-fw extra and more"></i>',
        )
        self.assertEqual(
            render_template('{% icon "extra-triangle" "and" extra_classes="more" %}'),
            '<i class="fas fa-triangle fa-fw extra and more"></i>',
        )

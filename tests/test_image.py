from django.conf import settings
from django.test import TestCase, override_settings

from .test_template_tags import render_template


class ImageTest(TestCase):
    """Test the Image Renderer."""

    def test_icons(self):
        self.assertEqual(
            '<img src="/static/icons/icons8-icons8-48.png" alt="Icon of Icons8 Icons8 48" class="icon icon-icons8-icons8-48">',  # noqa
            render_template('{% icon "icons8-icons8-48" renderer="ImageRenderer" %}'),
        )
        self.assertEqual(
            '<img src="/static/icons/icons8-48.png" alt="Icon of Icons8 48" class="icon icon-icons8-48">',  # noqa
            render_template('{% icon "icons8-48" renderer="ImageRenderer" %}'),
        )
        self.assertEqual(
            '<img src="/static/icons/icons8-48.png" alt="Icon of Icons8" class="icon icon-size-48 icon-icons8">',
            render_template('{% icon "icons8-s:48" renderer="ImageRenderer" %}'),
        )
        self.assertEqual(
            '<img src="/static/icons/icons8-b.png" alt="Icon of Icons8" class="icon icon-color-b icon-icons8">',
            render_template('{% icon "icons8-c:b" renderer="ImageRenderer" %}'),
        )
        self.assertEqual(
            '<img src="/static/icons/icons8-b-48.png" alt="Icon of Icons8" class="icon icon-color-b icon-size-48 icon-icons8">',  # noqa
            render_template('{% icon "icons8-c:b-s:48" renderer="ImageRenderer" %}'),
        )
        self.assertEqual(
            '<img src="/static/icons/icons8-b-48.png" alt="Icon of Icons8" class="icon icon-color-b icon-size-48 icon-icons8">',  # noqa
            render_template('{% icon "icons8-s:48-c:b" renderer="ImageRenderer" %}'),
        )
        self.assertEqual(
            '<img src="/static/icons/icons8-b-48.jpg" alt="Icon of Icons8" class="icon icon-color-b icon-size-48 icon-icons8">',  # noqa
            render_template('{% icon "icons8-s:48-c:b" renderer="ImageRenderer" format="jpg" %}'),
        )
        self.assertEqual(
            '<img src="/static/icons/icons8-b-48.png" alt="Icon of Icons8" class="icon icon-color-b icon-size-48 icon-icons8">',  # noqa
            render_template('{% icon "icons8" renderer="ImageRenderer" size="48" color="b" %}'),
        )
        self.assertEqual(
            '<img src="/static/icons/icons8-s:48-c:b-b-48.png" alt="Icon of Icons8 S:48 C:B" class="icon icon-color-b icon-size-48 icon-icons8-s:48-c:b">',  # noqa
            render_template('{% icon "icons8-s:48-c:b" renderer="ImageRenderer" size="48" color="b" %}'),
        )
        self.assertEqual(
            '<img src="/static/icons/icons8-s:48-c:b-b-48.jpg" alt="Icon of Icons8 S:48 C:B" class="icon icon-color-b icon-size-48 icon-icons8-s:48-c:b">',  # noqa
            render_template('{% icon "icons8-s:48-c:b" renderer="ImageRenderer" size="48" color="b" format="jpg" %}'),
        )

    def test_path_dev(self):
        self.assertEqual(
            '<img src="'
            + settings.STATIC_URL
            + 'icons/icons8-48.png" alt="Icon of Icons8 48" class="icon icon-icons8-48">',
            render_template('{% icon "icons8-48" renderer="ImageRenderer" %}'),
        )
        self.assertEqual(
            '<img src="/static/icons/icons8-48.png" alt="Icon of Icons8 48" class="icon icon-icons8-48">',
            render_template('{% icon "icons8-48" renderer="ImageRenderer" %}'),
        )

    @override_settings(DEBUG=False, STATIC_URL="http://static.example.com/")
    def test_path_deploy(self):
        self.assertEqual(
            '<img src="'
            + settings.STATIC_URL
            + 'icons/icons8-48.png" alt="Icon of Icons8 48" class="icon icon-icons8-48">',
            render_template('{% icon "icons8-48" renderer="ImageRenderer" %}'),
        )
        self.assertEqual(
            '<img src="http://static.example.com/icons/icons8-48.png" alt="Icon of Icons8 48" class="icon icon-icons8-48">',  # noqa
            render_template('{% icon "icons8-48" renderer="ImageRenderer" %}'),
        )

    def test_custom_renderer_image_root(self):
        DJANGO_ICONS = {
            "DEFAULTS": {"renderer": "fontawesome", "attrs": {"aria-hidden": True}},
            "RENDERERS": {"image": "ImageRenderer", "hd-image": "tests.app.renderers.CustomImageRenderer"},
            "ICONS": {"edit": {"renderer": "image"}, "feather": {"renderer": "hd-image"}},
        }
        with override_settings(DJANGO_ICONS=DJANGO_ICONS):
            self.assertEqual(
                render_template("{% icon 'edit' %}"),
                '<img src="/static/icons/edit.png" alt="Icon of Edit" class="icon icon-edit">',
            )
            self.assertEqual(
                render_template("{% icon 'feather' %}"),
                '<img src="/static/hd-icons/feather.png" alt="Icon of Feather" class="icon icon-feather">',
            )

    def test_custom_renderer_image_prefix(self):
        DJANGO_ICONS = {
            "DEFAULTS": {"renderer": "fontawesome", "attrs": {"aria-hidden": True}},
            "RENDERERS": {"icons8": "tests.app.renderers.CustomIcons8Renderer"},
            "ICONS": {"icons8-48": {"renderer": "icons8"}},
        }
        with override_settings(DJANGO_ICONS=DJANGO_ICONS):
            self.assertEqual(
                render_template("{% icon 'icons8-48' %}"),
                '<img src="/static/icons/icons8-icons8-48.png" alt="Icon of Icons8 48" class="icon icon-icons8-48">',
            )

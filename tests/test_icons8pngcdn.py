# coding: utf-8
from __future__ import unicode_literals

from django.test import TestCase

from .test_template_tags import render_template


class ImageTest(TestCase):
    """
    Test the Image Renderer
    """

    def test_icons(self):
        self.assertEqual(
            '<img src="https://png.icons8.com/color/icons8.png" alt="Icon of Icons8" class="icon icon-style-color icon-icons8">',
            render_template('{% icon "icons8" renderer="Icons8PngCdnRenderer" %}'),
        )
        self.assertEqual(
            '<img src="https://png.icons8.com/dusk/96/c0392b/icons8.png" alt="Icon of Icons8" class="icon icon-style-dusk icon-size-96 icon-color-c0392b icon-icons8">',
            render_template('{% icon "icons8-y:dusk-c:c0392b-s:96" renderer="Icons8PngCdnRenderer" %}'),
        )
        self.assertEqual(
            '<img src="https://png.icons8.com/dusk/icons8.png" alt="Icon of Icons8" class="icon icon-style-dusk icon-icons8">',
            render_template('{% icon "icons8-y:dusk" renderer="Icons8PngCdnRenderer" %}'),
        )
        self.assertEqual(
            '<img src="https://png.icons8.com/color/c0392b/icons8.png" alt="Icon of Icons8" class="icon icon-style-color icon-color-c0392b icon-icons8">',
            render_template('{% icon "icons8-c:c0392b" renderer="Icons8PngCdnRenderer" %}'),
        )
        self.assertEqual(
            '<img src="https://png.icons8.com/color/96/icons8.png" alt="Icon of Icons8" class="icon icon-style-color icon-size-96 icon-icons8">',
            render_template('{% icon "icons8-s:96" renderer="Icons8PngCdnRenderer" %}'),
        )

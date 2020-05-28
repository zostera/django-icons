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
            '<img src="https://png.icons8.com/color/icons8.png" alt="Icon of Icons8" class="icon icon-theme-color icon-icons8">',
            render_template('{% icon "icons8" renderer="icons8pngcdn" %}'),
        )
        self.assertEqual(
            '<img src="https://png.icons8.com/dusk/96/c0392b/icons8.png" alt="Icon of Icons8" class="icon icon-theme-dusk icon-size-96 icon-color-c0392b icon-icons8">',
            render_template(
                '{% icon "icons8-t:dusk-c:c0392b-s:96" renderer="icons8pngcdn" %}'
            ),
        )
        self.assertEqual(
            '<img src="https://png.icons8.com/dusk/icons8.png" alt="Icon of Icons8" class="icon icon-theme-dusk icon-icons8">',
            render_template('{% icon "icons8-t:dusk" renderer="icons8pngcdn" %}'),
        )
        self.assertEqual(
            '<img src="https://png.icons8.com/color/c0392b/icons8.png" alt="Icon of Icons8" class="icon icon-theme-color icon-color-c0392b icon-icons8">',
            render_template('{% icon "icons8-c:c0392b" renderer="icons8pngcdn" %}'),
        )
        self.assertEqual(
            '<img src="https://png.icons8.com/color/96/icons8.png" alt="Icon of Icons8" class="icon icon-theme-color icon-size-96 icon-icons8">',
            render_template('{% icon "icons8-s:96" renderer="icons8pngcdn" %}'),
        )
        self.assertEqual(
            '<div class="icons8-attribution">Icons by&nbsp;<a href="https://icons8.com/"><span><img src="https://png.icons8.com/color/icons8-logo.png" alt="Icons8 icon logo" class="icon icon-theme-color icon-icons8-logo icon-attribution" style="vertical-align:middle; width:1.5rem"><span style="margin-left:0.25rem">Icons8</span></span></a></div>',
            render_template('{% icon-attribution "icons8pngcdn" %}'),
        )
        self.assertEqual(
            '<div class="my-css icons8-attribution">Icons by&nbsp;<a href="https://icons8.com/"><span><img src="https://png.icons8.com/color/icons8-logo.png" alt="Icons8 icon logo" class="icon icon-theme-color icon-icons8-logo icon-attribution" style="vertical-align:middle; width:1.5rem"><span style="margin-left:0.25rem">Icons8</span></span></a></div>',
            render_template(
                '{% icon-attribution "icons8pngcdn" extra_classes="my-css" %}'
            ),
        )

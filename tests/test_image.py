# coding: utf-8
from __future__ import unicode_literals

from django.test import TestCase

from .test_template_tags import render_template


class ImageTest(TestCase):
    """
    Test the Material Design Renderer
    """

    def test_icons(self):
        self.assertEqual(
            render_template('{% icon "icons8-icons8-48" renderer="ImageRenderer" %}'),
            '<img src="/static/icons/icons8-icons8-48.png">',
        )

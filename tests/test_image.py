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
            '<img src="/static/icons/icons8-icons8-48.png" class="icon icon-icons8-icons8-48">',
            render_template('{% icon "icons8-icons8-48" renderer="ImageRenderer" %}'),
        )
        self.assertEqual(
            '<img src="/static/icons/icons8-48.png" class="icon icon-icons8-48">',
            render_template('{% icon "icons8-48" renderer="ImageRenderer" %}'),
        )
        self.assertEqual(
            '<img src="/static/icons/icons8-48.png" class="icon icon-size-48 icon-icons8">',
            render_template('{% icon "icons8-s:48" renderer="ImageRenderer" %}'),
        )
        self.assertEqual(
            '<img src="/static/icons/icons8-b.png" class="icon icon-color-b icon-icons8">',
            render_template('{% icon "icons8-c:b" renderer="ImageRenderer" %}'),
        )
        self.assertEqual(
            '<img src="/static/icons/icons8-b-48.png" class="icon icon-color-b icon-size-48 icon-icons8">',
            render_template('{% icon "icons8-c:b-s:48" renderer="ImageRenderer" %}'),
        )
        self.assertEqual(
            '<img src="/static/icons/icons8-b-48.png" class="icon icon-color-b icon-size-48 icon-icons8">',
            render_template('{% icon "icons8-s:48-c:b" renderer="ImageRenderer" %}'),
        )

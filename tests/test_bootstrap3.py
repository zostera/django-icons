# coding: utf-8
from __future__ import unicode_literals

from django.template import Template, Context
from django.test import TestCase

from .test_template_tags import render_template


class FontAwesomeTest(TestCase):
    """
    Test the Font Awesome Renderer
    """

    def test_icons(self):
        self.assertEqual(
            render_template('{%icon "user" renderer="Bootstrap3Renderer" %}'),
            '<i class="glyphicon glyphicon-user"></i>',
        )

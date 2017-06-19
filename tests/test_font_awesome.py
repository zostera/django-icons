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
            render_template('{%icon "user" size="lg" %}'),
            '<i class="fa fa-user fa-lg"></i>',
        )

# coding: utf-8
from __future__ import unicode_literals

from django.template import Template, Context
from django.test import TestCase


def render_template(content, **context_args):
    """
    Create a template with content ``content`` that first loads the font-awesome tags.
    """
    template = Template("{% load icons %}" + content)
    return template.render(Context(context_args))


class TemplateTagsTest(TestCase):
    """
    Test all template tags
    """

    def test_load_icons(self):
        self.assertHTMLEqual(
            render_template(''),
            '',
        )

    def test_icons(self):
        self.assertHTMLEqual(
            render_template('{%icon "user" %}'),
            '<i class="fa fa-user"></i>',
        )
        self.assertHTMLEqual(
            render_template('{%icon "user" "fa-big" %}'),
            '<i class="fa fa-user fa-big"></i>',
        )
        self.assertHTMLEqual(
            render_template('{%icon "delete" %}'),
            '<i class="fa fa-trash"></i>',
        )
        self.assertHTMLEqual(
            render_template('{%icon "edit" %}'),
            '<i class="fa fa-pencil"></i>',
        )

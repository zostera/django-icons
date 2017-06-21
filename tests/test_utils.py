# coding: utf-8
from __future__ import unicode_literals

from django.test import TestCase

from django_icons.renderers import FontAwesomeRenderer
from django_icons.utils import _get_setting, get_icon_kwargs_from_settings, get_icon_kwargs, \
    get_icon_renderer


class UtilsTest(TestCase):
    """
    Test the Font Awesome Renderer
    """
    pass
    #
    # def test_get_setting(self):
    #     with self.settings(DJANGO_ICONS=None):
    #         self.assertEqual(_get_setting('SECTION', 'name'), None)
    #         self.assertEqual(_get_setting('SECTION', 'name', 'foo'), 'foo')
    #     with self.settings(DJANGO_ICONS={'SECTION': {'name': 'bar'}}):
    #         self.assertEqual(_get_setting('SECTION', 'name'), 'bar')
    #         self.assertEqual(_get_setting('SECTION', 'name', 'foo'), 'bar')

    # def test_get_icon_kwargs_from_settings(self):
    #     with self.settings(DJANGO_ICONS=None):
    #         self.assertEqual(get_icon_kwargs_from_settings('info'), {'name': 'info'})
    #     with self.settings(DJANGO_ICONS={'ICONS': {'info': 'info-sign'}}):
    #         self.assertEqual(get_icon_kwargs_from_settings('info'), {'name': 'info-sign'})
    #     with self.settings(DJANGO_ICONS={'ICONS': {'info': {'name': 'info-sign'}}}):
    #         self.assertEqual(get_icon_kwargs_from_settings('info'), {'name': 'info-sign'})
    #     with self.settings(DJANGO_ICONS={'ICONS': {'info': {'title': 'Information'}}}):
    #         self.assertEqual(get_icon_kwargs_from_settings('info'), {'name': 'info', 'title': 'Information'})
    #
    # def test_get_icon_kwargs(self):
    #     with self.settings(DJANGO_ICONS=None):
    #         self.assertEqual(
    #             get_icon_kwargs('info', 'size-lg color-red'),
    #             {'name': 'info', 'extra_classes': ['size-lg', 'color-red']}
    #         )
    #     with self.settings(DJANGO_ICONS={'ICONS': {'info': 'info-sign'}}):
    #         self.assertEqual(get_icon_kwargs('info'), {'name': 'info-sign'})
    #     with self.settings(DJANGO_ICONS={'ICONS': {'info': {'name': 'info-sign'}}}):
    #         self.assertEqual(get_icon_kwargs('info'), {'name': 'info-sign'})
    #     with self.settings(DJANGO_ICONS={'ICONS': {'info': {'title': 'Information'}}}):
    #         self.assertEqual(get_icon_kwargs('info'), {'name': 'info', 'title': 'Information'})

    # def test_get_default_icon_renderer(self):
    #     with self.settings(DJANGO_ICONS=None):
    #         self.assertEqual(_get_default_icon_renderer(), FontAwesomeRenderer)
    #     with self.settings(DJANGO_ICONS={'DEFAULTS': {}}):
    #         self.assertEqual(_get_default_icon_renderer(), FontAwesomeRenderer)
    #     with self.settings(DJANGO_ICONS={'DEFAULTS': {'renderer': 'foo'}}):
    #         self.assertEqual(_get_default_icon_renderer(), 'foo')
    #     with self.settings(
    #             DJANGO_ICONS={
    #                 'DEFAULTS': {'renderer': 'foo'},
    #                 'RENDERERS': {'foo': FontAwesomeRenderer},
    #             }
    #     ):
    #         self.assertEqual(_get_default_icon_renderer(), 'foo')
    #
    # def test_get_icon_renderer(self):
    #     with self.settings(DJANGO_ICONS=None):
    #         self.assertEqual(get_icon_renderer(), FontAwesomeRenderer)

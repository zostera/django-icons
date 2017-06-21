# coding: utf-8
from __future__ import unicode_literals

from django.test import TestCase

from django_icons.utils import _get_setting, get_icon_kwargs_from_settings


class UtilsTest(TestCase):
    """
    Test the Font Awesome Renderer
    """

    def test_get_setting(self):
        with self.settings(DJANGO_ICONS=None):
            self.assertEqual(_get_setting('SECTION', 'name'), None)
            self.assertEqual(_get_setting('SECTION', 'name', 'foo'), 'foo')
        with self.settings(DJANGO_ICONS={'SECTION': {'name': 'bar'}}):
            self.assertEqual(_get_setting('SECTION', 'name'), 'bar')
            self.assertEqual(_get_setting('SECTION', 'name', 'foo'), 'bar')

    def test_get_icon_kwargs_from_settings(self):
        with self.settings(DJANGO_ICONS=None):
            self.assertEqual(get_icon_kwargs_from_settings('info'), {'name': 'info'})
        with self.settings(DJANGO_ICONS={'ICONS': {'info': 'info-sign'}}):
            self.assertEqual(get_icon_kwargs_from_settings('info'), {'name': 'info-sign'})
        with self.settings(DJANGO_ICONS={'ICONS': {'info': {'name': 'info-sign'}}}):
            self.assertEqual(get_icon_kwargs_from_settings('info'), {'name': 'info-sign'})
        with self.settings(DJANGO_ICONS={'ICONS': {'info': {'title': 'Information'}}}):
            self.assertEqual(get_icon_kwargs_from_settings('info'), {'name': 'info', 'title': 'Information'})

# coding: utf-8
from __future__ import unicode_literals

from django.test import TestCase

from django_icons.css import merge_css_list


class CSSTest(TestCase):
    """
    Test the CSS utilities
    """

    def test_merge_css_list(self):
        # No arguments results in an empty list
        self.assertEqual(
            merge_css_list(),
            [],
        )
        # Falsy arguments are ignores
        self.assertEqual(
            merge_css_list(None, False, ''),
            [],
        )
        # Spaces don't matter without any other results
        self.assertEqual(
            merge_css_list('    '),
            [],
        )
        # Spaces don't matter with other classes
        self.assertEqual(
            merge_css_list('  foo  '),
            ['foo'],
        )
        # Spaces don't matter with other classes
        self.assertEqual(
            merge_css_list('  foo  ', 'bar'),
            ['foo', 'bar'],
        )
        # Space separated classes are split
        self.assertEqual(
            merge_css_list('foo bar'),
            ['foo', 'bar'],
        )
        # Nested lists are fine
        self.assertEqual(
            merge_css_list(['foo', 'bar'], 'end'),
            ['foo', 'bar', 'end'],
        )
        # Duplicates are removed and first time class is encountered determines order
        self.assertEqual(
            merge_css_list(['foo', 'bar'], 'foo'),
            ['foo', 'bar'],
        )
        # Tabs and newlines are valid whitespace
        self.assertEqual(
            merge_css_list('foo\nbar\tend'),
            ['foo', 'bar', 'end'],
        )
        # Let's go crazy
        self.assertEqual(
            merge_css_list(
                'foo\nbar\tend',
                ['foo', ['bar', 'bar', ['foo bar end']]],
                '\n\t foo Foo',
                [[], [], [['Foo-Bar-End']]],
                ('end', 'bar', 'foo', 'Foo'),
            ),
            ['foo', 'bar', 'end', 'Foo', 'Foo-Bar-End'],
        )

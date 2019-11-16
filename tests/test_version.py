from unittest import TestCase

from django_icons import __version__


class VersionTestCase(TestCase):
    def test_version_is_valid(self):
        version_parts = __version__.split(".")
        self.assertEqual(len(version_parts), 3)

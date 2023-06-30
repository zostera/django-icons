from django.test import TestCase


class VersionTest(TestCase):
    """Test the package version."""

    def test_version(self):
        from django_icons import __version__

        parts = __version__.split(".")
        self.assertIn(len(parts), (2, 3))

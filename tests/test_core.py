from django.test import TestCase
from django.utils import translation
from django.utils.translation import gettext_lazy as _

from django_icons import icon
from django_icons.renderers import IconRenderer


class VersionTest(TestCase):
    """Test the IconRenderer."""

    def test_version(self):
        from django_icons import __version__

        parts = __version__.split(".")
        self.assertEqual(len(parts), 2)


class IconFunctionTest(TestCase):
    """Test the icon function."""

    def test_laziness(self):
        self.assertEqual(
            icon("user", title=_("user"), renderer=IconRenderer),
            '<i class="user" title="user"></i>',
        )
        user_icon = icon("user", title=_("user"), renderer=IconRenderer)
        with translation.override("nl"):
            self.assertEqual(user_icon, '<i class="user" title="gebruiker"></i>')

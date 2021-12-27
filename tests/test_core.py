from django.test import TestCase
from django.utils import translation
from django.utils.translation import gettext_lazy as _

from django_icons.core import icon, render_icon
from django_icons.renderers import IconRenderer


class VersionTest(TestCase):
    """Test the package version."""

    def test_version(self):
        from django_icons import __version__

        parts = __version__.split(".")
        self.assertEqual(len(parts), 2)


class RenderIconFunctionTest(TestCase):
    """Test the `render_icon` function."""

    def test_render_icon(self):
        self.assertEqual(
            render_icon("user", title=_("user"), renderer=IconRenderer),
            '<i class="user" title="user"></i>',
        )

    def test_laziness(self):
        user_icon = render_icon("user", title=_("user"), renderer=IconRenderer)
        with translation.override("nl"):
            self.assertEqual(user_icon, '<i class="user" title="gebruiker"></i>')


class IconFunctionTest(TestCase):
    """Test the `icon` function."""

    def test_icon(self):
        with self.assertWarns(DeprecationWarning):
            self.assertEqual(
                icon("user", title=_("user"), renderer=IconRenderer),
                '<i class="user" title="user"></i>',
            )

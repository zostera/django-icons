from django.test import TestCase
from django.utils import translation
from django.utils.translation import gettext_lazy as _

from django_icons import icon
from django_icons.renderers import BaseRenderer


class IconTest(TestCase):
    """Test the icon function."""

    def test_laziness(self):
        self.assertEqual(
            icon("user", title=_("user"), renderer=BaseRenderer),
            '<i class="user" title="user"></i>',
        )
        user_icon = icon("user", title=_("user"), renderer=BaseRenderer)
        with translation.override("nl"):
            self.assertEqual(user_icon, '<i class="user" title="gebruiker"></i>')

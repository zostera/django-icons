from django.test import TestCase, override_settings

from .test_template_tags import render_template


class SettingsContentTest(TestCase):
    """`content` in the ICONS settings accepts one value, a list, or a nested icon."""

    @override_settings(DJANGO_ICONS={"ICONS": {"single": {"content": "one"}}})
    def test_a_single_value_is_wrapped_in_a_list(self):
        self.assertIn("one", render_template('{% icon "single" %}'))

    @override_settings(DJANGO_ICONS={"ICONS": {"many": {"content": ["one", "two"]}}})
    def test_a_list_is_rendered_in_order(self):
        html = render_template('{% icon "many" %}')
        self.assertIn("onetwo", html)

    @override_settings(DJANGO_ICONS={"ICONS": {"nested": {"content": [{"name": "inner"}, "tail"]}}})
    def test_a_dict_entry_is_rendered_as_an_icon(self):
        self.assertHTMLEqual(
            render_template('{% icon "nested" %}'),
            '<i class="nested"><i class="inner"></i>tail</i>',
        )

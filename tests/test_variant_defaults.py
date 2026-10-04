from django.test import TestCase, override_settings

from .test_template_tags import render_template

RENDERER = "tests.app.renderers.CustomVariantDefaultsRenderer"


@override_settings(DJANGO_ICONS={"RENDERERS": {"variant-defaults": RENDERER}})
class VariantAttributeDefaultsTest(TestCase):
    """A variant attribute with a default is filled in when nothing else supplies it."""

    def test_defaults_apply_when_the_name_carries_no_variant(self):
        """Neither variant is in the name, so both fall back to their default."""
        self.assertHTMLEqual(
            render_template('{% icon "icons8" renderer="variant-defaults" %}'),
            '<img src="/static/icons/icons8-black-48.png" alt="Icon of Icons8"'
            ' class="icon icon-color-black icon-size-48 icon-icons8">',
        )

    def test_a_variant_in_the_name_wins_over_its_default(self):
        """Color comes from the name, size still falls back."""
        self.assertHTMLEqual(
            render_template('{% icon "icons8-c:b" renderer="variant-defaults" %}'),
            '<img src="/static/icons/icons8-b-48.png" alt="Icon of Icons8"'
            ' class="icon icon-color-b icon-size-48 icon-icons8">',
        )

    def test_a_keyword_argument_fills_the_rest_from_defaults(self):
        """Passing one variant as a keyword argument puts the other on its default."""
        self.assertHTMLEqual(
            render_template('{% icon "icons8" renderer="variant-defaults" color="red" %}'),
            '<img src="/static/icons/icons8-red-48.png" alt="Icon of Icons8"'
            ' class="icon icon-color-red icon-size-48 icon-icons8">',
        )


class VariantAttributeCacheIsolationTest(TestCase):
    """A subclass must use its own variant patterns, whatever rendered first."""

    def test_a_subclass_does_not_inherit_the_base_class_cache(self):
        from django_icons.renderers import ImageRenderer

        from .app.renderers import CustomVariantDefaultsRenderer

        # Populate the base class cache first. Looking the attribute up through the MRO
        # used to hand the subclass these patterns, defaults and all.
        base = ImageRenderer._get_image_variant_attributes_regex()
        subclass = CustomVariantDefaultsRenderer._get_image_variant_attributes_regex()

        self.assertIsNot(base, subclass)
        self.assertEqual({key: value[1] for key, value in base.items()}, {"color": None, "size": None})
        self.assertEqual({key: value[1] for key, value in subclass.items()}, {"color": "black", "size": "48"})

"""
Minimal smoke test.

This test verifies that the package can be installed and that
its most basic public API is usable. It intentionally avoids
test frameworks and any optional dependencies.
"""


def main():
    import django
    from django.conf import settings

    import django_icons
    from django_icons.renderers import IconRenderer

    # Basic imports work
    assert django.get_version()
    assert hasattr(django_icons, "__version__")

    if not settings.configured:
        settings.configure(
            INSTALLED_APPS=[],
            TEMPLATES=[],
            USE_I18N=False,
            USE_TZ=True,
            SECRET_KEY="django-icons-smoke-test",
        )
        django.setup()

    # One minimal functional call
    assert django_icons.render_icon("user", title="User", renderer=IconRenderer) == '<i class="user" title="User"></i>'


if __name__ == "__main__":
    main()

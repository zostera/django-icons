# Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

## Scope

The goal of this project is icon rendering for Django: define icons in settings (name, title,
and other attributes), render them via template tags, with pluggable renderers for Font
Awesome, Material, Bootstrap 3, images, and custom icon sets via subclassing `IconRenderer`.
Contributions that fit that goal are welcome. Contributions that don't — a general-purpose
templating helper unrelated to icons, a new dependency for a single renderer's sake — are
likely to be closed even if well-implemented, so it's worth opening an issue to discuss scope
before investing time in a pull request.

## Types of Contributions

### Report Bugs

Report bugs at <https://github.com/zostera/django-icons/issues>.

If you are reporting a bug, please include:

- Your operating system name and version.
- Any details about your local setup that might be helpful in troubleshooting.
- Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with "feature" is open to whoever wants to implement it.

### Write Documentation

`django-icons` could always use more documentation, whether as part of the official django-icons docs, in docstrings, or even on the web in blog posts, articles, and such.

### Submit Feedback

The best way to send feedback is to file an issue at
<https://github.com/zostera/django-icons/issues>.

If you are proposing a feature:

- Explain in detail how it would work.
- Keep the scope as narrow as possible, to make it easier to implement.

## Get Started!

Ready to contribute? Here's how to set up `django-icons` for local development.

You will need some knowledge of git, github, and Python/Django development. Using a Python virtual environment is advised.

### Local installation

This package uses [uv](https://github.com/astral-sh/uv) and [just](https://github.com/casey/just).

After installing both, check out this repository and type `just install` to bootstrap a development environment.

```console
git clone git://github.com/zostera/django-icons.git
cd django-icons
just install
```

### Running the tests

To run the tests:

```console
just test
```

To run the tests on all supported Python/Django combinations:

```console
just tests
```

## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. It fits the project's [scope](#scope) — if in doubt, open an issue first.
2. It includes tests for new or changed functionality, and passes all existing tests (`just test`).
3. It doesn't change the rendered markup of an existing renderer unless that's the explicit
   point of the PR — existing users depend on the current output.
4. It doesn't add a new runtime dependency without discussing it in an issue first.
5. If it adds functionality, the docs are updated and the change is added to `CHANGELOG.md`.

Pull requests that don't meet these may be asked for changes, or closed if they've gone stale
without a response — see [MAINTAINING.md](MAINTAINING.md) for how the project handles review
backlog and version support.

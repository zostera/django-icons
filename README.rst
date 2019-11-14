django-icons
------------

Icons for Django

.. image:: https://travis-ci.org/zostera/django-icons.svg?branch=master
    :target: https://travis-ci.org/zostera/django-icons

.. image:: https://coveralls.io/repos/github/zostera/django-icons/badge.svg?branch=develop
   :target: https://coveralls.io/github/zostera/django-icons?branch=develop

.. image:: https://img.shields.io/pypi/v/django-icons.svg
    :target: https://pypi.python.org/pypi/django-icons
    :alt: Latest PyPI version

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/ambv/black

Features
========

Use simple template tags to generate icons in your web application.
Supports *Font Awesome* out of the box, easily adaptable for other icon libraries.

The basic usage in a Django template::

   {% load icons %}
   {% icon 'edit' %}


Requirements
============

Python 3 and matching supported Django versions.


Running the demo
================

You can run the small demo app that is part of the test suite.
This requires Django, so you may have to `pip install django` in your environment.
To run the demo, from the root of the project (where you can find `manage.py`, run::

   python manage.py runserver


Running the tests
=================

The test suite uses `tox`. Run the complete test suite like this::

   tox

Run the tests only for the current environment like this::

   python manage.py test


Origin
======

Our plans at Zostera for an icon tool originate in https://github.com/dyve/django-bootstrap3.
We isolated this into a Font Awesome tool in https://github.com/zostera/django-fa.
When using our own product, we felt that the icon tool provided little improvement over plain HTML.
Also, Font Awesome's icon names did not match the the intended function of the icon. This is how we came
to think of a library that

- Took a limited number of arguments
- Converted those arguments into an icon
- Was able to support multiple icon libraries
- And could easily be extended by users

This is how we came to write and use `django-icons`.

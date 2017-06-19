django-icons
------------

Icons for Django

.. image:: https://coveralls.io/repos/github/zostera/django-icons/badge.svg?branch=develop
   :target: https://coveralls.io/github/zostera/django-icons?branch=develop


Warning
=======

While version < 1 (0.x.y), this project will not be fit for production use, and not adhere to semver.
From 1.0.0 on, `django-icons` will be deemed product ready and semantic versioning will be respected.


Features
========

Use simple template tags to generate icons in your web application.
Supports Font Awesome out of the box, easily adaptable for other icon libraries.

The basic usage is

.. code:: Django

   {% load icons %}
   {% icon 'edit' %}


Requirements
============

Django >= 1.11 and a matching Python version. Using Python 3 is strongly recommended.


Running the tests
=================

The test suite uses `tox`. Run the complete test suite like this:

.. code:: bash

   tox

Run the tests only for the current environment like this:

.. code:: bash

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

django-tinymce
==============

**django-tinymce** is a Django application that contains a widget to render a form field as a TinyMCE editor.

.. image:: https://jazzband.co/static/img/badge.svg
        :target: https://jazzband.co/
        :alt: Jazzband

.. image:: https://img.shields.io/pypi/v/django-tinymce.svg
        :target: https://pypi.python.org/pypi/django-tinymce

.. image:: https://img.shields.io/pypi/pyversions/django-tinymce.svg
        :target: https://pypi.python.org/pypi/django-tinymce

.. image:: https://img.shields.io/pypi/djversions/django-tinymce.svg
        :target: https://pypi.org/project/django-tinymce/

.. image:: https://img.shields.io/pypi/dm/django-tinymce.svg
        :target: https://pypi.python.org/pypi/django-tinymce

.. image:: https://github.com/jazzband/django-tinymce/workflows/Test/badge.svg
   :target: https://github.com/jazzband/django-tinymce/actions
   :alt: GitHub Actions

.. image:: https://codecov.io/gh/jazzband/django-tinymce/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/jazzband/django-tinymce
   :alt: Code coverage


Quickstart
==========

Install django-tinymce:

.. code-block:: bash

    $ pip install django-tinymce

Add tinymce to INSTALLED_APPS in settings.py for your project:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'tinymce',
    )

Add tinymce.urls to urls.py for your project:

.. code-block:: python

    urlpatterns = [
        ...
        path('tinymce/', include('tinymce.urls')),
    ]

In your code:

.. code-block:: python

    from django.db import models
    from tinymce.models import HTMLField

    class MyModel(models.Model):
        ...
        content = HTMLField()

**django-tinymce** uses staticfiles so everything should work as expected, different use cases (like using widget instead of HTMLField) and other stuff is available in documentation.

Releases
========

Latest release is 3.7.1. It supports Python 3.8+ and Django 3.2 to 5.0.

Using TinyMCE 5.10.7.

Previous releases can be found on github, but they are no longer maintained.

Documentation
=============

https://django-tinymce.readthedocs.org/

Support and updates
===================

Use github issues https://github.com/jazzband/django-tinymce/issues

License
=======

Originally written by Joost Cassee.

This program is licensed under the MIT License (see LICENSE.txt)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from distutils.core import setup
from setuptools import setup, find_packages
import metadata

app_name = metadata.name
version = metadata.version

setup(
    name = "django-%s" % app_name,
    version = version,
    packages = find_packages(),
    include_package_data = True,
    author = "Aljosa Mohorovic",
    author_email = "aljosa.mohorovic@gmail.com",
    description = "A Django application that contains a widget to render a" \
            " form field as a TinyMCE editor.",
    long_description = \
"""
django-tinymce
===

**django-tinymce** is a Django application that contains a widget to render a form field as a TinyMCE editor.

Quickstart:
===

Install django-tinymce:

    $ pip install django-tinymce

Add tinymce to INSTALLED_APPS in settings.py for your project:

    INSTALLED_APPS = (
        ...
        'tinymce',
    )

Add tinymce.urls to urls.py for your project:

    urlpatterns = patterns('',
        ...
        (r'^tinymce/', include('tinymce.urls')),
    )

In your code:

    from django.db import models
    from tinymce.models import HTMLField

    class MyModel(models.Model):
        ...
        content = HTMLField()

**django-tinymce** uses staticfiles so everything should work as expected, different use cases (like using widget instead of HTMLField) and other stuff is available in documentation.

Documentation:
===
http://django-tinymce.readthedocs.org/

Support and updates:
===
You can contact me directly at aljosa.mohorovic@gmail.com, track updates at https://twitter.com/maljosa or use github issues.
Be persistent and bug me, I often find myself lost in time so ping me if you're still waiting for me to answer.

License (and related information):
===
Originally written by Joost Cassee.

This program is licensed under the MIT License (see LICENSE.txt)
""",
    license = "MIT License",
    keywords = "django widget tinymce",
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    platforms = ['any'],
    url = "https://github.com/aljosa/django-tinymce",
)

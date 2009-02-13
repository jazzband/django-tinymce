#!/usr/bin/env python

from distutils.core import setup
import metadata

app_name = metadata.name
version = metadata.version

setup(
    name = "django-%s" % app_name,
    version = version,

    packages = [app_name, '%s.templatetags' % app_name],
    package_data = {app_name: ['templates/tinymce/*']},

    author = "Joost Cassee",
    author_email = "joost@cassee.net",
    description = "A Django application that contains a widget to render a" \
            " form field as a TinyMCE editor.",
    long_description = \
"""
Use the TinyMCE editor for your form textareas.

Features:

* Use as a form widget or with a view.
* Enhanced support for content languages.
* Integration with the TinyMCE spellchecker.
* Enables predefined link and image lists for dialogs.
* Can compress the TinyMCE javascript files.
* Integration with django-filebrowser.
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
    url = "http://code.google.com/p/django-%s/" % app_name,
    download_url = "http://code.google.com/p/django-%s/downloads/list" \
            % app_name,
)

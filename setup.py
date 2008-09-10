#!/usr/bin/env python

from distutils.core import setup

app_name = 'tinymce'
version = 'DEV'

setup(
    name = "django-%s" % app_name,
    version = version,

    packages = [app_name],

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
""",
    license = "MIT License",
    keywords = "django widget tinymce",
    classifiers=[
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
    url = "http://code.google.com/p/django-%s/" % app_name,
    download_url = "http://code.google.com/p/django-%s/downloads/list" \
            % app_name,
)

#!/usr/bin/env python
from setuptools import setup, find_packages
import metadata

app_name = metadata.name
version = 'metadata.version'
def read(filename):
    with open(filename) as fp:
        return fp.read()
long_description = read('README.md')

setup(
    name = "fool-django-%s" % app_name,
    version='2.2.3',
    packages = find_packages(),
    include_package_data = True,
    author = "Aljosa Mohorovic",
    author_email = "aljosa.mohorovic@gmail.com",
    description = "A Django application that contains a widget to render a" \
            " form field as a TinyMCE editor.",
    long_description = long_description,
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

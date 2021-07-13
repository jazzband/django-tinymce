#!/usr/bin/env python
import codecs
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

def read_file(filename):
    """Open a related file and return its content."""
    with codecs.open(os.path.join(here, filename), encoding='utf-8') as f:
        content = f.read()
    return content

README = read_file('README.rst')
CHANGELOG = read_file('CHANGELOG.rst')


setup(
    name="gu-django-tinymce",
    version='2.7.2',
    packages=find_packages(exclude="testtinymce"),
    include_package_data=True,
    author="Aljosa Mohorovic",
    author_email="aljosa.mohorovic@gmail.com",
    description=("A Django application that contains a widget to render a "
                 "form field as a TinyMCE editor."),
    long_description=README + "\n\n" + CHANGELOG,
    license="MIT License",
    keywords="django widget tinymce",
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    platforms=['any'],
    url="https://github.com/hu-django/tinymce",
    requires=[
        'django',
        'gu_django_filebrowser_no_grappelli',
    ],
    test_suite='runtests.runtests',
)

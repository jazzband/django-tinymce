#!/usr/bin/env python
from setuptools import setup, find_packages
import metadata

app_name = metadata.name
version = 'metadata.version'
def read(filename):
    with open(filename) as fp:
        return fp.read()


setup(
    name = "fool-django-%s" % app_name,
    url="https://github.com/themotleyfool/django-tinymce",
    author="Aljosa Mohorovic",
    author_email = "aljosa.mohorovic@gmail.com",
    description = "A Django application that contains a widget to render a" \
            " form field as a TinyMCE editor.",
    long_description = "A Django application forked by The Motley Fool that contains a widget to render a" \
            " form field as a TinyMCE editor.",
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
    install_requires=[
    ],
    use_scm_version=True,
    skip_upload_docs=True,
    setup_requires=[
        'setuptools_scm'
    ],
    packages=find_packages(),
    include_package_data=True,

)

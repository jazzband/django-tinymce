#!/usr/bin/env python
import codecs
import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))


def read_file(filename):
    """Open a related file and return its content."""
    with codecs.open(os.path.join(here, filename), encoding="utf-8") as f:
        content = f.read()
    return content


README = read_file("README.rst")
CHANGELOG = read_file("CHANGELOG.rst")


setup(
    name="django-tinymce",
    version="3.0.1",
    packages=find_packages(),
    include_package_data=True,
    author="Aljosa Mohorovic",
    author_email="aljosa.mohorovic@gmail.com",
    description=(
        "A Django application that contains a widget to render a "
        "form field as a TinyMCE editor."
    ),
    long_description=README + "\n\n" + CHANGELOG,
    license="MIT License",
    keywords="django widget tinymce",
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    platforms=["any"],
    url="https://github.com/aljosa/django-tinymce",
    test_suite="runtests.runtests",
)

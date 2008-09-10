from distutils.core import setup

setup(
    name = "django-tinymce",
    version = "DEV",

    packages = ['tinymce'],
    package_data = {'tinymce': ['*.txt']},

    author = "Joost Cassee",
    author_email = "joost@cassee.net",
    description = "A Django application that contains a widget to render a form field as a TinyMCE editor.",
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
    keywords = "django",
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
    url = "http://code.google.com/p/django-tinymce/",
    download_url = "http://django-tinymcel.googlecode.com/files/tinymce-1.0.tar.gz",
)

============
Installation
============

This section describes how to install the django-tinymce application in your Django
project.


.. _prerequisites:

Prerequisites
-------------

The django-tinymce application requires `Django`_ version 1.0 or higher. You will also
need `TinyMCE`_ version 3.0.1 or higher and a `language pack`_ for *every
language* you enabled in ``settings.LANGUAGES``. If you use the `django-filebrowser`_
application in your project, the tinymce application can use it as a browser
when including media.

If you want to use the `spellchecker plugin`_ using the supplied view (no PHP
needed) you must install the `PyEnchant`_ package and dictionaries for your
project languages. Note that the Enchant needs a dictionary that exactly
matches your language codes. For example, a dictionary for code ``'en-us'``
will not automatically be used for ``'en'``. You can check the availability of
the Enchant dictionary for the ``'en'`` language code using the following
Python code::

  import enchant
  enchant.dict_exists('en')

Note that the documentation will use 'TinyMCE' (capitalized) to refer the
editor itself and 'django-tinymce' (lower case) to refer to the Django application.

.. _`Django`: http://www.djangoproject.com/download/
.. _`TinyMCE`: http://tinymce.moxiecode.com/download.php
.. _`language pack`: http://tinymce.moxiecode.com/download_i18n.php
.. _`spellchecker plugin`: http://wiki.moxiecode.com/index.php/TinyMCE:Plugins/spellchecker
.. _`PyEnchant`: http://pythonhosted.org/pyenchant/download.html
.. _`django-filebrowser`: https://github.com/sehmaschine/django-filebrowser

Installation
------------
#. Install django-tinymce using `pip`_ (or any other way to install python package) from `PyPI`_. If you need to use a different way to install django-tinymce you can place the ``tinymce`` module on your Python path. You can put it into your Django project directory or run ``python setup.py install`` from a shell. ::

    pip install django-tinymce

#. Add ``tinymce`` to INSTALLED_APPS in ``settings.py`` for your project::

    INSTALLED_APPS = (
        ...
        'tinymce',
        ...
    )

#. Add ``tinymce.urls`` to ``urls.py`` for your project::

    urlpatterns = patterns('',
        ...
        (r'^tinymce/', include('tinymce.urls')),
        ...
    )

.. _`pip`: http://pip.openplans.org/
.. _`PyPI`: http://pypi.python.org/

Testing
-------

Verify that everything is installed and configured properly:

#. Setup an isolated environment with `virtualenv`_ and activate environment::

    virtualenv --no-site-packages env
    . env/bin/activate

#. Install required packages::

    pip install Django django-tinymce

#. Setup environment variable ``DJANGO_SETTINGS_MODULE``::

    export DJANGO_SETTINGS_MODULE='testtinymce.settings'

#. Create project and change into project directory

    django-admin startproject tinymce_test
    cd tinymce_test

#. Setup test database (it will be created in current folder)::

    python manage.py migrate

#. Create superuser

    python manage.py createsuperuser

#. Run Django runserver command to verify results::

    python manage.py runserver

#. Open this address in a browser::

    http://localhost:8000/admin/testapp/testpage/add/

If you see TinyMCE instead of standard textarea boxes everything is working fine, otherwise check installation steps.

.. _`virtualenv`: http://virtualenv.openplans.org/

.. _configuration:

Configuration
-------------

The application can be configured by editing the project's ``settings.py``
file.

``TINYMCE_JS_URL`` (default: ``settings.MEDIA_URL + 'js/tiny_mce/tiny_mce.js'``)
    The URL of the TinyMCE javascript file::

        TINYMCE_JS_URL = os.path.join(MEDIA_URL, "path/to/tiny_mce/tiny_mce.js")

``TINYMCE_JS_ROOT`` (default: ``settings.MEDIA_ROOT + 'js/tiny_mce'``)
  The filesystem location of the TinyMCE files. It is used by the compressor
  (see below)::

        TINYMCE_JS_ROOT = os.path.join(MEDIA_ROOT, "path/to/tiny_mce")

``TINYMCE_DEFAULT_CONFIG`` (default: ``{'theme': "simple", 'relative_urls': False}``)
  The default TinyMCE configuration to use. See `the TinyMCE manual`_ for all
  options. To set the configuration for a specific TinyMCE editor, see the
  ``mce_attrs`` parameter for the :ref:`widget <widget>`.

``TINYMCE_SPELLCHECKER`` (default: ``False``)
  Whether to use the spell checker through the supplied view. You must add
  ``spellchecker`` to the TinyMCE plugin list yourself, it is not added
  automatically.

``TINYMCE_COMPRESSOR`` (default: ``False``)
  Whether to use the TinyMCE compressor, which gzips all Javascript files into
  a single stream.  This makes the overall download size 75% smaller and also
  reduces the number of requests. The overall initialization time for TinyMCE
  will be reduced dramatically if you use this option.

``TINYMCE_EXTRA_MEDIA`` (default: ``None``)
  Extra media to include on the page with the :ref:`widget <widget>`.

``TINYMCE_FILEBROWSER`` (default: ``True`` if ``'filebrowser'`` is in ``INSTALLED_APPS``, else ``False``)
  Whether to use the django-filebrowser_ as a custom filebrowser for media inclusion.
  See the `official TinyMCE documentation on custom filebrowsers`_.

Example::

  TINYMCE_JS_URL = 'http://debug.example.org/tiny_mce/tiny_mce_src.js'
  TINYMCE_DEFAULT_CONFIG = {
      'plugins': "table,spellchecker,paste,searchreplace",
      'theme': "advanced",
      'cleanup_on_startup': True,
      'custom_undo_redo_levels': 10,
  }
  TINYMCE_SPELLCHECKER = True
  TINYMCE_COMPRESSOR = True
  TINYMCE_EXTRA_MEDIA = {
      'css': {
          'all': [
              ...
          ],
      },
      'js': [
          ...
      ],
  }

.. _`the TinyMCE manual`: http://www.tinymce.com/wiki.php/configuration
.. _`official TinyMCE documentation on custom filebrowsers`: http://www.tinymce.com/wiki.php/TinyMCE3x:How-to_implement_a_custom_file_browser

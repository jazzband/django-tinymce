============
Installation
============

This section describes how to install the django-tinymce application in your Django
project.


.. _prerequisites:

Prerequisites
-------------

The django-tinymce application requires a supported `Django`_ version.
If you use the `django-filebrowser`_ application in your project, the tinymce
application can use it as a browser when including media.

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

.. _`Django`: https://www.djangoproject.com/download/
.. _`TinyMCE`: https://www.tiny.cloud/get-tiny/
.. _`language pack`: https://www.tiny.cloud/get-tiny/language-packages/
.. _`spellchecker plugin`: https://www.tiny.cloud/docs/plugins/spellchecker/
.. _`PyEnchant`: https://pyenchant.github.io/pyenchant/install.html
.. _`django-filebrowser`: https://github.com/sehmaschine/django-filebrowser

Installation
------------
#. Install django-tinymce using `pip`_ (or any other way to install python package) from `PyPI`_. If you need to use a different way to install django-tinymce you can place the ``tinymce`` module on your Python path. ::

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
        path('tinymce/', include('tinymce.urls')),
        ...
    )

.. _`pip`: https://pip.pypa.io/
.. _`PyPI`: https://pypi.org/

Testing
-------

Verify that everything is installed and configured properly:

#. Setup an isolated environment with `virtualenv`_ and activate environment::

    virtualenv --no-site-packages env
    . env/bin/activate

#. Install required packages::

    pip install Django django-tinymce

#. Setup environment variable ``DJANGO_SETTINGS_MODULE``::

    export DJANGO_SETTINGS_MODULE='tests.settings'

#. Create project and change into project directory::

    django-admin startproject tinymce_test
    cd tinymce_test

#. Setup test database (it will be created in current folder)::

    python manage.py migrate

#. Create superuser (follow the prompts)::

    python manage.py createsuperuser

#. Run Django runserver command to verify results::

    python manage.py runserver

#. Open this address in a browser::

    http://localhost:8000/admin/testapp/testpage/add/

If you see TinyMCE instead of standard textarea boxes everything is working fine, otherwise check installation steps.

.. _`virtualenv`: https://virtualenv.pypa.io/

.. _configuration:

Configuration
-------------

The application can be configured by editing the project's ``settings.py``
file.

``TINYMCE_JS_URL`` (default: ``settings.STATIC_URL + 'tinymce/tinymce.min.js'``)
  The URL of the TinyMCE javascript file::

        TINYMCE_JS_URL = os.path.join(STATIC_URL, "path/to/tiny_mce/tiny_mce.js")

``TINYMCE_DEFAULT_CONFIG``
  The default TinyMCE configuration to use. See `the TinyMCE manual`_ for all
  options. To set the configuration for a specific TinyMCE editor, see the
  ``mce_attrs`` parameter for the :ref:`widget <widget>`.
  !Important: The ``language`` attribute should only be set to force TinyMCE to
  have a different language than Django's current active language.

  If not set, the default value of this setting is::


    {
        "theme": "silver",
        "height": 500,
        "menubar": False,
        "plugins": "advlist,autolink,lists,link,image,charmap,print,preview,anchor,"
        "searchreplace,visualblocks,code,fullscreen,insertdatetime,media,table,paste,"
        "code,help,wordcount",
        "toolbar": "undo redo | formatselect | "
        "bold italic backcolor | alignleft aligncenter "
        "alignright alignjustify | bullist numlist outdent indent | "
        "removeformat | help",
    }


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
      "height": "320px",
      "width": "960px",
      "menubar": "file edit view insert format tools table help",
      "plugins": "advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code "
      "fullscreen insertdatetime media table paste code help wordcount spellchecker",
      "toolbar": "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft "
      "aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor "
      "backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | "
      "fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | "
      "a11ycheck ltr rtl | showcomments addcomment code",
      "custom_undo_redo_levels": 10,
      "language": "es_ES",  # To force a specific language instead of the Django current language.
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

.. _`the TinyMCE manual`: https://www.tiny.cloud/docs/general-configuration-guide/
.. _`official TinyMCE documentation on custom filebrowsers`: https://www.tiny.cloud/docs/configure/file-image-upload/#file_picker_callback

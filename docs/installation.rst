============
Installation
============

This section describes how to install the tinymce application in your Django project.

Prerequisites
-------------

The tinymce application requires Django_ version 1.0 or higher. You will also need TinyMCE_ version 3.0 or higher and optionally a `language pack`_ for your projects languages. If you want to use the `spellchecker plugin`_ using the supplied view (no PHP needed) you must install the `PyEnchant`_ package and dictionaries for your project languages.

.. _Django: http://www.djangoproject.com/download/
.. _TinyMCE: http://tinymce.moxiecode.com/download.php
.. _`language pack`: http://tinymce.moxiecode.com/download_i18n.php
.. _`spellchecker plugin`: http://wiki.moxiecode.com/index.php/TinyMCE:Plugins/spellchecker
.. _`PyEnchant`: http://pyenchant.sourceforge.net/

Installation
------------

#. Place the ``tinymce`` module in your Python path. You could put it into your Django project directory or run ``python setup.py install`` from a shell.)

#. Copy the ``jscripts/tiny_mce`` directory from the TinyMCE distribution into a directory named ``js`` in your media root. You can override the location in your settings (see below).

#. If you want to use the TinyMCE compressor, copy ``media/tiny_mce_gzip.js`` from the ``tinymce`` module into the same directory as ``tiny_mce.js`` from the previous step.

#. If you want to use any of the views add tinymce your installed applications list and URLconf:

``settings.py``::

  INSTALLED_APPS = (
      ...
      'tinymce',
      ...
  )

``urls.py``::

  urlpatterns = patterns('',
      ...
      (r'^tinymce/', include('tinymce.urls')),
      ...
  )

Configuration
-------------

The application can be configured by editing the project's ``settings.py`` file.

``TINYMCE_JS_URL`` (default: ``settings.MEDIA_URL + 'js/tiny_mce/tiny_mce.js'``)
  The URL of the TinyMCE javascript file.

``TINYMCE_DEFAULT_CONFIG`` (default: ``{'theme': "simple"}``)
  The default TinyMCE configuration to use. See `the TinyMCE manual`_ for all options.

``TINYMCE_SPELLCHECKER`` (default: ``False``)
  Whether to use the spell checker through the supplied view. You must add ``spellchecker`` to the plugin list yourself, it is not added automatically.

``TINYMCE_COMPRESSOR`` (default: ``False``)
  Whether to use the TinyMCE compressor, which gzips all Javascript files into a single stream.  This makes the overall download size 75% smaller and also reduces the number of requests. The overall initialization time for TinyMCE will be reduced dramatically if you use this option.

Example::

  TINYMCE_JS_URL = 'http://debug.example.org/tiny_mce/tiny_mce_src.js'
  TINYMCE_DEFAULT_CONFIG = {
      'plugins': "table,spellchecker,paste,searchreplace",
      'theme': "advanced",
  }
  TINYMCE_SPELLCHECKER = True
  TINYMCE_COMPRESSOR = True

.. _`the TinyMCE manual`: http://wiki.moxiecode.com/index.php/TinyMCE:Configuration


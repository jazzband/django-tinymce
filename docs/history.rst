=========
History
=========

Changelog
---------

Release 1.5 (2009-02-13):
  * Updated Google Code CSS location.
  * Fixed a compressor crash when 'theme' configuration was omitted.
  * Added a note in the documentation about Python-JSON type conversion.
  * Fixed the filebrowser integration when serving media from a different
    domain.
  * Fixed flatpages example code in documentation.
  * Added support for the preview plugin.
  * Added "'relative_urls': False" to the default settings to fix integration
    with django-filebrowser.

Release 1.4 (2009-01-28):
  * Fixed bugs in compressor code causing it not to load.
  * Fixed widget media property.

Release 1.3 (2009-01-15):
  * Added integration with `django-filebrowser`_.
  * Added templates to source distribution.
  * Updated TinyMCE compressor support: copying media files no longer required.

.. _`django-filebrowser`: http://code.google.com/p/django-filebrowser/

Release 1.2 (2008-11-26):
  * Moved documentation from Wiki into repository.

Release 1.1 (2008-11-20):
  * Added TinyMCE compressor support by Jason Davies.
  * Added HTMLField.

Release 1.0 (2008-09-10):
  * Added link and image list support.
  * Moved from private repository to Google Code.


Credits
-------

tinymce was written by `Joost Cassee`_ based on the work by John D'Agostino. It
was partly taken from `his code at the Django code wiki`_. The TinyMCE_
Javascript WYSIWYG editor is made by Moxiecode_.

The TinyMCE compressor was written by `Jason Davies`_ based on the `PHP TinyMCE
compressor`_ from Moxiecode.


.. _`Joost Cassee`: http://joost.cassee.net/
.. _TinyMCE: http://tinymce.moxiecode.com/
.. _Moxiecode: http://www.moxiecode.com/
.. _`his code at the Django code wiki`: http://code.djangoproject.com/wiki/CustomWidgetsTinyMCE
.. _`Jason Davies`: http://www.jasondavies.com
.. _`PHP TinyMCE compressor`: http://wiki.moxiecode.com/index.php/TinyMCE:Compressor

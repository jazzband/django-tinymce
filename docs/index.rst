Welcome to the django-tinymce documentation
===========================================

django-tinymce is a Django_ application that contains a widget to render a form field
as a TinyMCE_ editor.

Features:
  * Use as a form widget or with a view.
  * Enhanced support for content languages.
  * Integration with the TinyMCE spellchecker.
  * Enables predefined link and image lists for dialogs.
  * Support for django-staticfiles
  * Can compress the TinyMCE Javascript code.
  * Integration with `django-filebrowser`_.

The django-tinymce code is licensed under the `MIT License`_. See the ``LICENSE.txt``
file in the distribution. Note that the TinyMCE editor is distributed under
`its own license`_.

Starting with django-tinymce v1.5.1 TinyMCE editor is bundled with django-tinymce to enable easy installation and usage.
`django-staticfiles`_ support is added to provide an easier way to configure and use django-tinymce.
Note that django-tinymce and TinyMCE licenses are compatible (although different) and we have permission to bundle TinyMCE with django-tinymce.

.. _Django: http://www.djangoproject.com/
.. _TinyMCE: http://tinymce.moxiecode.com/
.. _`django-staticfiles`: http://pypi.python.org/pypi/django-staticfiles/
.. _`django-filebrowser`: http://code.google.com/p/django-filebrowser/
.. _`MIT License`: http://www.opensource.org/licenses/mit-license.php
.. _`its own license`: http://tinymce.moxiecode.com/license.php

Documentation
-------------

.. toctree::
   :maxdepth: 2

   installation
   usage
   history


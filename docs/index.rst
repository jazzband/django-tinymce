Welcome to the django-tinymce documentation
===========================================

django-tinymce is a Django_ application that contains a widget to render a form field
as a TinyMCE_ editor.


Quickstart
----------

Make sure `staticfiles`_ application is properly configured (TinyMCE is bundled with django-tinymce and uses staticfiles to automatically serve TinyMCE files).

#. Install django-tinymce using `pip`_ (or any other way to install python package) from `PyPI`_. ::

    $ pip install django-tinymce

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

#. Use ``HTMLField`` where you would use ``TextField`` (or check Usage for alternatives). ::

    from django.db import models
    from tinymce.models import HTMLField

    class MyModel(models.Model):
        my_field = HTMLField()

The django-tinymce code is licensed under the `MIT License`_. See the ``LICENSE.txt``
file in the distribution. Note that the TinyMCE editor is distributed under
`its own license`_.
Note that django-tinymce and TinyMCE licenses are compatible (although different) and we have permission to bundle TinyMCE with django-tinymce.

.. _`staticfiles`: https://docs.djangoproject.com/en/1.6/ref/settings/#settings-staticfiles
.. _`pip`: http://pip.openplans.org/
.. _`PyPI`: http://pypi.python.org/
.. _Django: http://www.djangoproject.com/
.. _TinyMCE: http://tinymce.moxiecode.com/
.. _`MIT License`: http://www.opensource.org/licenses/mit-license.php
.. _`its own license`: http://tinymce.moxiecode.com/license.php

Documentation
-------------

.. toctree::
   :maxdepth: 2

   installation
   usage
   history


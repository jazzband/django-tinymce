django-tinymce
==============

**django-tinymce** is a Django application that contains a widget to render a form field as a TinyMCE editor.

WARNING
=======
v3.0 uses TinyMCE v4.x and is not backwards compatible w/ previous versions.

Quickstart
==========

Install requirements:

    $ pip install -r requirements.txt

Install django-tinymce:

.. code-block::

    $ pip install django-tinymce

Add tinymce to INSTALLED_APPS in settings.py for your project:

.. code-block::

    INSTALLED_APPS = (
        ...
        'tinymce',
    )

Add tinymce.urls to urls.py for your project:

.. code-block::

    urlpatterns = patterns('',
        ...
        (r'^tinymce/', include('tinymce.urls')),
    )

In your code:

.. code-block::

    from django.db import models
    from tinymce.models import HTMLField

    class MyModel(models.Model):
        ...
        content = HTMLField()

**django-tinymce** uses staticfiles so everything should work as expected, different use cases (like using widget instead of HTMLField) and other stuff is available in documentation.

Documentation
=============

http://django-tinymce.readthedocs.org/

Support and updates
===================

You can contact me directly at aljosa.mohorovic@gmail.com, track
updates at https://twitter.com/maljosa or use github issues.  Be
persistent and bug me, I often find myself lost in time so ping me if
you're still waiting for me to answer.

License
=======

Originally written by Joost Cassee.

This program is licensed under the MIT License (see LICENSE.txt)

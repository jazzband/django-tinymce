=====
Usage
=====

The application can enable TinyMCE for one form field using the ``widget``
keyword argument of ``Field`` constructors or for all textareas on a page using
a view.


.. _widget:

Using the widget
----------------

If you use the widget (recommended) you need to add some python code and
possibly modify your template.

Python code
^^^^^^^^^^^

The TinyMCE widget can be enabled by setting it as the widget for a formfield.
For example, to use a nice big TinyMCE widget for the content field of a
flatpage form you could use the following code::

  from django import forms
  from django.contrib.flatpages.models import FlatPage
  from tinymce.widgets import TinyMCE

  class FlatPageForm(forms.ModelForm):
      ...
      content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
      ...

      class Meta:
          model = FlatPage

The widget accepts the following extra keyword argument:

``mce_attrs`` (default: ``{}``)
  Extra TinyMCE configuration options. Options from
  ``settings.TINYMCE_DEFAULT_CONFIG`` (see :ref:`configuration`) are applied
  first and can be overridden.
  Python types are automatically converted to Javascript types, using standard
  JSON encoding. For example, to disable word wrapping you would include
  ``'nowrap': True``.

The tinymce application adds one TinyMCE configuration option that can be set
using ``mce_attrs`` (it is not useful as a default configuration):

``content_language`` (default: ``django.utils.translation.get_language_code()``)
  The language of the widget content. Will be used to set the ``language``,
  ``directionality`` and ``spellchecker_languages`` configuration options of
  the TinyMCE editor. It may be different from the interface language, which
  defaults to the current Django language and can be changed using the
  ``language`` configuration option in ``mce_attrs``)

Templates
^^^^^^^^^

The widget requires a link to the TinyMCE javascript code. The
``django.contrib.admin`` templates do this for you automatically, so if you are
just using tinymce in admin forms then you are done. In your own templates
containing a TinyMCE widget you must add the following to the HTML ``HEAD``
section (assuming you named your form 'form')::

  <head>
      ...
      {{ form.media }}
  </head>

See also `the section of form media`_ in the Django documentation.

.. _`the section of form media`: http://www.djangoproject.com/documentation/forms/#media-on-forms

The ``HTMLField`` model field type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For lazy developers the tinymce application also contains a model field type
for storing HTML. It uses the TinyMCE widget to render its form field. In this
example, the admin will render the ``my_field`` field using the TinyMCE
widget::

  from django.db import models
  from tinymce import models as tinymce_models

  class MyModel(models.Model):
      my_field = tinymce_models.HTMLField()

In all other regards, ``HTMLField`` behaves just like the standard Django
``TextField`` field type.

Using the view
--------------

If you cannot or will not change the widget on a form you can also use the
``tinymce-js`` named view to convert some or all textfields on a page to
TinyMCE editors. On the template of the page, add the following lines to the
``HEAD`` element::

  <script type="text/javascript" src="{{ STATIC_URL }}js/tiny_mce/tiny_mce.js"></script>
  <script type="text/javascript" src="{% url "tinymce-js" "NAME" %}"></script>

The use of ``STATIC_URL`` needs the
``django.core.context_processors.static`` context processors.

You may want to use``{% static %}`` instead like::

  <script type="text/javascript" src="{% static "js/tiny_mce/tiny_mce.js" %}"></script>
  <script type="text/javascript" src="{% url "tinymce-js" "NAME" %}"></script>

Be careful that some ``STATICFILES_STORAGE`` will modify your
``tiny_mce.js`` file name and your file will fail to load.

The ``NAME`` argument allows you to create multiple TinyMCE configurations. Now
create a template containing the Javascript initialization code. It should be
placed in the template path as ``NAME/tinymce_textareas.js`` or
``tinymce/NAME_textareas.js``.

Example::

  tinyMCE.init({
      mode: "textareas",
      theme: "advanced",
      plugins: "spellchecker,directionality,paste,searchreplace",
      language: "{{ language }}",
      directionality: "{{ directionality }}",
      spellchecker_languages : "{{ spellchecker_languages }}",
      spellchecker_rpc_url : "{{ spellchecker_rpc_url }}"
  });

This example also shows the variables you can use in the template. The language
variables are based on the current Django language. If the content language is
different from the interface language use the ``tinymce-js-lang`` view which
takes a language (``LANG_CODE``) argument::

  <script type="text/javascript" src="{% url "tinymce-js-lang" "NAME","LANG_CODE" %}"></script>


External link and image lists
-----------------------------

The TinyMCE link and image dialogs can be enhanced with a predefined list of
links_ and images_. These entries are filled using a variable loaded from an
external Javascript location. The tinymce application can serve these lists for
you.

.. _links: http://www.tinymce.com/wiki.php/Configuration:link_list
.. _images: http://www.tinymce.com/wiki.php/Configuration:image_list

Creating external link and image views
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To use a predefined link list, add the ``external_link_list_url`` option to the
``mce_attrs`` keyword argument to the widget (or the template if you use the
view). The value is a URL that points to a view that fills a list of 2-tuples
(*name*, *URL*) and calls ``tinymce.views.render_to_link_list``. For example:

Create the widget::

  from django import forms
  from django.core.urlresolvers import reverse
  from tinymce.widgets import TinyMCE

  class SomeForm(forms.Form):
      somefield = forms.CharField(widget=TinyMCE(mce_attrs={'external_link_list_url': reverse('someviewname')})

Create the view::

  from tinymce.views import render_to_link_list

  def someview(request):
      objects = ...
      link_list = [(unicode(obj), obj.get_absolute_url()) for obj in objects]
      return render_to_link_list(link_list)

Finally, include the view in your URLconf.

Image lists work exactly the same way, just use the TinyMCE
``external_image_list_url`` configuration option and call
``tinymce.views.render_to_image_list`` from your view.

The ``flatpages_link_list`` view
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As an example, the tinymce application contains a predefined view that lists
all ``django.contrib.flatpages`` objects:
``tinymce.views.flatpages_link_list``. If you want to use a TinyMCE widget for
the flatpages ``content`` field with a predefined list of other flatpages in
the link dialog you could use something like this::

  from django import forms
  from django.core.urlresolvers import reverse
  from django.contrib.flatpages.admin import FlatPageAdmin
  from django.contrib.flatpages.models import FlatPage
  from tinymce.widgets import TinyMCE

  class TinyMCEFlatPageAdmin(FlatPageAdmin):
      def formfield_for_dbfield(self, db_field, **kwargs):
          if db_field.name == 'content':
              return db_field.formfield(widget=TinyMCE(
                  attrs={'cols': 80, 'rows': 30},
                  mce_attrs={'external_link_list_url': reverse('tinymce-linklist')},
              ))
          return super(TinyMCEFlatPageAdmin, self).formfield_for_dbfield(db_field, **kwargs)

  somesite.register(FlatPage, TinyMCEFlatPageAdmin)

If you want to enable this for the default admin site
(``django.contrib.admin.site``) you will need to unregister the original
ModelAdmin class for flatpages first::

  from django.contrib import admin

  admin.site.unregister(FlatPage)
  admin.site.register(FlatPage, TinyMCEFlatPageAdmin)

The source contains a `test project`_ that includes this flatpages model admin.
You just need to add the TinyMCE javascript code.

#. Checkout the test project:
   ``svn checkout http://django-tinymce.googlecode.com/svn/trunk/testtinymce``
#. Copy the ``tiny_mce`` directory from the TinyMCE distribution into
   ``media/js``
#. Run ``python manage.py syncdb``
#. Run ``python manage.py runserver``
#. Connect to `http://localhost:8000/admin/`_

.. _`test project`: http://code.google.com/p/django-tinymce/source/browse/trunk/testproject/
.. _`http://localhost:8000/admin/`: http://localhost:8000/admin/


The TinyMCE preview button
--------------------------

TinyMCE contains a `preview plugin`_ that can be used to allow the user to view
the contents of the editor in the website context. The tinymce application
provides a view and a template tag to make supporting this plugin easier. To
use it point the ``plugin_preview_pageurl`` configuration to the view named
``tinymce-preview``::

  from django.core.urlresolvers import reverse
  widget = TinyMCE(mce_attrs={'plugin_preview_pageurl': reverse('tinymce-preview', "NAME")})

The view named by ``tinymce-preview`` looks for a template named either
``tinymce/NAME_preview.html`` or ``NAME/tinymce_preview.html``. The template
accesses the content of the TinyMCE editor by using the ``tinymce_preview``
tag::

  {% load tinymce_tags %}
  <html>
  <head>
  ...
  {% tinymce_preview "preview-content" %}
  </head>
  <body>
  ...
  <div id="preview-content"></div>
  ...

With this template code the text inside the HTML element with id
``preview-content`` will be replaced by the content of the TinyMCE editor.

.. _`preview plugin`: http://wiki.moxiecode.com/index.php/TinyMCE:Plugins/preview

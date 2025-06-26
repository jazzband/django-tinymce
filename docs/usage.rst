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

        class Meta:
            model = FlatPage
            widgets = {'content': TinyMCE(attrs={'cols': 80, 'rows': 30})}

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
  The language of the widget content. Will be used to set the ``language`` and
  ``directionality`` configuration options of the TinyMCE editor. It may be
  different from the interface language, which defaults to the current Django
  language and can be changed using the ``language`` configuration option in
  ``mce_attrs``.

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

.. _`the section of form media`: https://docs.djangoproject.com/en/stable/topics/forms/media/

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

    <script src="{{ STATIC_URL }}js/tiny_mce/tiny_mce.js"></script>
    <script src="{% url "tinymce-js" "NAME" %}"></script>

The use of ``STATIC_URL`` needs the
``django.core.context_processors.static`` context processors.

You may want to use ``{% static %}`` instead like::

    <script src="{% static "js/tiny_mce/tiny_mce.js" %}"></script>
    <script src="{% url "tinymce-js" "NAME" %}"></script>

Be careful that some ``STATICFILES_STORAGE`` will modify your
``tiny_mce.js`` file name and your file will fail to load.

The ``NAME`` argument allows you to create multiple TinyMCE configurations. Now
create a template containing the Javascript initialization code. It should be
placed in the template path as ``NAME/tinymce_textareas.js`` or
``tinymce/NAME_textareas.js``.

Example::

    tinyMCE.init({
        mode: "textareas",
        theme: "silver",
        plugins: "directionality,searchreplace",
        language: "{{ language }}",
        directionality: "{{ directionality }}",
    });

This example also shows the variables you can use in the template. The language
variables are based on the current Django language. If the content language is
different from the interface language use the ``tinymce-js-lang`` view which
takes a language (``LANG_CODE``) argument::

    <script src="{% url "tinymce-js-lang" "NAME","LANG_CODE" %}"></script>

External link and image lists
------------------------------

The TinyMCE link and image dialogs can be enhanced with a predefined list of
links_ and images_. These entries are configured using the ``link_list`` and
``image_list`` options. These options must point to a URL that returns JSON
data.

.. _links: https://www.tiny.cloud/docs/plugins/link/#link_list
.. _images: https://www.tiny.cloud/docs/plugins/image/#image_list

Example JSON response
^^^^^^^^^^^^^^^^^^^^^

Each URL must return a JSON array of objects with ``title`` and ``value`` fields, for example::

    [
      {"title": "My Page 1", "value": "https://example.com/page1"},
      {"title": "My Page 2", "value": "https://example.com/page2"}
    ]

Example Usage
^^^^^^^^^^^^^

To use a predefined link list::

    from django import forms
    from django.urls import reverse
    from tinymce.widgets import TinyMCE

    class SomeForm(forms.Form):
        somefield = forms.CharField(
            widget=TinyMCE(mce_attrs={'link_list': reverse('someviewname')})
        )

Example view for links::

    from django.http import JsonResponse

    def someview(request):
        objects = ...
        link_list = [{"title": str(obj), "value": obj.get_absolute_url()} for obj in objects]
        return JsonResponse(link_list, safe=False)

Similarly, for images::

    somefield = forms.CharField(
        widget=TinyMCE(mce_attrs={'image_list': reverse('someimageview')})
    )

Legacy Options
^^^^^^^^^^^^^^

Previous versions of TinyMCE used ``external_link_list_url`` and ``external_image_list_url``, and required using ``tinymce.views.render_to_link_list`` or ``tinymce.views.render_to_image_list``. These are no longer supported by recent TinyMCE versions and will not work.

If you have old code referring to ``external_link_list_url`` or ``external_image_list_url``, you must update it to use ``link_list`` and ``image_list`` as shown above.

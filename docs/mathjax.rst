MathJax 3 Support
===============

Django-tinymce comes bundled with a MathJax plugin based on https://github.com/dimakorotkov/tinymce-mathjax
that enables LaTeX in both inline and display mode. The MathJax 3 library is bundles with the plugin and needs
to be imported and configured anywhere the content is rendered or edited. You may enable the plugin as follows.

In ``settings.py``::

    TINYMCE_DEFAULT_CONFIG = {...
                                "external_plugins": {'mathjax': 'plugins/mathjax/plugin.min.js'},
                                "toolbar": "...all your other toolbar stuff...| mathjax",
                              ...}

On any page which will display your content, or which has your TinyMCE widget, you must include script tags to import
and configure the MathJax library like so::

     <script type="text/javascript">
        MathJax = {
            tex: {
                inlineMath: [['$', '$'], ['\\(', '\\)']]
            }
        };
     </script>
     <script type="text/javascript" async defer src="{% static 'plugins/mathjax/mathjax.min.js' %}"></script>

Please respect the ordering, the configuration script tag must precede the MathJax import, or inline mode will not
be enabled. If you wish to apply additional MathJax configuration options, you may edit the configuration script tag
appropriately. Please note that MathJax is configured differently depending upon which version you are using, so make
sure any documentation you follow is for version 3.

If you are using the admin to edit your content, one suggested way to include the MathJax tags would be to override
the admin ``change_form.html`` for your model according to the 'Overriding admin templates' section of
https://docs.djangoproject.com/en/dev/ref/contrib/admin/ to something like this::

    {% extends "admin/change_form.html" %}
    {% load i18n admin_urls static admin_modify %}
    {% block admin_change_form_document_ready %}
        {{ block.super }}
        <script type="text/javascript">
            MathJax = {
                tex: {
                    inlineMath: [['$', '$'], ['\\(', '\\)']]
                }
            };
        </script>
        <script type="text/javascript" async defer src="{% static 'plugins/mathjax/mathjax.min.js' %}"></script>
    {% endblock %}


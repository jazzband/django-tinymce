# Copyright (c) 2008 Joost Cassee
# Licensed under the terms of the MIT License (see LICENSE.txt)

from django.db import models
from django.contrib.admin import widgets as admin_widgets
from tinymce import widgets as tinymce_widgets
try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ['^tinymce\\.models\\.HTMLField'])
except ImportError:
    pass


class HTMLField(models.TextField):
    """
    A large string field for HTML content. It uses the TinyMCE widget in
    forms.
    """
    def formfield(self, **kwargs):
        defaults = {'widget': tinymce_widgets.TinyMCE}
        defaults.update(kwargs)

        # As an ugly hack, we override the admin widget
        if defaults['widget'] == admin_widgets.AdminTextareaWidget:
            defaults['widget'] = tinymce_widgets.AdminTinyMCE

        return super(HTMLField, self).formfield(**defaults)

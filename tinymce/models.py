# Copyright (c) 2008 Joost Cassee
# Licensed under the terms of the MIT License (see LICENSE.txt)

from django.contrib.admin import widgets as admin_widgets
from django.db import models

from tinymce import widgets as tinymce_widgets


class HTMLField(models.TextField):
    """
    A large string field for HTML content. It uses the TinyMCE widget in
    forms.
    """

    def formfield(self, **kwargs):
        defaults = {"widget": tinymce_widgets.TinyMCE}
        defaults.update(kwargs)

        # As an ugly hack, we override the admin widget
        if defaults["widget"] == admin_widgets.AdminTextareaWidget:
            defaults["widget"] = tinymce_widgets.AdminTinyMCE

        return super().formfield(**defaults)

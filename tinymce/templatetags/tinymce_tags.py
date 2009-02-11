# Copyright (c) 2009 Joost Cassee
# Licensed under the terms of the MIT License (see LICENSE.txt)

from django import template
from django.template.loader import render_to_string
import tinymce.settings

register = template.Library()


def tinymce_preview(element_id):
    return render_to_string('tinymce/preview_javascript.html',
        {'base_url': tinymce.settings.JS_BASE_URL, 'element_id': element_id})

register.simple_tag(tinymce_preview)

# coding: utf-8

from __future__ import absolute_import, unicode_literals

import json

from django import forms

from .conf import settings


class TinyMCE(forms.Textarea):

    def __init__(self, attrs=None, mce_attrs=None, **kwargs):
        super(TinyMCE, self).__init__(attrs)
        self.mce_attrs = mce_attrs or {}

    def build_attrs(self, extra_attrs=None, **kwargs):
        """Add tinymce data attributes."""
        attrs = super(TinyMCE,
                      self).build_attrs(extra_attrs=extra_attrs, **kwargs)

        if 'class' in attrs:
            attrs['class'] += ' django-tinymce'
        else:
            attrs['class'] = 'django-tinymce'

        tinymce_confing = settings.TINYMCE_CONFIG
        tinymce_confing.update(self.mce_attrs)
        attrs['data-django-tinymce-config'] = json.dumps(tinymce_confing)

        return attrs

    def _get_media(self):
        """
        Construct Media as a dynamic property.
        .. Note:: For more information visit
            https://docs.djangoproject.com/en/1.8/topics/forms/media/#media-as-a-dynamic-property
        """
        js = [settings.TINYMCE_JS, 'django_tinymce/django_tinymce.js']
        js += settings.TINYMCE_EXTRA_MEDIA['js']
        css = settings.TINYMCE_EXTRA_MEDIA['css']
        return forms.Media(
            js=js,
            css=css,
        )

    media = property(_get_media)

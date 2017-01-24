# coding: utf-8
"""Settings for Django-TinyMCE."""
from __future__ import absolute_import, unicode_literals

from appconf import AppConf
from django.conf import settings  # NOQA

__all__ = ('settings', 'TinyMCEConf')


class TinyMCEConf(AppConf):
    """Settings for Django-TinyMCE."""

    JS = '//cdn.tinymce.com/4/tinymce.min.js'
    """
    The URI for the TinyMCE JS file. By default this points to the TinyMCE CDN.
    If you want to select the version of the JS library used,
    or want to serve it from the local 'static' resources,
    add a line to your settings.py like so::
        TinyMCE_JS = 'assets/js/tinymce.min.js'
    .. tip:: Change this setting to a local asset
        in your development environment to
        develop without an Internet connection.
    """

    CONFIG = {
        'selector': '.django-tinymce',
        'theme': 'modern',
        'relative_urls': False
    }

    EXTRA_MEDIA = {
        'js': [],
        'css': {},
    }

    class Meta:
        prefix = 'TinyMCE'

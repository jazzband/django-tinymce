"""
Based on "TinyMCE Compressor PHP" from MoxieCode.

http://tinymce.moxiecode.com/

Copyright (c) 2008 Jason Davies
Licensed under the terms of the MIT License (see LICENSE.txt)
"""

from datetime import datetime
import os
import re
import json

from django.conf import settings
from django.core.cache import cache
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.text import compress_string
from django.utils.cache import patch_vary_headers, patch_response_headers
from django.utils.encoding import smart_text
from django.utils.http import http_date

import tinymce.settings

safe_filename_re = re.compile('^[a-zA-Z][a-zA-Z0-9_/-]*$')


def get_file_contents(filename):
    if 'staticfiles' in settings.INSTALLED_APPS or \
       'django.contrib.staticfiles' in settings.INSTALLED_APPS:
        from django.contrib.staticfiles import finders
        file_path = finders.find(os.path.join('tiny_mce', filename))
    else:
        file_path = os.path.join(tinymce.settings.JS_ROOT, filename)

    try:
        f = open(file_path)
        try:
            return f.read()
        finally:
            f.close()
    except (IOError, TypeError):
        return ''


def split_commas(str):
    if str == '':
        return []
    return str.split(',')


def gzip_compressor(request):
    plugins = split_commas(request.GET.get('plugins', ''))
    languages = split_commas(request.GET.get('languages', ''))
    themes = split_commas(request.GET.get('themes', ''))
    isJS = request.GET.get('js', '') == 'true'
    compress = request.GET.get('compress', 'true') == 'true'
    suffix = request.GET.get('suffix', '') == '_src' and '_src' or ''
    content = []

    response = HttpResponse()
    response['Content-Type'] = 'text/javascript'

    if not isJS:
        response.write(render_to_string('tinymce/tiny_mce_gzip.js', {
            'base_url': tinymce.settings.JS_BASE_URL,
        }))
        return response

    patch_vary_headers(response, ['Accept-Encoding'])

    now = datetime.utcnow()
    response['Date'] = now.strftime('%a, %d %b %Y %H:%M:%S GMT')

    cacheKey = '|'.join(plugins + languages + themes)
    cacheData = cache.get(cacheKey)

    if cacheData is not None:
        if 'ETag' in cacheData:
            if_none_match = request.META.get('HTTP_IF_NONE_MATCH')
            if if_none_match == cacheData['ETag']:
                response.status_code = 304
                response.content = ''
                response['Content-Length'] = '0'
                return response

        if 'Last-Modified' in cacheData:
            if_modified_since = request.META.get('HTTP_IF_MODIFIED_SINCE')
            if if_modified_since == cacheData['Last-Modified']:
                response.status_code = 304
                response.content = ''
                response['Content-Length'] = '0'
                return response

    tinyMCEPreInit = {
        'base': tinymce.settings.JS_BASE_URL,
        'suffix': '',
    }
    content.append('var tinyMCEPreInit={!s};'.format(
        json.dumps(tinyMCEPreInit)
    ))

    # Add core
    files = ['tiny_mce']

    # Add core languages
    for lang in languages:
        files.append('langs/{!s}'.format(lang))

    # Add plugins
    for plugin in plugins:
        files.append('plugins/{!s}/editor_plugin{!s}'.format(plugin, suffix))

        for lang in languages:
            files.append('plugins/{!s}/langs/{!s}'.format(plugin, lang))

    # Add themes
    for theme in themes:
        files.append('themes/{!s}/editor_template{!s}'.format(theme, suffix))

        for lang in languages:
            files.append('themes/{!s}/langs/{!s}'.format(theme, lang))

    for f in files:
        # Check for unsafe characters
        if not safe_filename_re.match(f):
            continue
        content.append(get_file_contents('{!s}.js'.format(f)))

    # Restore loading functions
    content.append('tinymce.each("{!s}".split(","), function(f){{'
                   'tinymce.ScriptLoader.markDone(tinyMCE.baseURL+'
                   '"/"+f+".js");}});'.format(','.join(files)))

    unicode_content = []
    for i, c in enumerate(content):
        try:
            unicode_content.append(c.decode('latin-1'))
        except AttributeError:
            # python 3 way
            unicode_content.append(smart_text(c))
        except UnicodeDecodeError:
            try:
                unicode_content.append(c.decode('utf-8'))
            except Exception:
                print('{!s} is nor latin-1 nor utf-8.'.format(files[i]))
                raise

    # Compress
    if compress:
        content = compress_string(b''.join([c.encode('utf-8')
                                           for c in unicode_content]))
        response['Content-Encoding'] = 'gzip'
        response['Content-Length'] = str(len(content))

    response.write(content)
    timeout = 3600 * 24 * 10
    patch_response_headers(response, timeout)
    if not response.has_header('Last-Modified'):
        # Last-Modified not set since Django 1.11
        response['Last-Modified'] = http_date()
    cache.set(cacheKey, {
        'Last-Modified': response['Last-Modified'],
        'ETag': response.get('ETag', ''),
    })
    return response

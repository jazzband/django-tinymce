"""
Based on "TinyMCE Compressor PHP" from MoxieCode.

http://tinymce.moxiecode.com/

Copyright (c) 2008 Jason Davies
Licensed under the terms of the MIT License (see LICENSE.txt)
"""

from datetime import datetime
import os

from django.conf import settings
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import Http404
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils.text import compress_string
from django.utils.cache import patch_vary_headers, patch_response_headers

import tinymce.settings


def get_file_contents(filename):
    try:
        f = open(os.path.join(tinymce.settings.JS_ROOT, filename))
        try:
            return f.read()
        finally:
            f.close()
    except IOError:
        return ""

def split_commas(str):
    if str == '':
        return []
    return str.split(",")

def gzip_compressor(request):
    plugins = split_commas(request.GET.get("plugins", ""))
    languages = split_commas(request.GET.get("languages", ""))
    themes = split_commas(request.GET.get("themes", ""))
    isJS = request.GET.get("js", "") == "true"
    compress = request.GET.get("compress", "true") == "true"
    suffix = request.GET.get("suffix", "") == "_src" and "_src" or ""
    content = []

    response = HttpResponse()
    response["Content-Type"] = "text/javascript"

    if not isJS:
        response.write(render_to_string('tinymce/tiny_mce_gzip.js', {
            'base_url': tinymce.settings.JS_BASE_URL,
        }, context_instance=RequestContext(request)))
        return response

    patch_vary_headers(response, ['Accept-Encoding'])

    now = datetime.utcnow()
    response['Date'] = now.strftime('%a, %d %b %Y %H:%M:%S GMT')

    cacheKey = '|'.join(plugins + languages + themes)
    cacheData = cache.get(cacheKey)

    if not cacheData is None:
        if cacheData.has_key('ETag'):
            if_none_match = request.META.get('HTTP_IF_NONE_MATCH', None)
            if if_none_match == cacheData['ETag']:
                response.status_code = 304
                response.content = ''
                response['Content-Length'] = '0'
                return response

        if cacheData.has_key('Last-Modified'):
            if_modified_since = request.META.get('HTTP_IF_MODIFIED_SINCE', None)
            if if_modified_since == cacheData['Last-Modified']:
                response.status_code = 304
                response.content = ''
                response['Content-Length'] = '0'
                return response

    # Add core, with baseURL added
    content.append(get_file_contents("tiny_mce%s.js" % suffix).replace(
            "tinymce._init();", "tinymce.baseURL='%s';tinymce._init();"
            % tinymce.settings.JS_BASE_URL))

    # Patch loading functions
    content.append("tinyMCE_GZ.start();")

    # Add core languages
    for lang in languages:
        content.append(get_file_contents("langs/%s.js" % lang))

    # Add themes
    for theme in themes:
        content.append(get_file_contents("themes/%s/editor_template%s.js"
                % (theme, suffix)))

        for lang in languages:
            content.append(get_file_contents("themes/%s/langs/%s.js"
                    % (theme, lang)))

    # Add plugins
    for plugin in plugins:
        content.append(get_file_contents("plugins/%s/editor_plugin%s.js"
                % (plugin, suffix)))

        for lang in languages:
            content.append(get_file_contents("plugins/%s/langs/%s.js"
                    % (plugin, lang)))

    # Add filebrowser
    if tinymce.settings.USE_FILEBROWSER:
        content.append(render_to_string('tinymce/filebrowser.js', {},
            context_instance=RequestContext(request)).encode("utf-8"))

    # Restore loading functions
    content.append("tinyMCE_GZ.end();")

    # Compress
    if compress:
        content = compress_string(''.join(content))
        response['Content-Encoding'] = 'gzip'
        response['Content-Length'] = str(len(content))

    response.write(content)
    timeout = 3600 * 24 * 10
    patch_response_headers(response, timeout)
    cache.set(cacheKey, {
        'Last-Modified': response['Last-Modified'],
        'ETag': response['ETag'],
    })
    return response

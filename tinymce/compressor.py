"""
Based on "TinyMCE Compressor PHP" from MoxieCode.

http://tinymce.moxiecode.com/

Copyright (c) 2008 Jason Davies
Licensed under the terms of the MIT License (see LICENSE.txt)
"""

from datetime import datetime
import json
import logging
import os
import re

from django.contrib.staticfiles import finders
from django.core.cache import cache
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.cache import patch_response_headers, patch_vary_headers
from django.utils.http import http_date
from django.utils.text import compress_string

import tinymce.settings

logger = logging.getLogger(__name__)

safe_filename_re = re.compile("^[a-zA-Z][a-zA-Z0-9_/-]*$")


def get_file_contents(filename, source=False):
    file_path = finders.find(os.path.join("tinymce", f"{filename}.js"))
    if not file_path:
        file_path = finders.find(os.path.join("tinymce", f"{filename}.min.js"))

    try:
        with open(file_path) as fh:
            return fh.read()
    except (IOError, TypeError):
        logger.error(f"Couldn't load file: {file_path} for {filename}")
        return ""


def split_commas(str):
    if str == "":
        return []
    return str.split(",")


def gzip_compressor(request):
    plugins = split_commas(request.GET.get("plugins", ""))
    languages = split_commas(request.GET.get("languages", ""))
    themes = split_commas(request.GET.get("themes", ""))
    files = split_commas(request.GET.get("files", ""))
    source = request.GET.get("src", "") == "true"
    isJS = request.GET.get("js", "") == "true"
    compress = request.GET.get("compress", "true") == "true"
    content = []

    response = HttpResponse()
    response["Content-Type"] = "text/javascript"

    js_url = tinymce.settings.get_js_url()
    js_base_url = js_url[: js_url.rfind("/")]
    if not isJS:
        response.write(render_to_string("tinymce/tiny_mce_gzip.js", {"base_url": js_base_url}))
        return response

    patch_vary_headers(response, ["Accept-Encoding"])

    now = datetime.utcnow()
    response["Date"] = now.strftime("%a, %d %b %Y %H:%M:%S GMT")

    cacheKey = "|".join(plugins + languages + themes)
    cacheData = cache.get(cacheKey)

    if cacheData is not None:
        if "ETag" in cacheData:
            if_none_match = request.META.get("HTTP_IF_NONE_MATCH")
            if if_none_match == cacheData["ETag"]:
                response.status_code = 304
                response.content = ""
                response["Content-Length"] = "0"
                return response

        if "Last-Modified" in cacheData:
            if_modified_since = request.META.get("HTTP_IF_MODIFIED_SINCE")
            if if_modified_since == cacheData["Last-Modified"]:
                response.status_code = 304
                response.content = ""
                response["Content-Length"] = "0"
                return response

    tinyMCEPreInit = {
        "base": js_base_url,
        "suffix": "",
    }
    content.append(f"var tinyMCEPreInit={json.dumps(tinyMCEPreInit)};")

    # Add core
    files = ["tinymce"]

    # Add core languages
    for lang in languages:
        files.append(f"langs/{lang}")

    # Add plugins
    for plugin in plugins:
        files.append(f"plugins/{plugin}/plugin")

        for lang in languages:
            files.append(f"plugins/{plugin}/langs/{lang}")

    # Add themes
    for theme in themes:
        files.append(f"themes/{theme}/theme")

        for lang in languages:
            files.append(f"themes/{theme}/langs/{lang}")

    for f in files:
        # Check for unsafe characters
        if not safe_filename_re.match(f):
            continue
        content.append(get_file_contents(f, source=source))

    # Restore loading functions
    content.append(
        'tinymce.each("{}".split(",")'.format(",".join(files))
        + ', function(f){tinymce.ScriptLoader.markDone(tinyMCE.baseURL+"/"+f+".js");});'
    )

    # Compress
    if compress:
        content = compress_string(b"".join([c.encode("utf-8") for c in content]))
        response["Content-Encoding"] = "gzip"
        response["Content-Length"] = str(len(content))

    response.write(content)
    timeout = 3600 * 24 * 10
    patch_response_headers(response, timeout)
    if not response.has_header("Last-Modified"):
        response["Last-Modified"] = http_date()
    cache.set(
        cacheKey,
        {"Last-Modified": response["Last-Modified"], "ETag": response.get("ETag", "")},
    )
    return response

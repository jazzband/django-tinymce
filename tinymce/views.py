# Copyright (c) 2008 Joost Cassee
# Licensed under the terms of the MIT License (see LICENSE.txt)

import json
import logging

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from tinymce.compressor import gzip_compressor

try:
    import enchant
except ImportError:
    enchant = None


@csrf_exempt
def spell_check(request):
    """
    Returns a response that implements the TinyMCE spellchecker protocol.
    """
    try:
        if not enchant:
            raise RuntimeError("install pyenchant for spellchecker functionality")

        method = request.POST.get("method")
        text = request.POST.get("text")
        lang = request.POST.get("lang")

        if not enchant.dict_exists(lang):
            e_msg = f"Dictionary not found for language '{lang}', check pyenchant."
            raise RuntimeError(e_msg)

        checker = enchant.Dict(lang)

        def sanitize_words(text):
            """
            Sanitize words in text and recommend suggestions for wrong words.
            """
            suggested_words = {}
            words = text.split()
            for word in words:
                word.strip()
                word.strip(".,:;'\"")
                if not checker.check(word):
                    suggested_words[word] = checker.suggest(word)
            return suggested_words

        if method == "spellcheck":
            output = {"words": sanitize_words(text)}
        else:
            e_msg = f"Got an unexpected method '{method}'"
            raise RuntimeError(e_msg)

    except Exception as err:
        logging.exception("Error running spellchecker")
        output = {"error": str(err)}

    return JsonResponse(output)


def flatpages_link_list(request):
    """
    Returns a HttpResponse whose content is a Javascript file representing a
    list of links to flatpages.
    """
    from django.contrib.flatpages.models import FlatPage

    link_list = [(page.title, page.url) for page in FlatPage.objects.all()]
    return render_to_link_list(link_list)


def compressor(request):
    """
    Returns a GZip-compressed response.
    """
    return gzip_compressor(request)


def render_to_link_list(link_list):
    """
    Returns a HttpResponse whose content is a Javascript file representing a
    list of links suitable for use wit the TinyMCE external_link_list_url
    configuration option. The link_list parameter must be a list of 2-tuples.
    """
    return render_to_js_vardef("tinyMCELinkList", link_list)


def render_to_image_list(image_list):
    """
    Returns a HttpResponse whose content is a Javascript file representing a
    list of images suitable for use wit the TinyMCE external_image_list_url
    configuration option. The image_list parameter must be a list of 2-tuples.
    """
    return render_to_js_vardef("tinyMCEImageList", image_list)


def render_to_js_vardef(var_name, var_value):
    output = f"var {var_name} = {json.dumps(var_value)};"
    return HttpResponse(output, content_type="application/x-javascript")


def filebrowser(request):
    try:
        fb_url = request.build_absolute_uri(reverse("fb_browse"))
    except Exception:
        fb_url = request.build_absolute_uri(reverse("filebrowser:fb_browse"))

    return render(
        request,
        "tinymce/filebrowser.js",
        {"fb_url": fb_url},
        content_type="application/javascript",
    )

# Copyright (c) 2008 Joost Cassee
# Licensed under the terms of the MIT License (see LICENSE.txt)

import logging
from django.core import urlresolvers
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.datastructures import MultiValueDictKeyError
from django.utils.translation import ugettext as _
from tinymce.compressor import gzip_compressor
import json
try:
    from django.views.decorators.csrf import csrf_exempt
except ImportError:
    pass
try:
    import enchant
except ImportError:
    enchant = None

try:
    from django.utils.encoding import smart_text as smart_unicode
except ImportError:
    try:
        from django.utils.encoding import smart_unicode
    except ImportError:
        from django.forms.util import smart_unicode


def spell_check(request):
    """
    Returns a HttpResponse that implements the TinyMCE spellchecker protocol.
    """
    try:
        if not enchant:
            raise RuntimeError("install pyenchant for spellchecker functionality")

        raw = smart_unicode(request.body)
        input = json.loads(raw)
        id = input['id']
        method = input['method']
        params = input['params']
        lang = params[0]
        arg = params[1]

        if not enchant.dict_exists(str(lang)):
            raise RuntimeError("dictionary not found for language {!r}".format(lang))

        checker = enchant.Dict(str(lang))

        if method == 'checkWords':
            result = [word for word in arg if word and not checker.check(word)]
        elif method == 'getSuggestions':
            result = checker.suggest(arg)
        else:
            raise RuntimeError("Unknown spellcheck method: {!r}".format(method))
        output = {
            'id': id,
            'result': result,
            'error': None,
        }
    except Exception:
        logging.exception("Error running spellchecker")
        return HttpResponse(_("Error running spellchecker"))
    return HttpResponse(json.dumps(output),
                        content_type='application/json')

try:
    spell_check = csrf_exempt(spell_check)
except NameError:
    pass


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
    return render_to_js_vardef('tinyMCELinkList', link_list)


def render_to_image_list(image_list):
    """
    Returns a HttpResponse whose content is a Javascript file representing a
    list of images suitable for use wit the TinyMCE external_image_list_url
    configuration option. The image_list parameter must be a list of 2-tuples.
    """
    return render_to_js_vardef('tinyMCEImageList', image_list)


def render_to_js_vardef(var_name, var_value):
    output = "var {!s} = {!s};".format(var_name, json.dumps(var_value))
    return HttpResponse(output, content_type='application/x-javascript')


def filebrowser(request):
    try:
        fb_url = request.build_absolute_uri(urlresolvers.reverse('fb_browse'))
    except:
        fb_url = request.build_absolute_uri(urlresolvers.reverse('filebrowser:fb_browse'))

    return render_to_response('tinymce/filebrowser.js', {'fb_url': fb_url },
            context_instance=RequestContext(request))

def filebrowserPath(request):
    try:
        _dir = request.GET['dir']
    except MultiValueDictKeyError:
        _dir = ''

    return render_to_response('tinymce/defaultpath.js', {'dir': _dir,},
                              context_instance=RequestContext(request))

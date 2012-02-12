# Copyright (c) 2008 Joost Cassee
# Licensed under the terms of the MIT License (see LICENSE.txt)

import logging
from django.core import urlresolvers
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.utils import simplejson
from django.utils.translation import ugettext as _
from tinymce.compressor import gzip_compressor
from tinymce.widgets import get_language_config
try:
    from django.views.decorators.csrf import csrf_exempt
except ImportError:
    pass

def textareas_js(request, name, lang=None):
    """
    Returns a HttpResponse whose content is a Javscript file. The template
    is loaded from 'tinymce/<name>_textareas.js' or
    '<name>/tinymce_textareas.js'. Optionally, the lang argument sets the
    content language.
    """
    template_files = (
        'tinymce/%s_textareas.js' % name,
        '%s/tinymce_textareas.js' % name,
    )
    template = loader.select_template(template_files)

    vars = get_language_config(lang)
    vars['content_language'] = lang
    context = RequestContext(request, vars)

    return HttpResponse(template.render(context),
            content_type="application/x-javascript")

def spell_check(request):
    """
    Returns a HttpResponse that implements the TinyMCE spellchecker protocol.
    """
    try:
        import enchant

        raw = request.raw_post_data
        input = simplejson.loads(raw)
        id = input['id']
        method = input['method']
        params = input['params']
        lang = params[0]
        arg = params[1]

        if not enchant.dict_exists(str(lang)):
            raise RuntimeError("dictionary not found for language '%s'" % lang)

        checker = enchant.Dict(str(lang))

        if method == 'checkWords':
            result = [word for word in arg if word and not checker.check(word)]
        elif method == 'getSuggestions':
            result = checker.suggest(arg)
        else:
            raise RuntimeError("Unkown spellcheck method: '%s'" % method)
        output = {
            'id': id,
            'result': result,
            'error': None,
        }
    except Exception:
        logging.exception("Error running spellchecker")
        return HttpResponse(_("Error running spellchecker"))
    return HttpResponse(simplejson.dumps(output),
            content_type='application/json')

try:
    spell_check = csrf_exempt(spell_check)
except NameError:
    pass

def preview(request, name):
    """
    Returns a HttpResponse whose content is an HTML file that is used
    by the TinyMCE preview plugin. The template is loaded from
    'tinymce/<name>_preview.html' or '<name>/tinymce_preview.html'.
    """
    template_files = (
        'tinymce/%s_preview.html' % name,
        '%s/tinymce_preview.html' % name,
    )
    template = loader.select_template(template_files)
    return HttpResponse(template.render(RequestContext(request)),
            content_type="text/html")


def flatpages_link_list(request):
    """
    Returns a HttpResponse whose content is a Javscript file representing a
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
    Returns a HttpResponse whose content is a Javscript file representing a
    list of links suitable for use wit the TinyMCE external_link_list_url
    configuration option. The link_list parameter must be a list of 2-tuples.
    """
    return render_to_js_vardef('tinyMCELinkList', link_list)

def render_to_image_list(image_list):
    """
    Returns a HttpResponse whose content is a Javscript file representing a
    list of images suitable for use wit the TinyMCE external_image_list_url
    configuration option. The image_list parameter must be a list of 2-tuples.
    """
    return render_to_js_vardef('tinyMCEImageList', image_list)

def render_to_js_vardef(var_name, var_value):
    output = "var %s = %s" % (var_name, simplejson.dumps(var_value))
    return HttpResponse(output, content_type='application/x-javascript')

def filebrowser(request):
    try:
        fb_url = request.build_absolute_uri(urlresolvers.reverse('fb_browse'))
    except:
        fb_url = request.build_absolute_uri(urlresolvers.reverse('filebrowser:fb_browse'))

    return render_to_response('tinymce/filebrowser.js', {'fb_url': fb_url},
            context_instance=RequestContext(request))

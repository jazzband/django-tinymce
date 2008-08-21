import logging
from django.forms import ModelForm
from django.forms.models import modelformset_factory
from django.http import HttpResponse
from django.template import RequestContext, loader
from tinymce.utils import get_language_config
from django.utils import simplejson
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _
from tinymce.widgets import TinyMCE

def textareas_js(request, name='', lang=None):
    if name:
        template_files = (
            'tinymce/textareas_%s.js' % name,
            '%s/textareas.js' % name,
        )
    else:
        template_files = ('tinymce/textareas.js',)

    template = loader.select_template(template_files)
    vars = get_language_config(lang)
    vars['content_language'] = lang
    context = RequestContext(request, vars)

    return HttpResponse(template.render(context),
            content_type="application/x-javascript")


def spell_check(request):
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
        checker = enchant.Dict(lang)
        if method == 'checkWords':
            result = [word for word in arg if not checker.check(word)]
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

# coding: utf-8

from django.test import TestCase
from django.template import Template, Context


class TestTemplateTags(TestCase):
    TEMPLATE = Template("{% load tinymce_tags %} {% tinymce_preview 'text' %}")

    def test_tinymce_preview(self):
        rendered = self.TEMPLATE.render(Context({}))
        check_tinymce_popup = '<script language="javascript" src="/static/tiny_mce/tiny_mce_popup.js"></script>'
        check_tinymce_embed = '<script type="text/javascript"\nsrc="/static/tiny_mce/plugins/preview/jscripts/embed.js"></script>'
        check_tinymce_popup_init = '''<script type="text/javascript">\n    tinyMCEPopup.onInit.add(function(ed) {\n        var dom = tinyMCEPopup.dom;\n\n        dom.setHTML(\'text\', ed.getContent());\n    });\n\n    document.write(\'<base href="\' + tinyMCEPopup.getWindowArg("base") + \'">\');\n</script>'''
        self.assertIn(check_tinymce_popup, rendered)
        self.assertIn(check_tinymce_embed, rendered)
        self.assertIn(check_tinymce_popup_init, rendered)

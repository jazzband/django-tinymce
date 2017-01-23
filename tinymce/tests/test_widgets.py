# coding: utf-8

from django import forms
from django.test import TestCase
from django.test.utils import override_settings
from django.utils.translation import override

from tinymce.widgets import get_language_config, TinyMCE


@override_settings(LANGUAGES=[('en', 'English')])
class TestWidgets(TestCase):

    def test_default_config(self):
        config = get_language_config()
        config_ok = {
            'spellchecker_languages': '+English=en',
            'directionality': 'ltr',
            'language': 'en',
            'spellchecker_rpc_url': '/tinymce/spellchecker/'
        }
        self.assertEqual(config, config_ok)
        with override(None):
            # Even when no language is activated
            config = get_language_config()
            self.assertEqual(config, config_ok)

    @override_settings(LANGUAGES_BIDI=['en'])
    def test_default_config_rtl(self):
        config = get_language_config()
        config_ok = {
            'spellchecker_languages': '+English=en',
            'directionality': 'rtl',
            'language': 'en',
            'spellchecker_rpc_url': '/tinymce/spellchecker/'
        }
        self.assertEqual(config, config_ok)

    def test_content_language(self):
        config = get_language_config('ru-ru')
        config_ok = {
            'spellchecker_languages': 'English=en',
            'directionality': 'ltr',
            'language': 'en',
            'spellchecker_rpc_url': '/tinymce/spellchecker/'
        }
        self.assertEqual(config, config_ok)

    def test_tinymce_widget(self):
        widget = TinyMCE()
        html = widget.render(
            'foobar', 'lorem ipsum', attrs={'id': 'id_foobar'}
        )
        self.assertIn('id="id_foobar"', html)
        self.assertIn('name="foobar"', html)
        self.assertIn('lorem ipsum', html)
        self.assertIn('class="tinymce"', html)
        html = widget.render(
            'foobar', 'lorem ipsum', attrs={'id': 'id_foobar', 'class': 'foo'}
        )
        self.assertIn('class="foo tinymce"', html)

    def test_tinymce_widget_required(self):
        """
        The TinyMCE widget should never output the required HTML attribute, even
        if the form field is required, as the client-side browser validation
        might prevent form submission.
        """
        class TinyForm(forms.Form):
            field = forms.CharField(required=True, widget=TinyMCE())

        rendered = str(TinyForm())
        self.assertNotIn('required', rendered)

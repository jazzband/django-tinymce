# coding: utf-8

from contextlib import contextmanager

from django import forms
from django.test import TestCase
from django.test.utils import override_settings
from django.utils.translation import override

import tinymce.settings
from tinymce.widgets import get_language_config, TinyMCE


@contextmanager
def override_tinymce_settings(settings_dict):
    saved_values = {}
    for setting, value in settings_dict.items():
        saved_values[setting] = getattr(tinymce.settings, setting)
        setattr(tinymce.settings, setting, value)
    yield
    for setting in settings_dict.keys():
        setattr(tinymce.settings, setting, saved_values[setting])


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

    @override_settings(TINYMCE_INCLUDE_JQUERY=False)
    def test_tinymce_widget_media(self):
        widget = TinyMCE()
        self.assertEqual(
            widget.media.render_js(),
            [
                '<script type="text/javascript" src="/tinymce/compressor/"></script>',
                '<script type="text/javascript" src="/static/django_tinymce/jquery-1.9.1.min.js"></script>',
                '<script type="text/javascript" src="/static/django_tinymce/init_tinymce.js"></script>',
            ]
        )
        self.assertEqual(list(widget.media.render_css()), [])
        with override_tinymce_settings({'USE_COMPRESSOR': False, 'INCLUDE_JQUERY': False}):
            widget = TinyMCE()
            self.assertEqual(
                widget.media.render_js(),
                [
                    '<script type="text/javascript" src="/static/tiny_mce/tiny_mce.js"></script>',
                    '<script type="text/javascript" src="/static/django_tinymce/init_tinymce.js"></script>',
                ]
            )

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

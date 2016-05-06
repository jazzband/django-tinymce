# coding: utf-8

from django.test import TestCase
from django.test.utils import override_settings

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

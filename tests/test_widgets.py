from contextlib import contextmanager
from unittest.mock import patch

import django
from django import forms
from django.test import SimpleTestCase
from django.test.utils import override_settings
from django.utils.translation import override

import tinymce.settings
from tinymce.widgets import TinyMCE, get_language_config


@contextmanager
def override_tinymce_settings(settings_dict):
    saved_values = {}
    for setting, value in settings_dict.items():
        saved_values[setting] = getattr(tinymce.settings, setting)
        setattr(tinymce.settings, setting, value)
    yield
    for setting in settings_dict.keys():
        setattr(tinymce.settings, setting, saved_values[setting])


@override_settings(LANGUAGES=[("en", "English")])
class TestWidgets(SimpleTestCase):
    def test_default_config(self):
        config = get_language_config("en")
        config_ok = {
            "spellchecker_languages": "+English=en",
            "directionality": "ltr",
            "spellchecker_rpc_url": "/tinymce/spellchecker/",
        }
        self.assertEqual(config, config_ok)

    def test_no_active_language(self):
        widget = TinyMCE()
        with override(None):
            config = widget.get_mce_config(attrs={"id": "id"})
            self.assertNotIn("language", config.keys())
            self.assertEqual(config["spellchecker_languages"], "+English=en")

    @override_settings(LANGUAGES_BIDI=["en"])
    def test_default_config_rtl(self):
        config = get_language_config("en")
        config_ok = {
            "spellchecker_languages": "+English=en",
            "directionality": "rtl",
            "spellchecker_rpc_url": "/tinymce/spellchecker/",
        }
        self.assertEqual(config, config_ok)

    def test_config_from_language_code(self):
        langs = [
            ("en", "en"),
            ("fr", "fr_FR"),  # Currently no "fr" language file exist for TinyMCE.
            ("de-ch", "de"),
            ("pt-br", "pt_BR"),
            ("he", "he_IL"),
            ("he_il", "he_IL"),
        ]
        widget = TinyMCE()
        for lang_code, lang_expected in langs:
            with override_settings(LANGUAGE_CODE=lang_code):
                config = widget.get_mce_config(attrs={"id": "id"})
                self.assertEqual(config["language"], lang_expected)
        # A language with no matching TinyMCE translation:
        expected = "No TinyMCE language found for 'af', defaulting to 'en_US'"
        with self.assertWarnsRegex(RuntimeWarning, expected):
            with override_settings(LANGUAGE_CODE="af"):
                config = widget.get_mce_config(attrs={"id": "id"})
                self.assertEqual(config["language"], "en_US")

    def test_no_language_for_en_US(self):
        """
        en_US shouldn't set 'language'
        (https://github.com/tinymce/tinymce/issues/4228)
        """
        widget = TinyMCE()
        with override_settings(LANGUAGE_CODE="en-us"):
            config = widget.get_mce_config(attrs={"id": "id"})
            self.assertNotIn("language", config.keys())
        self.assertEqual(config["directionality"], "ltr")

    def test_language_override_from_config(self):
        """language in DEFAULT_CONFIG has priority over current Django language."""
        widget = TinyMCE()
        orig_config = tinymce.settings.DEFAULT_CONFIG
        with patch.dict(tinymce.settings.DEFAULT_CONFIG, {**orig_config, "language": "es_ES"}):
            config = widget.get_mce_config(attrs={"id": "id"})
            self.assertEqual(config["language"], "es_ES")

    def test_mce_attrs_language_priority(self):
        widget = TinyMCE(mce_attrs={"language": "ru"})
        orig_config = tinymce.settings.DEFAULT_CONFIG
        with patch.dict(tinymce.settings.DEFAULT_CONFIG, {**orig_config, "language": "es_ES"}):
            config = widget.get_mce_config(attrs={"id": "id"})
            self.assertEqual(config["language"], "ru")

    def test_content_language(self):
        config = get_language_config("ru-ru")
        config_ok = {
            "spellchecker_languages": "English=en",
            "directionality": "ltr",
            "spellchecker_rpc_url": "/tinymce/spellchecker/",
        }
        self.assertEqual(config, config_ok)

    def test_tinymce_widget(self):
        widget = TinyMCE()
        html = widget.render("foobar", "lorem ipsum", attrs={"id": "id_foobar"})
        self.assertIn('id="id_foobar"', html)
        self.assertIn('name="foobar"', html)
        self.assertIn("lorem ipsum", html)
        self.assertIn('class="tinymce"', html)
        html = widget.render("foobar", "lorem ipsum", attrs={"id": "id_foobar", "class": "foo"})
        self.assertIn('class="foo tinymce"', html)

    def test_tinymce_widget_size(self):
        widget = TinyMCE(attrs={"cols": 80, "rows": 30})
        html = widget.render("foobar", "lorem ipsum", attrs={"id": "id_foobar"})
        self.assertIn('cols="80"', html)
        self.assertIn('rows="30"', html)

    def test_tinymce_widget_media(self):
        widget = TinyMCE()
        js_type = 'type="text/javascript" ' if django.get_version() < "3.1" else ""
        self.assertEqual(
            widget.media.render_js(),
            [
                f'<script {js_type}src="/tinymce/compressor/"></script>',
                f'<script {js_type}src="/static/django_tinymce/init_tinymce.js"></script>',
            ],
        )
        self.assertEqual(list(widget.media.render_css()), [])
        with override_tinymce_settings({"USE_COMPRESSOR": False}):
            widget = TinyMCE()
            self.assertEqual(
                widget.media.render_js(),
                [
                    f'<script {js_type}src="/static/tinymce/tinymce.min.js"></script>',
                    f'<script {js_type}src="/static/django_tinymce/init_tinymce.js"></script>',
                ],
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
        self.assertNotIn("required", rendered)

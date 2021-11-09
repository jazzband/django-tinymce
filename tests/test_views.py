import os
from unittest.mock import Mock, patch
from urllib.parse import urlencode

from django.contrib.flatpages.models import FlatPage
from django.http import HttpResponse
from django.test import TestCase

from tinymce.views import render_to_image_list

devnull = open(os.devnull, "w")


def compress_whitespace(s):
    # replace whitespace runs with a single space
    return " ".join(s.split())


class TestViews(TestCase):
    @patch("tinymce.views.enchant")
    def test_spell_check_words(self, enchant_mock):
        checker_mock = Mock()
        checker_mock.check.return_value = True
        enchant_mock.Dict.return_value = checker_mock

        body = urlencode({"method": "spellcheck", "text": "tesat", "lang": "en"})
        response = self.client.post(
            "/tinymce/spellchecker/", body, content_type="application/x-www-form-urlencoded"
        )

        output = {"words": {}}

        self.assertEqual(200, response.status_code)
        self.assertEqual("application/json", response["Content-Type"])
        self.assertEqual(output, response.json())

    @patch("tinymce.views.enchant")
    def test_spell_check_suggest(self, enchant_mock):
        result = ["sample"]
        checker_mock = Mock()
        checker_mock.check.return_value = False
        checker_mock.suggest.return_value = result
        enchant_mock.Dict.return_value = checker_mock

        body = urlencode({"method": "spellcheck", "text": "smaple", "lang": "en"})
        response = self.client.post(
            "/tinymce/spellchecker/", body, content_type="application/x-www-form-urlencoded"
        )

        output = {"words": {"smaple": ["sample"]}}

        self.assertEqual(200, response.status_code)
        self.assertEqual("application/json", response["Content-Type"])
        self.assertEqual(output, response.json())

    @patch("tinymce.views.enchant")
    def test_spell_check_empty(self, enchant_mock):
        checker_mock = Mock()
        checker_mock.check.return_value = True
        enchant_mock.Dict.return_value = checker_mock

        body = urlencode({"method": "spellcheck", "text": "", "lang": "en"})
        response = self.client.post(
            "/tinymce/spellchecker/", body, content_type="application/x-www-form-urlencoded"
        )

        output = {"words": {}}

        self.assertEqual(200, response.status_code)
        self.assertEqual("application/json", response["Content-Type"])
        self.assertEqual(output, response.json())

    @patch("tinymce.views.enchant")
    def test_spell_check_unknown_method(self, enchant_mock):
        body = urlencode({"method": "test", "text": "test", "lang": "en"})
        with patch("sys.stderr", devnull):
            response = self.client.post(
                "/tinymce/spellchecker/", body, content_type="application/x-www-form-urlencoded"
            )

        output = {"error": "Got an unexpected method 'test'"}

        self.assertEqual(200, response.status_code)
        self.assertEqual("application/json", response["Content-Type"])
        self.assertEqual(output, response.json())

    @patch("tinymce.views.enchant")
    def test_spell_check_unknown_lang(self, enchant_mock):
        enchant_mock.dict_exists.return_value = False

        body = urlencode({"method": "spellcheck", "text": "test", "lang": "en"})
        with patch("sys.stderr", devnull):
            response = self.client.post(
                "/tinymce/spellchecker/", body, content_type="application/x-www-form-urlencoded"
            )

        output = {"error": "Dictionary not found for language 'en', check pyenchant."}

        self.assertEqual(200, response.status_code)
        self.assertEqual("application/json", response["Content-Type"])
        self.assertEqual(output, response.json())

    def test_flatpages_link_list(self):
        FlatPage.objects.create(
            url="/test/url",
            title="Test Title",
        )
        response = self.client.get("/tinymce/flatpages_link_list/")
        result_ok = b'var tinyMCELinkList = [["Test Title", "/test/url"]];'
        self.assertEqual(200, response.status_code)
        self.assertEqual("application/x-javascript", response["Content-Type"])
        self.assertEqual(result_ok, response.content)

    @patch("tinymce.views.gzip_compressor")
    def test_compressor(self, gzip_mock):
        response_ok = HttpResponse("test", content_type="text/javascript")
        gzip_mock.return_value = response_ok

        response = self.client.get("/tinymce/compressor/")

        self.assertEqual(200, response.status_code)
        self.assertEqual("text/javascript", response["Content-Type"])
        self.assertEqual(response_ok.content, response.content)
        self.assertTrue(gzip_mock.called_once)

    def test_render_to_image_list(self):
        response = render_to_image_list([("test", "test.jpg")])
        result_ok = b'var tinyMCEImageList = [["test", "test.jpg"]];'
        self.assertEqual(200, response.status_code)
        self.assertEqual("application/x-javascript", response["Content-Type"])
        self.assertEqual(result_ok, response.content)

    @patch("tinymce.views.reverse", return_value="/filebrowser")
    def test_filebrowser(self, reverse_mock):
        response = self.client.get("/tinymce/filebrowser/")
        with open("tinymce/templates/tinymce/filebrowser.js") as f:
            response_ok = f.read()
        response_ok = response_ok.replace("{{ fb_url }}", "http://testserver/filebrowser")
        self.assertEqual(200, response.status_code)
        self.assertEqual(
            compress_whitespace(response_ok),
            compress_whitespace(response.content.decode()),
        )

import os
from unittest.mock import patch

from django.contrib.flatpages.models import FlatPage
from django.http import HttpResponse
from django.test import TestCase

from tinymce.views import render_to_image_list

devnull = open(os.devnull, "w")


def compress_whitespace(s):
    # replace whitespace runs with a single space
    return " ".join(s.split())


class TestViews(TestCase):
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
        gzip_mock.assert_called_once()

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

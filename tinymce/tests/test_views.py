# coding: utf-8

import json
import os
from mock import patch, Mock

from django.contrib.flatpages.models import FlatPage
from django.http import HttpResponse
from django.test import TestCase

from tinymce.views import render_to_image_list

devnull = open(os.devnull, 'w')


class TestViews(TestCase):

    @patch('tinymce.views.enchant')
    def test_spell_check_words(self, enchant_mock):
        checker_mock = Mock()
        checker_mock.check.return_value = False
        enchant_mock.Dict.return_value = checker_mock

        body = json.dumps({
            'id': 'test',
            'method': 'checkWords',
            'params': ['en', ['test']]
        })
        response = self.client.post('/tinymce/spellchecker/',
                                    body, content_type='application/json')

        output = {
            'id': 'test',
            'result': ['test'],
            'error': None,
        }
        response_ok = HttpResponse(json.dumps(output), content_type='application/json')
        self.assertEqual(200, response.status_code)
        self.assertEqual('application/json', response['Content-Type'])
        self.assertEqual(response_ok.content, response.content)

    @patch('tinymce.views.enchant')
    def test_spell_check_suggest(self, enchant_mock):
        result = ['test']
        checker_mock = Mock()
        checker_mock.suggest.return_value = result
        enchant_mock.Dict.return_value = checker_mock

        body = json.dumps({
            'id': 'test',
            'method': 'getSuggestions',
            'params': ['en', 'test']
        })
        response = self.client.post('/tinymce/spellchecker/',
                                    body, content_type='application/json')
        output = {
            'id': 'test',
            'result': result,
            'error': None,
        }
        response_ok = HttpResponse(json.dumps(output), content_type='application/json')
        self.assertEqual(200, response.status_code)
        self.assertEqual('application/json', response['Content-Type'])
        self.assertEqual(response_ok.content, response.content)

    @patch('tinymce.views.enchant')
    def test_spell_check_unknown(self, enchant_mock):
        checker_mock = Mock()
        checker_mock.suggest.return_value = ['test']
        enchant_mock.Dict.return_value = checker_mock

        body = json.dumps({
            'id': 'test',
            'method': 'test',
            'params': ['en', 'test']
        })
        with patch('sys.stderr', devnull):
            response = self.client.post('/tinymce/spellchecker/',
                                        body, content_type='application/json')
        result_ok = b'Error running spellchecker'
        self.assertEqual(200, response.status_code)
        self.assertEqual('text/html; charset=utf-8', response['Content-Type'])
        self.assertEqual(result_ok, response.content)

    def test_flatpages_link_list(self):
        FlatPage.objects.create(
            url='/test/url',
            title='Test Title',
        )
        response = self.client.get('/tinymce/flatpages_link_list/')
        result_ok = b'var tinyMCELinkList = [["Test Title", "/test/url"]];'
        self.assertEqual(200, response.status_code)
        self.assertEqual('application/x-javascript', response['Content-Type'])
        self.assertEqual(result_ok, response.content)

    @patch('tinymce.views.gzip_compressor')
    def test_compressor(self, gzip_mock):
        response_ok = HttpResponse('test', content_type='text/javascript')
        gzip_mock.return_value = response_ok

        response = self.client.get('/tinymce/compressor/')

        self.assertEqual(200, response.status_code)
        self.assertEqual('text/javascript', response['Content-Type'])
        self.assertEqual(response_ok.content, response.content)
        self.assertTrue(gzip_mock.called_once)

    def test_render_to_image_list(self):
        response = render_to_image_list([('test', 'test.jpg')])
        result_ok = b'var tinyMCEImageList = [["test", "test.jpg"]];'
        self.assertEqual(200, response.status_code)
        self.assertEqual('application/x-javascript', response['Content-Type'])
        self.assertEqual(result_ok, response.content)

    @patch('tinymce.views.reverse', return_value='/filebrowser')
    def test_filebrowser(self, reverse_mock):
        response = self.client.get('/tinymce/filebrowser/')
        response_ok = b'function djangoFileBrowser(field_name, url, type, win) {\n\n    var url = "http://testserver/filebrowser?pop=2&type=" + type;\n    var dir = window.filebrowserPath.getDefaultPath();\n    if ( dir ) {\n        url += "&dir=" + dir\n    }\n\n    tinyMCE.activeEditor.windowManager.open(\n        {\n            \'file\': url,\n            \'width\': 820,\n            \'height\': 500,\n            \'resizable\': "yes",\n            \'scrollbars\': "yes",\n            \'inline\': "no",\n            \'close_previous\': "no"\n        },\n        {\n            \'window\': win,\n            \'input\': field_name,\n            \'editor_id\': tinyMCE.selectedInstance.editorId\n        }\n    );\n    return false;\n}\n'
        self.assertEqual(200, response.status_code)
        self.assertEqual(response_ok, response.content)

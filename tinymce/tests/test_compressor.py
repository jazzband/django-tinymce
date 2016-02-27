# coding: utf-8

import zlib
from mock import patch


from django.test import TestCase, RequestFactory

from tinymce.compressor import gzip_compressor


class TestCompressor(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_not_js(self):
        request = self.factory.get('/tinymce/compressor/')
        response = gzip_compressor(request)

        self.assertEqual(200, response.status_code)
        self.assertEqual('text/javascript', response['Content-Type'])
        self.assertContains(response, 'tinyMCE_GZ')

    @patch('tinymce.compressor.cache.get')
    def test_cache_data_etag(self, cache_mock):
        cache_mock.return_value = {
            'ETag': 'test',
        }
        request = self.factory.get('/tinymce/compressor/', {
            'js': 'true',
        })
        request.META['HTTP_IF_NONE_MATCH'] = 'test'
        response = gzip_compressor(request)

        self.assertEqual(304, response.status_code)
        self.assertEqual('0', response['Content-Length'])
        self.assertEqual('text/javascript', response['Content-Type'])
        self.assertEqual(b'', response.content)
        self.assertTrue(cache_mock.called_once)

    @patch('tinymce.compressor.cache.get')
    def test_cache_data_last_modified(self, cache_mock):
        cache_mock.return_value = {
            'Last-Modified': 'test',
        }
        request = self.factory.get('/tinymce/compressor/', {
            'js': 'true',
        })
        request.META['HTTP_IF_MODIFIED_SINCE'] = 'test'
        response = gzip_compressor(request)

        self.assertEqual(304, response.status_code)
        self.assertEqual('0', response['Content-Length'])
        self.assertEqual('text/javascript', response['Content-Type'])
        self.assertEqual(b'', response.content)
        self.assertTrue(cache_mock.called_once)

    def test_compressor(self):
        request = self.factory.get('/tinymce/compressor/', {
            'js': 'true',
            'compress': 'true',
            'languages': 'en',
            'plugins': 'example',
            'themes': 'advanced',
        })
        response = gzip_compressor(request)
        response_string = zlib.decompress(response.content, 16 + zlib.MAX_WBITS)
        self.assertEqual(200, response.status_code)
        self.assertEqual('text/javascript', response['Content-Type'])
        self.assertEqual('gzip', response['Content-Encoding'])
        self.assertIn(b'var tinyMCEPreInit', response_string)

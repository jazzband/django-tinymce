# coding: utf-8
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse


class TestTinymceViews(object):

    def test_get(self, client, flatpages):
        flatpage = flatpages[0]
        url = reverse('tinymce-linklist')
        response = client.get(url)
        assert response.status_code == 200
        result = response.content.decode('utf-8')
        result_ok = 'var tinyMCELinkList = [["{}", "{}"]];'.format(
            flatpage.title, flatpage.url
        )
        assert result == result_ok

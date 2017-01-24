# coding:utf-8

import pytest
from selenium.common.exceptions import NoSuchElementException

from django.conf import settings
from django import forms
try:
    from django.urls import reverse
except ImportError:
    # Django < 1.10
    from django.core.urlresolvers import reverse

from tinymce.widgets import TinyMCE

from tests.testapp.forms import TestPageModelForm


class TestTinyMCE(object):
    form = TestPageModelForm
    widget_cls = TinyMCE

    def test_initial_data(self, testpages):
        testpage = testpages[0]
        form = TestPageModelForm(instance=testpage)
        html = form.as_p()
        assert testpage.content1 in html
        assert 'data-django-tinymce-config' in html

    def test_initial_form_class(self):
        widget = self.widget_cls(attrs={'class': 'my-class'})
        assert 'my-class' in widget.render('name', None)
        assert 'django-tinymce' in widget.render('name', None)

    def test_no_js_error(self, db, live_server, driver):
        url = reverse('admin:testapp_testpage_add')
        driver.get(live_server + url)
        with pytest.raises(NoSuchElementException):
            error = driver.find_element_by_xpath('//body[@JSError]')
            pytest.fail(error.get_attribute('JSError'))

    def test_extra_media(self):
        form = TestPageModelForm()
        js = [settings.TINYMCE_JS, 'django_tinymce/django_tinymce.js']
        js += settings.TINYMCE_EXTRA_MEDIA['js']
        css = {'all': ['test.css']}
        assert form.media._js == js
        assert form.media._css == css

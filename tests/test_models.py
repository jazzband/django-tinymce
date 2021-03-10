from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.test import SimpleTestCase

from tests.testapp.models import TestModel
from tinymce.widgets import AdminTinyMCE


class TestModels(SimpleTestCase):
    def setUp(self):
        self.site = AdminSite()

    def test_htmlfield(self):
        ma = admin.ModelAdmin(TestModel, self.site)
        self.assertIsInstance(ma.get_form(None).base_fields["foobar"].widget, AdminTinyMCE)

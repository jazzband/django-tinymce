from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.test import TestCase

from tinymce.widgets import AdminTinyMCE

from .models import TestModel


class TestModels(TestCase):
    def setUp(self):
        self.site = AdminSite()

    def test_htmlfield(self):
        ma = admin.ModelAdmin(TestModel, self.site)
        self.assertIsInstance(ma.get_form(None).base_fields["foobar"].widget, AdminTinyMCE)

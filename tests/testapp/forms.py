
from django import forms

from tinymce.widgets import TinyMCE

from tests.testapp.models import TestPage


class TestPageModelForm(forms.ModelForm):
    class Meta:
        model = TestPage
        fields = ['content1']
        widgets = {
            'content1': TinyMCE
        }

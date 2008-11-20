from django import forms
from django.core.urlresolvers import reverse
from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

from testtinymce.testapp.models import TestPage
from tinymce.widgets import TinyMCE

class TinyMCEFlatPageAdmin(FlatPageAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'content':
            return forms.CharField(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
                mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')},
            ))
        return super(TinyMCEFlatPageAdmin, self).formfield_for_dbfield(db_field, **kwargs)

class TinyMCETestPageAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ('content1', 'content2'):
            return forms.CharField(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
                mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')},
            ))
        return super(TinyMCETestPageAdmin, self).formfield_for_dbfield(db_field, **kwargs)

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, TinyMCEFlatPageAdmin)
admin.site.register(TestPage, TinyMCETestPageAdmin)

from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
try:
    from django.urls import reverse
except ImportError:
    # Django < 1.10
    from django.core.urlresolvers import reverse

from tinymce.widgets import TinyMCE

from tests.testapp.models import TestPage, TestInline


class TinyMCETestInlineAdmin(admin.StackedInline):
    model = TestInline
    extra = 1

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ('content1', 'content2'):
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
                mce_attrs={
                    'external_link_list_url': reverse('tinymce-linklist')
                },
            ))
        return super(TinyMCETestInlineAdmin, self).formfield_for_dbfield(db_field, **kwargs)


class TinyMCEFlatPageAdmin(FlatPageAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'content':
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
                mce_attrs={
                    'external_link_list_url': reverse('tinymce-linklist')
                },
            ))
        return super(TinyMCEFlatPageAdmin, self).formfield_for_dbfield(db_field, **kwargs)


class TinyMCETestPageAdmin(admin.ModelAdmin):
    inlines = [TinyMCETestInlineAdmin]

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ('content1', 'content2'):
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
                mce_attrs={
                    'external_link_list_url': reverse('tinymce-linklist')
                },
            ))
        return super(TinyMCETestPageAdmin, self).formfield_for_dbfield(db_field, **kwargs)


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, TinyMCEFlatPageAdmin)
admin.site.register(TestPage, TinyMCETestPageAdmin)

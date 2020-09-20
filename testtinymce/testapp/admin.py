from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.urls import reverse

from testtinymce.testapp.models import TestInline, TestPage
from tinymce.widgets import TinyMCE


class TinyMCETestInlineAdmin(admin.StackedInline):
    model = TestInline
    extra = 1

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ("content1", "content2"):
            return db_field.formfield(
                widget=TinyMCE(
                    attrs={"cols": 80, "rows": 30},
                    mce_attrs={"external_link_list_url": reverse("tinymce-linklist")},
                )
            )
        return super().formfield_for_dbfield(db_field, **kwargs)


class TinyMCEFlatPageAdmin(FlatPageAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == "content":
            return db_field.formfield(
                widget=TinyMCE(
                    attrs={"cols": 80, "rows": 30},
                    mce_attrs={"external_link_list_url": reverse("tinymce-linklist")},
                )
            )
        return super().formfield_for_dbfield(db_field, **kwargs)


class TinyMCETestPageAdmin(admin.ModelAdmin):
    inlines = [TinyMCETestInlineAdmin]

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ("content1", "content2"):
            return db_field.formfield(
                widget=TinyMCE(
                    attrs={"cols": 80, "rows": 30},
                    mce_attrs={"external_link_list_url": reverse("tinymce-linklist")},
                )
            )
        return super().formfield_for_dbfield(db_field, **kwargs)


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, TinyMCEFlatPageAdmin)
admin.site.register(TestPage, TinyMCETestPageAdmin)

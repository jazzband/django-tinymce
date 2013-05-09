import pytest
from django.core.urlresolvers import reverse

def test_tinymce(selenium_admin_client, live_server):
    admin_url = reverse('admin:testapp_testpage_add')
    live_admin_url = live_server + admin_url
    tinymce_script = "return typeof window.tinyMCE !== 'undefined'"

    selenium_admin_client.get(live_admin_url)
    has_tinymce = selenium_admin_client.execute_script(tinymce_script)

    assert has_tinymce == True

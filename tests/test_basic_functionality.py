from django.core.urlresolvers import reverse

def test_admin_url(admin_client):
    url = reverse('admin:index')
    r = admin_client.get(url)
    assert r.status_code == 200

def test_compressor_url(admin_client):
    #/tinymce/compressor/    tinymce.views.compressor        tinymce-compressor
    url = reverse('tinymce-compressor')
    r = admin_client.get(url)
    assert r.status_code == 200

def test_filebrowser_url(admin_client):
    #/tinymce/filebrowser/   tinymce.views.filebrowser       tinymce-filebrowser
    url = reverse('tinymce-filebrowser')
    r = admin_client.get(url)
    assert r.status_code == 200

def test_flatpages_link_list_url(admin_client):
    #/tinymce/flatpages_link_list/   tinymce.views.flatpages_link_list
    url = reverse('tinymce.views.flatpages_link_list')
    r = admin_client.get(url)
    assert r.status_code == 200

#def test_tinymce_js_url(admin_client):
    #/tinymce/js/textareas/<name>/   tinymce.views.textareas_js      tinymce-js
    #url = reverse('tinymce-js')
    #r = admin_client.get(url)
    #assert r.status_code == 200

#def test_tinymce_js_lang_url(admin_client):
    #/tinymce/js/textareas/<name>/<lang>     tinymce.views.textareas_js      tinymce-js-lang
    #url = reverse('tinymce-js-lang')
    #r = admin_client.get(url)
    #assert r.status_code == 200

#def test_tinmce_preview_url(admin_client):
    #/tinymce/preview/<name>/        tinymce.views.preview   tinymce-preview
    #url = reverse('tinymce-preview')
    #r = admin_client.get(url)
    #assert r.status_code == 200

def test_spellchecker_url(admin_client):
    #/tinymce/spellchecker/  tinymce.views.spell_check
    url = reverse('tinymce.views.spell_check')
    r = admin_client.get(url)
    assert r.status_code == 200

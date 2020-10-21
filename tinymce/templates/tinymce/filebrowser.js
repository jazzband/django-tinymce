function djangoFileBrowser(callback, value, meta) {
    var url = "{{ fb_url }}?pop=5&type=" + meta.filetype;

    tinyMCE.activeEditor.windowManager.openUrl(
        {
            'title': 'Django Filebrowser',
            'url': url,
            'width': 1024,
            'height': 800,
            'onMessage': function (dialogApi, details) {
                callback(details.content)
                dialogApi.close()
            }
        },
    );
    return false
}

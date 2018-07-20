function djangoFileBrowser(field_name, url, type, win) {
    var url = "{{ fb_url }}?pop=4&type=" + type;

    tinyMCE.activeEditor.windowManager.open(
        {
            'file': url,
            'width': 820,
            'height': 500,
        },
        {
            'window': win,
            'input': field_name,
        }
    );
    return false;
}

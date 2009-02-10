function djangoFileBrowser(field_name, url, type, win) {
    var url = "{{ fb_url }}?pop=2&type=" + type;

    tinyMCE.activeEditor.windowManager.open(
        {
            'file': url,
            'width': 820,
            'height': 500,
            'resizable': "yes",
            'scrollbars': "yes",
            'inline': "no",
            'close_previous': "no"
        },
        {
            'window': win,
            'input': field_name,
            'editor_id': tinyMCE.selectedInstance.editorId
        }
    );
    return false;
}

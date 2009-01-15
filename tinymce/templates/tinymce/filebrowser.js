function DjangoFileBrowser(field_name, url, type, win) {
    var url = "{% url filebrowser-index %}?pop=2&type=" + type;

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

function djangoFileBrowser(input_id, input_value, type, win) {
    var cmsURL = "{{ fb_url }}?pop=1&type=" + type;

    var w = window,
        d = document,
        e = d.documentElement,
        g = d.getElementsByTagName('body')[0],
        x = w.innerWidth || e.clientWidth || g.clientWidth,
        y = w.innerHeight || e.clientHeight || g.clientHeight;

    w.name = input_id;

    tinymce.activeEditor.windowManager.open({
        file: cmsURL,
        width: x * 0.8,
        height: y * 0.8,
        resizable: 'yes',
        scrollbars: 'yes',
        inline: 'yes',
        close_previous: 'no',
        title: 'File Manager'
    }, {
        window: win,
        input: input_id,
        editor_id: tinyMCE.activeEditor.id
    });
    return false;
};


// function djangoFileBrowser(field_name, url, type, win) {
//     var url = "{{ fb_url }}?pop=2&type=" + type;

//     tinyMCE.activeEditor.windowManager.open(
//         {
//             'file': url,
//             'width': 820,
//             'height': 500,
//             'resizable': "yes",
//             'scrollbars': "yes",
//             'inline': "no",
//             'close_previous': "no",
//             'title': "File Browser"
//         },
//         {
//             'window': win,
//             'input': field_name,
//             // 'editor_id': tinyMCE.selectedInstance.editorId
//         }
//     );
//     return false;
// }

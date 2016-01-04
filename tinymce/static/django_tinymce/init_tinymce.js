var django = django || {
    "jQuery": jQuery.noConflict(true)
};

(function ($) {
  function initTinyMCE($e) {
    if ($e.parents('.empty-form').length == 0) {  // Don't do empty inlines
      var mce_conf = $.parseJSON($e.attr('data-mce-conf'));
      // There is no way to pass a JavaScript function as an option, because
      // all options are serialized as JSON. For any TinyMCE options that expect
      // functions, assume that we were given a function name, and resolve that
      // to a function reference using the `window` global.
      var fns = ['color_picker_callback', 'file_browser_callback', 'file_picker_callback',
            'images_dataimg_filter', 'images_upload_handler'];
      for (var i=0;i<fns.length;i++) {
        if (typeof mce_conf[fns[i]] !== undefined) {
          var fn = mce_conf[fns[i]];
          mce_conf[fns[i]] = window[fn];  // resolve function name to reference
        }
      }

      var id = $e.attr('id');
      if ('elements' in mce_conf && mce_conf['mode'] == 'exact') {
        mce_conf['elements'] = id;
      }
      if ($e.attr('data-mce-gz-conf')) {
        tinyMCE_GZ.init($.parseJSON($e.attr('data-mce-gz-conf')));
      }
      if (!tinyMCE.editors[id]) {
        tinyMCE.init(mce_conf);
      }
    }
  }

  $(function () {
    // initialize the TinyMCE editors on load
    $('.tinymce').each(function () {
      initTinyMCE($(this));
    });

    // initialize the TinyMCE editor after adding an inline
    // XXX: We don't use jQuery's click event as it won't work in Django 1.4
    document.body.addEventListener("click", function(ev) {
      if(!ev.target.parentNode || ev.target.parentNode.className.indexOf("add-row") === -1) {
        return;
      }
      var $addRow = $(ev.target.parentNode);
      setTimeout(function() {  // We have to wait until the inline is added
        $('textarea.tinymce', $addRow.parent()).each(function () {
          initTinyMCE($(this));
        });
      }, 0);
    }, true);
  });
}((typeof django === 'undefined' || typeof django.jQuery === 'undefined') && jQuery || django && django.jQuery));

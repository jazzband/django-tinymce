from tinymce.widgets import TinyMCE

def test_widget(settings):
    w = TinyMCE(profile=None)
    output = w.render('content', '', {'id': 'content'})
    default_output = u'<textarea cols="40" id="content" name="content" rows="10"></textarea>\n<script type="text/javascript">tinyMCE.init({"theme": "modern", "selector": "#content", "toolbar": "insertfile undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image | print preview media fullpage | forecolor backcolor emoticons", "plugins": "advlist autolink link image lists charmap print preview hr anchor pagebreak spellchecker searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking save table contextmenu directionality emoticons template paste textcolor"})</script>'
    assert output == default_output

def test_custom_profile(settings):
    w = TinyMCE(profile={'toolbar': ''})
    output = w.render('content', '', {'id': 'content'})
    custom_output = u'<textarea cols="40" id="content" name="content" rows="10"></textarea>\n<script type="text/javascript">tinyMCE.init({"toolbar": "", "selector": "#content"})</script>'
    assert output == custom_output

def is_installed(settings):
    """
    Check Django settings and verify that tinymce application is included
    in INSTALLED_APPS to be sure that staticfiles will work properly and
    serve required files.
    """

    if not hasattr(settings, 'INSTALLED_APPS'):
        raise RuntimeError('Django settings should contain INSTALLED_APPS.')

    if 'tinymce' not in settings.INSTALLED_APPS:
        raise RuntimeError('Add tinymce to INSTALLED_APPS in settings.')

    return True


class ConfigurationError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)


def parse_profile(profile):
    D = profile

    # directionality
    i = D.get('directionality', None)
    if i is None:
        D['directionality'] = 'ltr'
    elif i not in ('ltr', 'rtl'):
        raise ConfigurationError('directionality must be ltr or rtl')

    # browser_spellcheck
    i = D.get('browser_spellcheck', None)
    if i is None:
        D['browser_spellcheck'] = False
    elif i not in (False, True):
        raise ConfigurationError('browser_spellcheck must be True or False')

    # nowrap
    i = D.get('nowrap', None)
    if i is None:
        D['nowrap'] = False
    elif i not in (False, True):
        raise ConfigurationError('nowrap must be True or False')

    # skin
    i = D.get('skin', None)
    if i is None:
        D['skin'] = 'lightgray'

    # theme
    i = D.get('theme', None)
    if i is None:
        D['theme'] = 'modern'

    # inline
    D['inline'] = D.get('inline', False)

    # convert_fonts_to_spans
    D['convert_fonts_to_spans'] = D.get('convert_fonts_to_spans', True)

    # element_format
    i = D.get('element_format', None)
    if i is None:
        D['element_format'] = 'xhtml'
    elif i not in ('xhtml', 'html'):
        raise ConfigurationError('element_format must be xhtml or html')

    # fix_list_elements
    i = D.get('fix_list_elements', None)
    if i is None:
        D['fix_list_elements'] = False
    elif i not in (False, True):
        raise ConfigurationError('fix_list_elements must be True or False')

    # force_p_newlines
    i = D.get('force_p_newlines', None)
    if i is not None and i not in (False, True):
        raise ConfigurationError('force_p_newlines must be True or False')

    # force_hex_style_colors
    i = D.get('force_hex_style_colors', None)
    if i is not None and i not in (False, True):
        raise ConfigurationError('force_hex_style_colors must be True or False')

    # keep_styles
    i = D.get('keep_styles', None)
    if i is not None and i not in (False, True):
        raise ConfigurationError('keep_styles must be True or False')

    # protect
    i = D.get('protect', None)
    if i is not None and not (isinstance(i, tuple) or isinstance(i, list)):
        raise ConfigurationError('protect must be tuple or list')

    # schema
    i = D.get('schema', None)
    if i is not None and i not in ('html4', 'html5', 'html5-strict'):
        raise ConfigurationError('schema must be html4, html5 or html5-strict')

    # visual
    i = D.get('visual', None)
    if i is not None and i not in (False, True):
        raise ConfigurationError('visual must be True or False')

    # custom_undo_redo_levels
    i = D.get('custom_undo_redo_levels', None)
    if i is not None and not isinstance(i, int):
        raise ConfigurationError('custom_undo_redo_levels must be int')

    # menu
    i = D.get('menu', None)
    if i is not None and not isinstance(i, dict):
        raise ConfigurationError('menu must be dict')

    # statusbar
    i = D.get('statusbar', None)
    if i is not None and i not in (False, True):
        raise ConfigurationError('statusbar must be True or False')

    # resize
    i = D.get('resize', None)
    if i is not None and i not in (False, True, 'both'):
        raise ConfigurationError('resize must be True, False or "both"')

    # convert_urls
    i = D.get('convert_urls', None)
    if i is not None and i not in (False, True):
        raise ConfigurationError('convert_urls must be True or False')

    # relative_urls
    i = D.get('relative_urls', None)
    if i is not None and i not in (False, True):
        raise ConfigurationError('relative_urls must be True or False')

    # remove_script_host
    i = D.get('remove_script_host', None)
    if i is not None and i not in (False, True):
        raise ConfigurationError('remove_script_host must be True or False')

    # document_base_url
    i = D.get('document_base_url', None)
    if i is not None and (not isinstance(i, str) or not i.endswith('/')):
        raise ConfigurationError('document_base_url must be str and end with "/"')

    # file_browser_callback_types
    i = D.get('file_browser_callback_types', None)
    if i is not None:
        if not isinstance(i, str): 
            raise ConfigurationError('file_browser_callback_types must be str and combination of file, image or media')
        allowed_types = ('file', 'image', 'media')
        types = set(i.split(' '))
        if not all([(t in allowed_types) for t in types]):
            raise ConfigurationError('file_browser_callback_types must be str and combination of file, image or media')

    return D

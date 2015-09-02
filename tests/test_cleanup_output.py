import pytest
from pytest import raises
from tinymce.utils import parse_profile, ConfigurationError

def test_convert_fonts_to_spans():
    profile = {}
    P = parse_profile(profile)
    assert 'convert_fonts_to_spans' in P
    assert P['convert_fonts_to_spans'] == True

    profile = {'convert_fonts_to_spans': True}
    P = parse_profile(profile)
    assert 'convert_fonts_to_spans' in P
    assert P['convert_fonts_to_spans'] == True

    profile = {'convert_fonts_to_spans': False}
    P = parse_profile(profile)
    assert 'convert_fonts_to_spans' in P
    assert P['convert_fonts_to_spans'] == False

def test_custom_elements():
    # FIXME: check docs
    profile = {}
    P = parse_profile(profile)
    assert 'custom_elements' not in P

    profile = {'custom_elements': 'el1,el2'}
    P = parse_profile(profile)
    assert 'custom_elements' in P
    assert P['custom_elements'] == 'el1,el2'

def test_doctype():
    profile = {}
    P = parse_profile(profile)
    assert 'doctype' not in P

    profile = {'doctype': 'lol'}
    P = parse_profile(profile)
    assert 'doctype' in P

def test_element_format():
    profile = {}
    P = parse_profile(profile)
    assert 'element_format' in P
    assert P['element_format'] == 'xhtml'

    profile = {'element_format': 'xhtml'}
    P = parse_profile(profile)
    assert 'element_format' in P
    assert P['element_format'] == 'xhtml'

    profile = {'element_format': 'html'}
    P = parse_profile(profile)
    assert 'element_format' in P
    assert P['element_format'] == 'html'

    profile = {'element_format': 'lol'}
    with raises(ConfigurationError) as ex:
        P = parse_profile(profile)

def test_entities():
    profile = {}
    P = parse_profile(profile)
    assert 'entities' not in P

    profile = {'entities': '160,nbsp,162,cent,8364,euro,163,pound'}
    P = parse_profile(profile)
    assert 'entities' in P
    assert P['entities'] == '160,nbsp,162,cent,8364,euro,163,pound'

def test_entity_encoding():
    # FIXME: check default state
    choices = ('named', 'numeric', 'raw', 'named+numeric')

    profile = {}
    P = parse_profile(profile)
    assert 'entity_encoding' not in P

    profile = {'entity_encoding': 'raw'}
    P = parse_profile(profile)
    assert 'entity_encoding' in P
    assert P['entity_encoding'] == 'raw'

def test_extended_valid_elements():
    profile = {}
    P = parse_profile(profile)
    assert 'extended_valid_elements' not in P

    profile = {'extended_valid_elements': 'img[class|src|name]'}
    P = parse_profile(profile)
    assert 'extended_valid_elements' in P
    assert P['extended_valid_elements'] == 'img[class|src|name]'

def test_fix_list_elements():
    profile = {}
    P = parse_profile(profile)
    assert 'fix_list_elements' in P
    assert P['fix_list_elements'] == False

    profile = {'fix_list_elements': False}
    P = parse_profile(profile)
    assert 'fix_list_elements' in P
    assert P['fix_list_elements'] == False

    profile = {'fix_list_elements': True}
    P = parse_profile(profile)
    assert 'fix_list_elements' in P
    assert P['fix_list_elements'] == True

    profile = {'fix_list_elements': 'lol'}
    with raises(ConfigurationError) as ex:
        P = parse_profile(profile)

def test_font_formats():
    profile = {}
    P = parse_profile(profile)
    assert 'font_formats' not in P

    profile = {'font_formats': 'lol'}
    P = parse_profile(profile)
    assert 'font_formats' in P
    assert P['font_formats'] == 'lol'

def test_fontsize_formats():
    # FIXME: check default state
    profile = {}
    P = parse_profile(profile)
    assert 'fontsize_formats' not in P

    fontsize_formats = "8pt 10pt 12pt 14pt 18pt 24pt 36pt"
    profile = {'fontsize_formats': fontsize_formats}
    P = parse_profile(profile)
    assert 'fontsize_formats' in P
    assert P['fontsize_formats'] == fontsize_formats

def test_force_p_newlines():
    # FIXME: check default state
    profile = {}
    P = parse_profile(profile)
    assert 'force_p_newlines' not in P
    #assert P['force_p_newlines'] == True

    profile = {'force_p_newlines': True}
    P = parse_profile(profile)
    assert 'force_p_newlines' in P
    assert P['force_p_newlines'] == True

    profile = {'force_p_newlines': False}
    P = parse_profile(profile)
    assert 'force_p_newlines' in P
    assert P['force_p_newlines'] == False

    profile = {'force_p_newlines': 'lol'}
    with raises(ConfigurationError) as ex:
        P = parse_profile(profile)

def test_force_hex_style_colors():
    profile = {}
    P = parse_profile(profile)
    assert 'force_hex_style_colors' not in P

    profile = {'force_hex_style_colors': True}
    P = parse_profile(profile)
    assert P['force_hex_style_colors'] == True

    profile = {'force_hex_style_colors': False}
    P = parse_profile(profile)
    assert P['force_hex_style_colors'] == False

    profile = {'force_hex_style_colors': 'lol'}
    with raises(ConfigurationError) as ex:
        P = parse_profile(profile)

def test_forced_root_block():
    profile = {}
    P = parse_profile(profile)
    assert 'forced_root_block' not in P

    profile = {'forced_root_block': 'p'}
    P = parse_profile(profile)
    assert P['forced_root_block'] == 'p'

    profile = {'forced_root_block': False}
    P = parse_profile(profile)
    assert P['forced_root_block'] == False

def test_forced_root_block_attrs():
    profile = {}
    P = parse_profile(profile)
    assert 'forced_root_block_attrs' not in P

    profile = {'forced_root_block_attrs': {'lol': 'lol'}}
    P = parse_profile(profile)
    assert 'forced_root_block_attrs' in P
    assert P['forced_root_block_attrs'] == {'lol': 'lol'}

def test_formats():
    # FIXME: check docs
    pass

def test_indentation():
    profile = {}
    P = parse_profile(profile)
    assert 'indentation' not in P

    profile = {'indentation': '20pt'}
    P = parse_profile(profile)
    assert P['indentation'] == '20pt'

def test_invalid_elements():
    profile = {}
    P = parse_profile(profile)
    assert 'invalid_elements' not in P

    profile = {'invalid_elements': 'em,i'}
    P = parse_profile(profile)
    assert P['invalid_elements'] == 'em,i'

def test_invalid_styles():
    profile = {}
    P = parse_profile(profile)
    assert 'invalid_styles' not in P

    profile = {'invalid_styles': 'lol'}
    P = parse_profile(profile)
    assert P['invalid_styles'] == 'lol'

def test_keep_styles():
    profile = {}
    P = parse_profile(profile)
    assert 'keep_styles' not in P

    profile = {'keep_styles': False}
    P = parse_profile(profile)
    assert P['keep_styles'] == False

    profile = {'keep_styles': 'lol'}
    with raises(ConfigurationError) as ex:
        P = parse_profile(profile)

def test_protect():
    profile = {}
    P = parse_profile(profile)
    assert 'protect' not in P

    profile = {'protect': ['a', 'b']}
    P = parse_profile(profile)
    assert P['protect'] == ['a', 'b']

    profile = {'protect': ('a', 'b')}
    P = parse_profile(profile)
    assert P['protect'] == ('a', 'b')

    profile = {'protect': 'lol'}
    with raises(ConfigurationError) as ex:
        P = parse_profile(profile)

def test_schema():
    profile = {}
    P = parse_profile(profile)
    assert 'schema' not in P

    profile = {'schema': 'html5'}
    P = parse_profile(profile)
    assert P['schema'] == 'html5'

    profile = {'schema': 'lol'}
    with raises(ConfigurationError) as ex:
        P = parse_profile(profile)

def test_style_formats():
    # FIXME: check docs
    pass

def test_block_formats():
    profile = {}
    P = parse_profile(profile)
    assert 'block_formats' not in P

    profile = {'block_formats': 'lol'}
    P = parse_profile(profile)
    assert P['block_formats'] == 'lol'

def test_valid_children():
    profile = {}
    P = parse_profile(profile)
    assert 'valid_children' not in P

    profile = {'valid_children': 'lol'}
    P = parse_profile(profile)
    assert P['valid_children'] == 'lol'

def test_valid_elements():
    profile = {}
    P = parse_profile(profile)
    assert 'valid_elements' not in P

    profile = {'valid_elements': 'lol'}
    P = parse_profile(profile)
    assert P['valid_elements'] == 'lol'

def test_valid_styles():
    profile = {}
    P = parse_profile(profile)
    assert 'valid_styles' not in P

    profile = {'valid_styles': 'lol'}
    P = parse_profile(profile)
    assert P['valid_styles'] == 'lol'

def test_valid_classes():
    profile = {}
    P = parse_profile(profile)
    assert 'valid_classes' not in P

    profile = {'valid_classes': 'lol'}
    P = parse_profile(profile)
    assert P['valid_classes'] == 'lol'

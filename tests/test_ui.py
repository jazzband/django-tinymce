import pytest
from pytest import raises
from tinymce.utils import parse_profile, ConfigurationError

def test_toolbar():
    # FIXME: check docs, test all
    profile = {}
    P = parse_profile(profile)
    assert 'toolbar' not in P

    profile = {'toolbar': 'lol'}
    P = parse_profile(profile)
    assert P['toolbar'] == 'lol'

def test_toolbar_n():
    pass

def test_menubar():
    profile = {}
    P = parse_profile(profile)
    assert 'menubar' not in P

    profile = {'menubar': False}
    P = parse_profile(profile)
    assert P['menubar'] == False

    profile = {'menubar': 'lol'}
    P = parse_profile(profile)
    assert P['menubar'] == 'lol'

def test_menu():
    profile = {}
    P = parse_profile(profile)
    assert 'menu' not in P

    profile = {'menu': {}}
    P = parse_profile(profile)
    assert P['menu'] == {}

    profile = {'menu': 'lol'}
    with raises(ConfigurationError):
        P = parse_profile(profile)

def test_statusbar():
    profile = {}
    P = parse_profile(profile)
    assert 'statusbar' not in P

    profile = {'statusbar': False}
    P = parse_profile(profile)
    assert P['statusbar'] == False

    profile = {'statusbar': 'lol'}
    with raises(ConfigurationError):
        P = parse_profile(profile)

def test_resize():
    profile = {}
    P = parse_profile(profile)
    assert 'resize' not in P

    profile = {'resize': True}
    P = parse_profile(profile)
    assert P['resize'] == True

    profile = {'resize': False}
    P = parse_profile(profile)
    assert P['resize'] == False

    profile = {'resize': 'both'}
    P = parse_profile(profile)
    assert P['resize'] == 'both'

    profile = {'resize': 'lol'}
    with raises(ConfigurationError):
        P = parse_profile(profile)

def test_width():
    profile = {}
    P = parse_profile(profile)
    assert 'width' not in P

    profile = {'width': 500}
    P = parse_profile(profile)
    assert P['width'] == 500

def test_height():
    profile = {}
    P = parse_profile(profile)
    assert 'height' not in P

    profile = {'height': 500}
    P = parse_profile(profile)
    assert P['height'] == 500

def test_preview_styles():
    profile = {}
    P = parse_profile(profile)
    assert 'preview_styles' not in P

    profile = {'preview_styles': True}
    P = parse_profile(profile)
    assert P['preview_styles'] == True

    profile = {'preview_styles': False}
    P = parse_profile(profile)
    assert P['preview_styles'] == False

def test_fixed_toolbar_container():
    profile = {}
    P = parse_profile(profile)
    assert 'fixed_toolbar_container' not in P

    profile = {'fixed_toolbar_container': 'lol'}
    P = parse_profile(profile)
    assert P['fixed_toolbar_container'] == 'lol'

def test_event_root():
    profile = {}
    P = parse_profile(profile)
    assert 'event_root' not in P

    profile = {'event_root': 'lol'}
    P = parse_profile(profile)
    assert P['event_root'] == 'lol'

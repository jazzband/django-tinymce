import pytest
from pytest import raises
from tinymce.utils import parse_profile, ConfigurationError


def test_auto_focus():
    profile = {}
    P = parse_profile(profile)
    assert 'auto_focus' not in P

    profile = {'auto_focus': 'elm1'}
    P = parse_profile(profile)
    assert 'auto_focus' in P
    assert P.get('auto_focus') == 'elm1'

def test_directionality():
    profile = {}
    P = parse_profile(profile)
    assert 'directionality' in P
    assert P['directionality'] == 'ltr'

    profile = {'directionality': 'ltr'}
    P = parse_profile(profile)
    assert 'directionality' in P
    assert P['directionality'] == 'ltr'

    profile = {'directionality': 'rtl'}
    P = parse_profile(profile)
    assert 'directionality' in P
    assert P['directionality'] == 'rtl'

    profile = {'directionality': 'lol'}
    with raises(ConfigurationError) as ex:
        P = parse_profile(profile)

def test_browser_spellcheck():
    profile = {}
    P = parse_profile(profile)
    assert 'browser_spellcheck' in P
    assert P['browser_spellcheck'] == False

    profile = {'browser_spellcheck': False}
    P = parse_profile(profile)
    assert 'browser_spellcheck' in P
    assert P['browser_spellcheck'] == False

    profile = {'browser_spellcheck': True}
    P = parse_profile(profile)
    assert 'browser_spellcheck' in P
    assert P['browser_spellcheck'] == True

    profile = {'browser_spellcheck': 'lol'}
    with raises(ConfigurationError) as ex:
        P = parse_profile(profile)

def test_language():
    # FIXME: check issues
    pass

def test_language_url():
    profile = {}
    P = parse_profile(profile)
    assert 'language_url' not in P

    profile = {'language_url': 'lol'}
    P = parse_profile(profile)
    assert 'language_url' in P

def test_nowrap():
    profile = {}
    P = parse_profile(profile)
    assert 'nowrap' in P
    assert P['nowrap'] == False

    profile = {'nowrap': False}
    P = parse_profile(profile)
    assert 'nowrap' in P
    assert P['nowrap'] == False

    profile = {'nowrap': True}
    P = parse_profile(profile)
    assert 'nowrap' in P
    assert P['nowrap'] == True

    profile = {'nowrap': 'lol'}
    with raises(ConfigurationError) as ex:
        P = parse_profile(profile)

def test_object_resizing():
    # FIXME: check default options in tinymce
    profile = {}
    P = parse_profile(profile)
    assert 'object_resizing' not in P

    profile = {'object_resizing': 'img'}
    P = parse_profile(profile)
    assert 'object_resizing' in P
    assert P['object_resizing'] == 'img'

def test_plugins():
    # FIXME: check all plugins
    profile = {}
    P = parse_profile(profile)
    assert 'plugins' not in P

def test_external_plugins():
    profile = {}
    P = parse_profile(profile)
    assert 'external_plugins' not in P

    profile = {
        'external_plugins': {
            'myplugin': '/external/plugin.js',
        }
    }
    P = parse_profile(profile)
    assert 'external_plugins' in P
    assert P['external_plugins'] == {'myplugin': '/external/plugin.js'}

def test_selector():
    profile = {}
    P = parse_profile(profile)
    assert 'selector' not in P

    profile = {'selector': 'textarea'}
    P = parse_profile(profile)
    assert 'selector' in P
    assert P['selector'] == 'textarea'

def test_skin():
    profile = {}
    P = parse_profile(profile)
    assert 'skin' in P
    assert P['skin'] == 'lightgray'

    profile = {'skin': 'lol'}
    P = parse_profile(profile)
    assert 'skin' in P
    assert P['skin'] == 'lol'

def test_skin_url():
    profile = {}
    P = parse_profile(profile)
    assert 'skin_url' not in P

    profile = {'skin_url': '/skin/'}
    P = parse_profile(profile)
    assert 'skin_url' in P

def test_theme():
    profile = {}
    P = parse_profile(profile)
    assert 'theme' in P
    assert P['theme'] == 'modern'

    profile = {'theme': 'lol'}
    P = parse_profile(profile)
    assert 'theme' in P
    assert P['theme'] == 'lol'

def test_theme_url():
    profile = {}
    P = parse_profile(profile)
    assert 'theme_url' not in P

    profile = {'theme_url': '/theme/url/'}
    P = parse_profile(profile)
    assert 'theme_url' in P
    assert P['theme_url'] == '/theme/url/'

def test_inline():
    profile = {}
    P = parse_profile(profile)
    assert 'inline' in P
    assert P['inline'] == False

    profile = {'inline': True}
    P = parse_profile(profile)
    assert 'inline' in P
    assert P['inline'] == True

def test_hidden_input():
    # FIXME: check what's default
    profile = {}
    P = parse_profile(profile)
    assert 'hidden_input' not in P

    profile = {'hidden_input': False}
    P = parse_profile(profile)
    assert 'hidden_input' in P
    assert P['hidden_input'] == False

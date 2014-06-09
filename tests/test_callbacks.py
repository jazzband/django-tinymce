import pytest
from pytest import raises
from tinymce.utils import parse_profile, ConfigurationError

def test_file_browser_callback():
    profile = {}
    P = parse_profile(profile)
    assert 'file_browser_callback' not in P

    profile = {'file_browser_callback': 'lol'}
    P = parse_profile(profile)
    assert P['file_browser_callback'] == 'lol'

def test_file_browser_callback_types():
    profile = {}
    P = parse_profile(profile)
    assert 'file_browser_callback_types' not in P

    profile = {'file_browser_callback_types': 'file image media'}
    P = parse_profile(profile)
    assert P['file_browser_callback_types'] == 'file image media'

    profile = {'file_browser_callback_types': 'lol'}
    with raises(ConfigurationError):
        P = parse_profile(profile)

def test_init_instance_callback():
    profile = {}
    P = parse_profile(profile)
    assert 'init_instance_callback' not in P

    profile = {'init_instance_callback': 'lol'}
    P = parse_profile(profile)
    assert P['init_instance_callback'] == 'lol'

def test_setup():
    profile = {}
    P = parse_profile(profile)
    assert 'setup' not in P

    profile = {'setup': 'lol'}
    P = parse_profile(profile)
    assert P['setup'] == 'lol'

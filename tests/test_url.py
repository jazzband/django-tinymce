import pytest
from pytest import raises
from tinymce.utils import parse_profile, ConfigurationError

def test_convert_urls():
    profile = {}
    P = parse_profile(profile)
    assert 'convert_urls' not in P

    profile = {'convert_urls': False}
    P = parse_profile(profile)
    assert P['convert_urls'] == False

    profile = {'convert_urls': 'lol'}
    with raises(ConfigurationError):
        P = parse_profile(profile)

def test_relative_urls():
    profile = {}
    P = parse_profile(profile)
    assert 'relative_urls' not in P

    profile = {'relative_urls': False}
    P = parse_profile(profile)
    assert P['relative_urls'] == False

    profile = {'relative_urls': 'lol'}
    with raises(ConfigurationError):
        P = parse_profile(profile)

def test_remove_script_host():
    profile = {}
    P = parse_profile(profile)
    assert 'remove_script_host' not in P

    profile = {'remove_script_host': False}
    P = parse_profile(profile)
    assert P['remove_script_host'] == False

    profile = {'remove_script_host': 'lol'}
    with raises(ConfigurationError):
        P = parse_profile(profile)

def test_document_base_url():
    profile = {}
    P = parse_profile(profile)
    assert 'document_base_url' not in P

    profile = {'document_base_url': '/path/'}
    P = parse_profile(profile)
    assert P['document_base_url'] == '/path/'

    profile = {'document_base_url': 'lol'}
    with raises(ConfigurationError):
        P = parse_profile(profile)

def test_allow_script_urls():
    # FIXME: access denied in docs
    pass

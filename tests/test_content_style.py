import pytest
from pytest import raises
from tinymce.utils import parse_profile, ConfigurationError

def test_body_id():
    profile = {}
    P = parse_profile(profile)
    assert 'body_id' not in P

    profile = {'body_id': 'lol'}
    P = parse_profile(profile)
    assert P['body_id'] == 'lol'

def test_body_class():
    profile = {}
    P = parse_profile(profile)
    assert 'body_class' not in P

    profile = {'body_class': 'lol'}
    P = parse_profile(profile)
    assert P['body_class'] == 'lol'

def test_content_css():
    profile = {}
    P = parse_profile(profile)
    assert 'content_css' not in P

    profile = {'content_css': 'lol'}
    P = parse_profile(profile)
    assert P['content_css'] == 'lol'

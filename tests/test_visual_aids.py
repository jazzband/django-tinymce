import pytest
from pytest import raises
from tinymce.utils import parse_profile, ConfigurationError

def test_visual():
    profile = {}
    P = parse_profile(profile)
    assert 'visual' not in P

    profile = {'visual': True}
    P = parse_profile(profile)
    assert P['visual'] == True

    profile = {'visual': False}
    P = parse_profile(profile)
    assert P['visual'] == False

    profile = {'visual': 'lol'}
    with raises(ConfigurationError):
        P = parse_profile(profile)

def test_visual_table_class():
    profile = {}
    P = parse_profile(profile)
    assert 'visual_table_class' not in P

    profile = {'visual_table_class': 'lol'}
    P = parse_profile(profile)
    assert P['visual_table_class'] == 'lol'

def test_visual_anchor_class():
    profile = {}
    P = parse_profile(profile)
    assert 'visual_anchor_class' not in P

    profile = {'visual_anchor_class': 'lol'}
    P = parse_profile(profile)
    assert P['visual_anchor_class'] == 'lol'

import pytest
from pytest import raises
from tinymce.utils import parse_profile, ConfigurationError

def test_custom_undo_redo_levels():
    profile = {}
    P = parse_profile(profile)
    assert 'custom_undo_redo_levels' not in P

    profile = {'custom_undo_redo_levels': 10}
    P = parse_profile(profile)
    assert P['custom_undo_redo_levels'] == 10

    profile = {'custom_undo_redo_levels': 'lol'}
    with raises(ConfigurationError):
        P = parse_profile(profile)

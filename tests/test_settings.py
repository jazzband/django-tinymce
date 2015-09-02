import pytest
from pytest import raises
from tinymce.utils import is_installed


def test_settings(settings):
    with raises(RuntimeError):
        is_installed(settings)

    settings.INSTALLED_APPS = ('tinymce',)
    assert is_installed(settings) == True

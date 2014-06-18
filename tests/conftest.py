import pytest
from django.conf import settings

def pytest_configure():
    settings.configure(
        STATIC_URL='/static/'
    )

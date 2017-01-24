# -*- coding:utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import os
import random
import string

import pytest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

browsers = {
    # 'firefox': webdriver.Firefox,
    # 'chrome': webdriver.Chrome,
    'phantomjs': webdriver.PhantomJS,
}


def random_string(n):
    return ''.join(
        random.choice(string.ascii_uppercase + string.digits)
        for _ in range(n)
    )


@pytest.fixture(scope='session',
                params=browsers.keys())
def driver(request):
    if 'DISPLAY' not in os.environ:
        pytest.skip('Test requires display server (export DISPLAY)')

    try:
        b = browsers[request.param]()
    except WebDriverException as e:
        pytest.skip(e)
    else:
        b.set_window_size(1200, 800)
        request.addfinalizer(lambda *args: b.quit())
        return b


@pytest.fixture
def testpages(db):
    from tests.testapp.models import TestPage

    return TestPage.objects.bulk_create(
        [TestPage(pk=pk, content1=random_string(50), content2=random_string(50)) for pk in range(10)]
    )


@pytest.fixture
def flatpages(db):
    from django.contrib.flatpages.models import FlatPage

    return FlatPage.objects.bulk_create(
        [FlatPage(pk=pk, title=random_string(50), url=random_string(50)) for pk in range(1)]
    )

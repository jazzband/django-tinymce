import pytest
from selenium.webdriver.phantomjs.webdriver import WebDriver
from django.core.urlresolvers import reverse

@pytest.fixture
def selenium_admin_client(live_server, admin_client):
    """
    Provides Selenium WebDriver with authenticated Django admin user.
    """

    sessionid = admin_client.cookies['sessionid']
    cookie = {
        'name': sessionid.key,
        'value': sessionid.value,
        'path': '/',
        'secure': False
    }

    selenium = WebDriver()
    selenium.get(live_server + reverse('admin:index'))
    selenium.delete_cookie('sessionid')
    selenium.add_cookie(cookie)

    return selenium

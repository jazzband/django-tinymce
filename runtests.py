import os
import sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'testtinymce.settings'
test_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, test_dir)

import django
from django.conf import settings
from django.test.utils import get_runner


def runtests():
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=1, interactive=True)
    failures = test_runner.run_tests(['tinymce'])
    sys.exit(bool(failures))

if __name__ == '__main__':
    runtests()

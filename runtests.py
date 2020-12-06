import argparse
import os
import sys

# Force this to happen before loading django
try:
    os.environ["DJANGO_SETTINGS_MODULE"] = "testtinymce.settings"
    test_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, test_dir)
except ImportError:
    pass
else:
    import django
    from django.conf import settings
    from django.test.utils import get_runner


def runtests(modules=["tinymce"], verbosity=1, failfast=False):
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner(interactive=True, verbosity=verbosity, failfast=failfast)
    failures = test_runner.run_tests(modules)
    sys.exit(bool(failures))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the django-tinymce test suite.")
    parser.add_argument(
        "modules",
        nargs="*",
        metavar="module",
        help='Optional path(s) to test modules; e.g. "tinymce" or '
        '"tinymce.tests.test_widgets".',
    )
    parser.add_argument(
        "-v",
        "--verbosity",
        default=1,
        type=int,
        choices=[0, 1, 2, 3],
        help="Verbosity level; 0=minimal output, 1=normal output, 2=all output",
    )
    parser.add_argument(
        "--failfast",
        action="store_true",
        help="Stop running the test suite after first failed test.",
    )
    options = parser.parse_args()
    runtests(modules=options.modules, verbosity=options.verbosity, failfast=options.failfast)

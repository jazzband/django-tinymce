#!/usr/bin/env python
import os
import sys

try:
    os.environ["DJANGO_SETTINGS_MODULE"] = "testtinymce.settings"
    test_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, test_dir)
except ImportError:
    pass
else:
    from django.core.management import execute_from_command_line


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "%s.settings" % __package__)
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()

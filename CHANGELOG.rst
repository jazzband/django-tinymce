Changelog
#########

This document describes changes between each past release.

3.7.1 (2024-02-06)
==================

- Reintroduce the ``MANIFEST.in`` file to properly build the package.
  Release 3.7.0 on PyPI was unusable (#454).

3.7.0 (2024-02-06)
==================

- Drop support for Django 2.2, 4.0, and 4.1.
- Add support for Django 4.2 and 5.0.
- Drop support for Python 3.7 and add support for Python 3.11 and 3.12.
- New ``pyproject.toml`` replaces the legacy ``setup.py`` project config.
- Use staticfiles storage API to find tinymce location (#420). It was already
  done in 3.6.0, but had to be reverted in 3.6.1 (see #430).
- Fixed selector usage for elements with ``__prefix__`` (typically inlines).
- ``TINYMCE_JS_ROOT`` setting has been removed.

3.6.1 (2023-03-20)
==================

- Fixed a regression by reverting usage of staticfiles to find tinymce
  location (#420, #430).

3.6.0 (2023-03-18)
==================

- Upgrade embedded tinyMCE from 5.10.1 to 5.10.7
- Replace obsolete mode and elements by selector and target (#417)
- Detect non-installed tinyMCE soon in init_tinymce.js
- Stop installing the tests directory (#355)
- Add support for translatable strings in tinyMCE config
- Use staticfiles storage API to find tinymce location (#420)

3.5.0 (2022-08-27)
==================

- Support new non-jQuery formset:added event triggered on Django 4.1
- Replace an obsolete call to tinyMCE.editors (#391)
- Confirm support for Django 4.0 and 4.1
- Drop support for Django 3.0, 3.1 and Python 3.6
- Add Python 3.10 support

3.4.0 (2021-11-25)
==================

- Upgrade to TinyMCE 5.10.1
- Confirmed support for Django 3.2
- Repair the spellchecker plugin functionality.


3.3.0 (2021-03-24)
==================

- Add support for Django 3.1
- Improve detection of dynamically added formsets
- Update configuration documentation


3.2.0 (2020-12-10)
==================

- Remove support for universal builds
- Add compatibility of django-filebrowser with tinymce 5
- Load the CHANGELOG in the documentation front page
- Fix en_US language loading
- Speed up tests by removing the loading of a database
- Add verbosity option to tests
- Assume TinyMCE files are utf-8 encoded


3.1.0 (2020-09-29)
==================

- Add support for language configuration
- Upgrade to TinyMCE 5.5.0
- Remove the jQuery dependency and fix multiples errors around that

  .. note::
     As a consequence, ``TINYMCE_INCLUDE_JQUERY`` setting has been removed.

- Move to the Jazzband organization


3.0.2 (2020-04-22)
==================

- Update the default config.


3.0.0 (2020-04-10)
==================

- Upgrade to TinyMCE 5
- Fix compressor


2.9.0 (2020-04-10)
==================

- Upgrade test matrix to Python 3.7 and Django 2.1, 2.2
- Add support for TinyMCE FileBrowser 4.0
- Remove support for South


2.8.0 (2019-01-15)
==================

- Use the attrs set on instantiation as well as the attrs passed to render (#237)


2.7.0 (2017-12-19)
==================

- Drop support for Django 1.7, 1.8, 1.9 and 1.10.
- Django 1.11 is still supported but issues a deprecation warning.
- Add support for Django 2.0
- Added INCLUDE_JQUERY setting to decide whether TinyMCE.media should include
  a jQuery release (#190).


2.6.0 (2017-01-23)
==================

- Avoid deprecation warning with django.core.urlresolvers (#188)
- Fixed a client-side validation issue when the TinyMCE widget has the HTML
  required attribute set (#187).
- Fixed a crash when no languages are activated (#175).


2.5.0 (2017-01-23)
==================

- Added compatibility for Django 1.11.
- Dropped support for Django 1.6.


2.4.0 (2016-08-31)
==================

- Added compatibility for Django 1.10.
- Fix JQuery Problem with grappelli
- Fix Python 3 compatibility (#170)
- Improve documentation (#163, #171)
- Cleaned Imports (#182)
- Fix TinyMCE Widget for ModelTranslation tabs (#174)
- Fix JSON mimetype (#186)


2.3.0 (2016-03-10)
==================

- Added tests (#149)
- Improved Python3 support


2.2.0 (2015-12-23)
==================

- TinyMCE compressor now use staticfiles to get the file content (and
  to find files that are in multiple static directory.) (#142)


2.1.0 (2015-12-23)
==================

- Rewrite URL files to let it works with Django 1.9 (#147, #148)
- Add a CONTRIBUTORS file.


2.0.6 (2015-11-12)
==================

- Make sure jQuery is loaded both in the admin and for non-admin forms. (#141)


2.0.5 (2015-09-09)
==================

- Use static finders for development mode. (#131)


2.0.4 (2015-08-07)
==================

- Fix non-admin jQuery.


2.0.3 (2015-08-06)
==================

- Handle non-admin jQuery. (#108)


2.0.2 (2015-07-26)
==================

- Add Python3 support.


2.0.1 (2015-07-24)
==================

- Fix missing CHANGELOG.


2.0.0 (2015-07-23)
==================

* Starts supporting Django 1.8

Older Changelog entries can be found on
https://github.com/jazzband/django-tinymce/blob/3.1.0/docs/history.rst

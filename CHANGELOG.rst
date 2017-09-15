Changelog
#########

This document describes changes between each past release.


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

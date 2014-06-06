def is_installed(settings):
    """
    Check Django settings and verify that tinymce application is included in INSTALLED_APPS to be sure that staticfiles will work properly and serve required files.
    """

    if not hasattr(settings, 'INSTALLED_APPS'):
        raise RuntimeError('Django settings should contain INSTALLED_APPS.')

    if 'tinymce' not in settings.INSTALLED_APPS:
        raise RuntimeError('Add tinymce to INSTALLED_APPS in settings.')

    return True

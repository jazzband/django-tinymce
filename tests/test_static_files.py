import tempfile

from django.core.management import call_command
from django.test import SimpleTestCase


class TestStaticFiles(SimpleTestCase):

    def test_manifest_static_files_storage(self):
        """
        Test that TinyMCE's static files can be collected
        when using ManifestStaticFilesStorage - missing
        .map files can cause this to fail if the static
        files refer to them (GH issue #460)
        """
        with tempfile.TemporaryDirectory() as temp_dir:
            with self.settings(
                STATIC_ROOT=temp_dir,
                STATICFILES_STORAGE="django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
            ):
                result = call_command("collectstatic", "--no-input")
                self.assertRegex(result, r"\d+ static files copied")

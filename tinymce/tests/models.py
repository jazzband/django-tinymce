
from django.db import models
from tinymce import models as tinymce_models


class TestModel(models.Model):
    foobar = tinymce_models.HTMLField()

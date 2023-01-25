from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime

class Article(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    content = RichTextField(config_name='awesome_ckeditor')
    created_at = models.DateTimeField(default=datetime.now, blank=False)
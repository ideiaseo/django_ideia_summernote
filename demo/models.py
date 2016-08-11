from __future__ import unicode_literals

from django.db import models

# Create your models here.
from ideia_summernote.fields import SummernoteField


class Book(models.Model):

    title = models.CharField(null=False, blank=False, max_length=100)
    text = SummernoteField(null=False, blank=False)

    class Meta:
        ordering = ['-id']
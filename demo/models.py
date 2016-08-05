from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Book(models.Model):

    title = models.CharField(null=False, blank=False, max_length=100)
    text = models.TextField(null=False, blank=False)
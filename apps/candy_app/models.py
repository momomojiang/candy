from __future__ import unicode_literals
from django.db import models

# Create your models here.

# class IMG(models.Model):
#     img = models.ImageField(upload_to='upload')

class Comment(models.Model):
    comment = models.CharField(max_length = 255)
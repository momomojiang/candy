from __future__ import unicode_literals
from django.db import models
from ..login.models import User
from .models import *

# Create your models here.

class MessageManager(models.Manager):
    def message_validator(sefl,postData):
        errors={}
        if len(postData['message'])<10:
            errors['message']="Message filed should more than 10 characters"
        return errors
    def create_message(self, postData):
        message = Message.objects.create(message=postData['message'],poster=poster)

class Message(models.Model):
    message = models.CharField(max_length=125)
    poster = models.ForeignKey(User, related_name="created_message",null=True)
    objects = MessageManager()
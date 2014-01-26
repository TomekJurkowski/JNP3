from django.db import models
from django.template.defaultfilters import slugify
import os

# Create your models here.

def upload_to(path, attribute):
    def upload_callback(instance, filename):
        return '%s%s/%s' % (path, unicode(slugify(getattr(instance, attribute))), filename)
    return upload_callback

class Post(models.Model):
    post_id = models.IntegerField()
    author_name = models.CharField(max_length=32)
    author_email = models.EmailField(max_length=128)
    post_subject = models.CharField(max_length=64)
    post_body = models.TextField(max_length=2048)
    image = models.ImageField(upload_to=upload_to('thread/', 'post_id'), blank=True)

class Reply(models.Model):
    reply_id = models.IntegerField()
    op_post_id = models.IntegerField()
    reply_name = models.CharField(max_length=32)
    reply_email = models.CharField(max_length=128)
    reply_body = models.TextField(max_length=2048)
    image = models.ImageField(upload_to=upload_to('thread/answers/', 'reply_id'), blank=True)

class GlobalId(models.Model):
    global_id = models.IntegerField()
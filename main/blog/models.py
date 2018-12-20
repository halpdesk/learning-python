from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
import re

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

class User(models.Model):
    username    = models.CharField(max_length=64)
    password    = models.CharField(max_length=128)
    created_at  = models.DateTimeField(auto_now=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class Post(models.Model):
    title       = models.CharField(max_length=64, default='')
    excerpt     = models.CharField(max_length=256, default='')
    body        = models.CharField(max_length=4096, default='')
    user        = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
        null=True
    )
    created_at  = models.DateTimeField(auto_now=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post     = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
    comment  = models.CharField(max_length=512, default='')
    created_at  = models.DateTimeField(auto_now=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return re.search("(\w)+\W*(\w)*", self.comment) # matches the first two words


    # likes    = models.IntegerField(default=0)

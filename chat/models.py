# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    author = models.ForeignKey(User)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'message'
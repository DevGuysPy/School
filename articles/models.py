from django.db import models
from django.conf import settings

from School.models import Teacher

class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'articles'

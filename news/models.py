import datetime

from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    published = models.DateTimeField(default=datetime.datetime.now())
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f"{self.title} published at {self.published}"

    objects = models.Manager()

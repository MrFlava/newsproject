import datetime

from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=120)
    link = models.URLField(max_length=250, default='https://www.google.com/')
    published = models.DateTimeField(default=datetime.datetime.now())
    upvotes_amount = models.IntegerField(default=0)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f"{self.title} published at {self.published}"

    objects = models.Manager()


class Comment(models.Model):
    content = models.TextField()
    published = models.DateTimeField(default=datetime.datetime.now())
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.content} published at {self.published}"

    objects = models.Manager()

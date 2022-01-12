from django.db import models

from helpers.models import TimestampModel

from accounts.models import User
from post.models import Post


class Topic(TimestampModel):
    title = models.CharField(max_length=255)
    Description = models.TextField()
    ulr_name = models.CharField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    posts = models.ManyToManyField(Post, related_name="topic_posts")

from django.db import models

from helpers.models import TimestampModel

from accounts.models import User
from comment.models import Comment


class Post(TimestampModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.ManyToManyField(Comment, related_name="post_comments")

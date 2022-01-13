from django.db import models

from helpers.models import TimestampModel

from accounts.models import User
from post.models import Post


class Comment(TimestampModel):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )

from django.db import models

from helpers.models import TimestampModel

from accounts.models import User
from topic.models import Topic


class Post(TimestampModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(
        Topic, on_delete=models.CASCADE, related_name="posts"
    )

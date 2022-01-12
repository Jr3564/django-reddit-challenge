from django.db import models

from helpers.models import TimestampModel

from accounts.models import User


class Comment(TimestampModel):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

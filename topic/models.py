from django.db import models

from helpers.models import TimestampModel

from accounts.models import User


class Topic(TimestampModel):
    title = models.CharField(max_length=255)
    Description = models.TextField()
    url_name = models.SlugField(db_index=True, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

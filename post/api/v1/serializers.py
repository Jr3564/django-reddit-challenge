###
# Libraries
##
from rest_framework import serializers

###
# Models
##
from post.models import Post
from helpers.serializers import TimestampSerializer


class PostSerializer(TimestampSerializer):
    author = serializers.PrimaryKeyRelatedField(
        source="author.username", read_only=True
    )
    comments = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "content",
            "author",
            "comments",
            "date",
            "updated",
        )

    def create(self, validate_data):
        user = self.context.get("request", {"user", None}).user
        return Post.objects.create(**validate_data, author=user)

###
# Libraries
##
from rest_framework import serializers
from rest_framework.exceptions import NotFound

###
# Models
##
from comment.models import Comment
from post.models import Post
from helpers.serializers import TimestampSerializer


class CommentSerializer(TimestampSerializer):
    author = serializers.PrimaryKeyRelatedField(
        source="author.username", read_only=True
    )

    class Meta:
        model = Comment
        fields = (
            "id",
            "content",
            "author",
            "date",
            "updated",
        )

    def create(self, validate_data):
        try:
            post_instance = Post.objects.get(pk=self.context.get("post_pk"))

        except Post.DoesNotExist as err:
            raise NotFound(err)

        user = self.context.get("request").user

        return Comment.objects.create(
            **validate_data, author=user, post=post_instance
        )

    @classmethod
    def get_serialized_comments(cls, comment_ids: "list[int]"):
        comment_models_instances = Comment.objects.in_bulk(
            comment_ids
        ).values()
        return cls(comment_models_instances, many=True).data

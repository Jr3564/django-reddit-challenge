###
# Libraries
##
from rest_framework import serializers
from rest_framework.exceptions import NotFound

###
# Models
##
from post.models import Post
from topic.models import Topic
from comment.models import Comment

###
# Serializers
##
from comment.api.v1.serializers import CommentSerializer


from helpers.serializers import TimestampSerializer


class NestedTopicComments(CommentSerializer):
    class Meta:
        model = Comment
        fields = (
            "id",
            "content",
            "author",
        )


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
        try:
            topic_instance = Topic.objects.get(
                url_name=self.context.get("topic_url_name")
            )

        except Topic.DoesNotExist as err:
            raise NotFound(err)

        user = self.context.get("request").user

        return Post.objects.create(
            **validate_data, author=user, topic=topic_instance
        )

    def to_representation(self, topic_models_instance):
        response = super().to_representation(topic_models_instance)
        comments_ids = response.get("comments", [])

        if comments_ids:
            response["comments"] = NestedTopicComments.get_serialized_comments(
                comments_ids
            )

        return response

    @classmethod
    def get_serialized_posts(cls, post_ids: "list[int]"):
        post_models_instances = Post.objects.in_bulk(post_ids).values()
        return cls(post_models_instances, many=True).data

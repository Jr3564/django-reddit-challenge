###
# Libraries
##
from rest_framework import serializers

###
# Models
##
from topic.models import Topic
from post.models import Post

###
# Serializers
##
from post.api.v1.serializers import PostSerializer

from helpers.serializers import TimestampSerializer


class NestedTopicPosts(PostSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "content",
            "author",
        )


class TopicSerializer(TimestampSerializer):
    author = serializers.PrimaryKeyRelatedField(
        source="author.username", read_only=True
    )
    posts = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = Topic
        fields = (
            "id",
            "title",
            "Description",
            "url_name",
            "author",
            "posts",
            "date",
            "updated",
        )

    def create(self, validate_data):
        user = self.context.get("request", {"user", None}).user
        return Topic.objects.create(**validate_data, author=user)

    def to_representation(self, topic_models_instance):
        response = super().to_representation(topic_models_instance)
        posts_ids = response.get("posts", [])

        if posts_ids:
            response["posts"] = NestedTopicPosts.get_serialized_posts(
                posts_ids
            )

        return response

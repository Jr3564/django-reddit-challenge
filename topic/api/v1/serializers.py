###
# Libraries
##
from rest_framework import serializers

###
# Models
##
from topic.models import Topic
from helpers.serializers import TimestampSerializer

# TODO: Não permitir salvar url_name em branco


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
            "ulr_name",
            "author",
            "posts",
            "date",
            "updated",
        )

    def create(self, validate_data):
        user = self.context.get("request", {"user", None}).user
        return Topic.objects.create(**validate_data, author=user)

###
# Libraries
##
from rest_framework import serializers

###
# Models
##
from comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        source="author.username", read_only=True
    )
    date = serializers.DateTimeField(source="created_at", read_only=True)
    updated = serializers.DateTimeField(source="updated_at", read_only=True)

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
        user = self.context.get("request", {"user", None}).user
        return Comment.objects.create(**validate_data, author=user)

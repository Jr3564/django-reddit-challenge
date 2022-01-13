###
# Libraries
###
from rest_framework import permissions, viewsets

###
# Serializers
###
from comment.api.v1.serializers import CommentSerializer

###
# Models
###
from comment.models import Comment


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self, *args, **kwargs):
        post_pk = self.kwargs.get("nested_2_pk")
        return self.queryset.filter(post=post_pk)

    def get_serializer_context(self):
        return {
            **super().get_serializer_context(),
            "post_pk": self.kwargs.get("nested_2_pk"),
        }

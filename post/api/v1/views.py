###
# Libraries
###
from rest_framework import permissions, viewsets

###
# Serializers
###
from post.api.v1.serializers import PostSerializer

###
# Models
###
from post.models import Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self, *args, **kwargs):
        topic_url_name = self.kwargs.get("nested_1_url_name")
        return self.queryset.filter(topic__url_name=topic_url_name)

    def get_serializer_context(self):
        return {
            **super().get_serializer_context(),
            "topic_url_name": self.kwargs.get("nested_1_url_name"),
        }

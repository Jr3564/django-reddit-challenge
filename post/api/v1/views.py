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

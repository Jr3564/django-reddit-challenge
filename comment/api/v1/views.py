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

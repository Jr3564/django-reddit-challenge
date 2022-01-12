###
# Libraries
###
from rest_framework import permissions, viewsets

###
# Serializers
###
from topic.api.v1.serializers import TopicSerializer

###
# Models
###
from topic.models import Topic


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = (permissions.IsAuthenticated,)

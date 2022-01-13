"""
API V1: Topic Urls
"""
###
# Libraries
###
from django.conf.urls import url, include
from rest_framework_nested import routers

###
# Views
###
from .views import TopicViewSet
from post.api.v1.views import PostViewSet
from comment.api.v1.views import CommentViewSet

###
# Routers
###
""" Main router """
router = routers.SimpleRouter()

router.register("topics", TopicViewSet)

topics_router = routers.NestedSimpleRouter(router, r"topics")
topics_router.register(r"posts", PostViewSet)

posts_router = routers.NestedSimpleRouter(topics_router, r"posts")
posts_router.register(r"comments", CommentViewSet)

###
# URLs
###
urlpatterns = [
    url(r"^", include(posts_router.urls)),
    url(r"^", include(topics_router.urls)),
    url(r"^", include(router.urls)),
]

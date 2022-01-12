"""
API V1: Comment Urls
"""
###
# Libraries
###
from django.conf.urls import url, include
from rest_framework_nested import routers

###
# Views
###
from .views import CommentViewSet

###
# Routers
###
""" Main router """
router = routers.SimpleRouter()

router.register("comments", CommentViewSet)

###
# URLs
###
urlpatterns = [url(r"^", include(router.urls))]

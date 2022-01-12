"""
API V1: Post Urls
"""
###
# Libraries
###
from django.conf.urls import url, include
from rest_framework_nested import routers

###
# Views
###
from .views import PostViewSet

###
# Routers
###
""" Main router """
router = routers.SimpleRouter()

router.register("posts", PostViewSet)

###
# URLs
###
urlpatterns = [url(r"^", include(router.urls))]

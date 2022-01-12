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

###
# Routers
###
""" Main router """
router = routers.SimpleRouter()

router.register("topics", TopicViewSet)

###
# URLs
###
urlpatterns = [url(r"^", include(router.urls))]

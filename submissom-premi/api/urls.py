# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, DiscussionViewSet, CommentViewSet, HashtagViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'discussions', DiscussionViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'hashtags', HashtagViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

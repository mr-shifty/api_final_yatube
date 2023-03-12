from rest_framework import routers

from django.urls import include, path
from django.views.generic import TemplateView

from api.v1.views import (CommentViewSet, FollowViewSet, GroupViewSet,
                          PostViewSet, UserViewSet)


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'users', UserViewSet)
router.register(r'follow', FollowViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]

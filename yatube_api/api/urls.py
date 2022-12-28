from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from .views import (CommentViewSet, FollowViewSet, GroupViewSet, PostDetail,
                    PostList)

router_v1 = routers.DefaultRouter()
router_v1.register('groups', GroupViewSet, basename='group'),
router_v1.register(r'follow', FollowViewSet, basename='follow')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments',
)

urlpatterns = [
    path('v1/posts/', PostList.as_view()),
    path('v1/posts/<int:pk>/', PostDetail.as_view()),
    path('v1/', include(router_v1.urls)),
    path('v1/jwt/', include('djoser.urls')),
    path('v1/jwt/', include('djoser.urls.jwt')),
    path(
        'v1/jwt/create/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'v1/jwt/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path(
        'v1/jwt/verify/',
        TokenVerifyView.as_view(),
        name='token_verify'
    ),
]

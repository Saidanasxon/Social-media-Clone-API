from django.urls import path, include
from . import views
from rest_framework import routers


app_name = 'my_app'

router = routers.DefaultRouter()
router.register('users', views.UserViewSet),
router.register('posts', views.PostViewSet),
router.register('comments', views.CommentViewSet),

urlpatterns = [
    path('my_app/', include(router.urls)),
]
from .serializers import *
from .models import *
from .permissions import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication, BaseAuthentication, SessionAuthentication

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [CustomPermission]


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [CustomPermission]

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [CustomPermission]


from rest_framework import serializers
from .models import * 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("last_login", 'is_superuser', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined', 'groups', 'user_permissions')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

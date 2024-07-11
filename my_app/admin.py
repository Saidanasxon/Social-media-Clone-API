from django.contrib import admin
from .models import UserModel, Post, Comment

class UserPostInline(admin.TabularInline):
    model = Post
    extra = 0


class UserCommentInline(admin.TabularInline):
    model = Comment
    extra = 0

@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    inlines = [UserPostInline, UserCommentInline]
    

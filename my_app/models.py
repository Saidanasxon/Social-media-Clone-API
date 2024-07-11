from django.db import models
from django.contrib.auth.models import User

class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.user.username
    
    
class Post(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='blogs')
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    like = models.BooleanField(default=False)

    def __str__(self):
        return self.title
        
class Comment(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user} commented on {self.post}'

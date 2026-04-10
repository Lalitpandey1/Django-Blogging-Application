from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='liked_blogs',blank=True,default=0)
    title = models.CharField(max_length=200,default='Untitled')     # must give default 
    content = models.TextField()
    photo = models.ImageField(upload_to='static/photos/',null=True,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f' {self.user.username} - {self.title[:25]}'


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE, related_name='comments')
    text = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.text[:25]}'

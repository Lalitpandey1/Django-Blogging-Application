from rest_framework import serializers
from blog.models import Blog

class BlogSerializer(serializers.ModelSerializer):
    # Hum 'author' ka sirf username dikhana chahte hain, poora object nahi
    author_name = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'photo', 'author_name', 'create_at']
from rest_framework import generics
from blog.models import Blog
from .serializers import BlogSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Ye view Blogs ki list dikhayega aur naye blogs create bhi karega
class BlogListCreateAPIView(generics.ListCreateAPIView):
    queryset = Blog.objects.all().order_by('-create_at')
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Dekh sab sakte hain, post sirf logged-in user

    def perform_create(self, serializer):
        # Save karte waqt current user ko author set kar raha hai
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = Blog.objects.all().order_by('-create_at')
        author = self.request.query_params.get('author')
        if author:
            queryset = queryset.filter(user__username=author)
        return queryset

class BlogDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
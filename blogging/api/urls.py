from django.urls import path
from .views import BlogDetailAPIView, BlogListCreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Blogs ke liye endpoint
    path('blogs/', BlogListCreateAPIView.as_view(), name='api-blog-list'),
    path('blogs/<int:pk>/', BlogDetailAPIView.as_view(), name='api-blog-detail'),
    # JWT Authentication ke endpoints (Login aur Refresh)
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
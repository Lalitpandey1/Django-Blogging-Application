
from django.urls import path ,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('new_blog/',views.new_blog , name='new_blog'),
    path('<int:blog_id>/edit_blog/', views.edit_blog, name='edit_blog'),
    path('<int:blog_id>/delete_blog/', views.delete_blog, name='delete_blog'),
    path('register/', views.register, name='register'),
    path('logged_out/', views.logged_out, name='logged_out'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('<int:blog_id>/like/', views.liked_blog, name='blog_like_toggle'),
    path('<int:blog_id>/comments/', views.add_comment, name='add_comment')
]
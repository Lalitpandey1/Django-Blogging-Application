from django.contrib import messages
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render
from  .forms import NewBlogForm, UserRegistration,CommentForm
from .models import Blog,Comments
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    blogs = Blog.objects.prefetch_related('likes', 'comments').all().order_by('-create_at')
    paginator = Paginator(blogs, 3)  # Show 3 blogs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'index.html',{'page_obj': page_obj})

@login_required
def new_blog(request):
    new_blog = NewBlogForm()
    if request.method == 'POST':
        new_blog = NewBlogForm(request.POST, request.FILES)
        if new_blog.is_valid():
            blog = new_blog.save(commit=False)
            blog.user = request.user
            blog.save()
            messages.success(request, 'Blog created successfully!')
        return redirect('home')
    return render(request,'createBlog.html',{'form':new_blog})

@login_required
def edit_blog(request, blog_id):
    
    new_blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        form = NewBlogForm(request.POST, request.FILES, instance=new_blog)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.user = request.user
            new_blog.save()
            messages.success(request, 'Blog updated successfully!')
            return redirect('home')
    else:
        form = NewBlogForm(instance=new_blog)
    return render(request, 'createBlog.html', {'form': form})

@login_required
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        blog.delete()
        messages.success(request, 'Blog deleted successfully!')
        return redirect('home')
    return render(request, 'deleteBlog.html', {'blog': blog})

def register(request):
    form = UserRegistration()
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    return render(request,'registration/register.html',{'form':form})


def logged_out(request):
    return render(request,'registration/logout.html')

@login_required
def profile(request,username):
    profile_user = get_object_or_404(User, username = username)  # fetches the user
    user_blogs = Blog.objects.filter(user = profile_user).order_by('-create_at')
    return render(request,'profile.html',{'username':username , 'all_blogs' : user_blogs})
    
@login_required
def liked_blog(request, blog_id):
    blog = get_object_or_404(Blog , pk=blog_id)
    if request.user in blog.likes.all():
        blog.likes.remove(request.user)
    else:
        blog.likes.add(request.user)
    return redirect(request.META.get('HTTP_REFERER', 'home'))

@login_required
def add_comment(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    if request.method == 'POST':
        # print(f"DEBUG: Data in POST: {request.POST}")
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            print(comment)
    return redirect(request.META.get('HTTP_REFERER', 'home'))
   
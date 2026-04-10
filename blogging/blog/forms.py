from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Blog,Comments

class NewBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content','photo']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Write a comment...'
            })}

class UserRegistration(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username','email','password1','password2')


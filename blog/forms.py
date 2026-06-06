from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        
        fields = ['title', 'category', 'excerpt', 'content', 'featured_image', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a catchy title...'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'A short summary for the homepage...'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder': 'Write your full article here...'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
   
class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        self.fields['password1'].widget.attrs.update({'placeholder': 'Minimum 8 characters'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm your password'})
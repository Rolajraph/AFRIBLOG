from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from .models import Category, Post 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import PermissionDenied
from django.utils.text import slugify
from django.contrib.auth.models import User
from .forms import PostForm,UserRegistrationForm
from django.core.paginator import Paginator
from .models import Post
from .models import Comment
from django.contrib.auth.decorators import user_passes_test

def category_list(request):
    categories = Category.objects.annotate(num_posts=Count('posts'))
    return render(request, 'category.html', {'categories': categories})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
  
    all_posts = category.posts.all().order_by('-created_on')
    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'category_detail.html', {
        'category': category, 
        'page_obj': page_obj 
    })

def write_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user 
            post.save()
            return redirect('home')
    else:
        form = PostForm() 
    
    return render(request, 'write.html', {'form': form})

def home_view(request):
    post_list = Post.objects.filter(status=1).order_by('-created_on')
    paginator = Paginator(post_list, 6) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,  
    }
    return render(request, 'index.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post_detail.html', {'post': post})

def index(request):
    post_list = Post.objects.filter(status=1).order_by('-created_on')
    paginator = Paginator(post_list, 6) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj': page_obj})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm() 
    return render(request, 'registration/register.html', {'form': form})
@login_required
def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    if request.user != post.author:
        raise PermissionDenied("You do not have permission to edit this post.")
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
        
    return render(request, 'write.html', {'form': form, 'edit': True})

@login_required
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
   
    if request.user != post.author:
        raise PermissionDenied("You do not have permission to delete this post.")
    
    if request.method == 'POST':
        post.delete()
        return redirect('home')
        
    return render(request, 'delete_confirm.html', {'post': post})
@login_required
def add_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(
                post=post,
                author=request.user,
                content=content
            )
    return redirect('post_detail', slug=slug)
@user_passes_test(lambda u: u.is_staff)
def delete_comment(request, comment_id): 
    comment = get_object_or_404(Comment, id=comment_id)
    post_slug = comment.post.slug
    comment.delete()
    return redirect('post_detail', slug=post_slug)
@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    
    # Permission check: Only the author can edit
    if request.user != comment.author:
        raise PermissionDenied("You can only edit your own comments.")
        
    if request.method == 'POST':
        # logic to save the updated content
        comment.content = request.POST.get('content')
        comment.save()
        return redirect('post_detail', slug=comment.post.slug)
    
    return render(request, 'edit_comment.html', {'comment': comment})
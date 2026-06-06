"""
URL configuration for afriblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from blog import views 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Add these missing paths
    path('', views.index, name='home'), 
    path('categories/', views.category_list, name='categories'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('write/', views.write_post, name='write'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('edit/<slug:slug>/', views.edit_post, name='edit_post'),
    path('delete/<slug:slug>/', views.delete_post, name='delete_post'),
    path('register/', views.register, name='register'), 
    path('post/<slug:slug>/add_comment/', views.add_comment, name='add_comment'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('comment/add/<slug:slug>/', views.add_comment, name='add_comment'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'), 
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('comment/edit/<int:comment_id>/', views.edit_comment, name='edit_comment'),
   
]
    
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
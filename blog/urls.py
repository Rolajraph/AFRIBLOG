from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'), 
    path('categories/', views.category_list, name='categories'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('write/', views.write_post, name='write'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('edit/<slug:slug>/', views.edit_post, name='edit_post'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('delete/<slug:slug>/', views.delete_post, name='delete_post'),
    path('post/<slug:slug>/add_comment/', views.add_comment, name='add_comment'),
    path('register/', views.register, name='register'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
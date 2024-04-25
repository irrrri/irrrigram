from django.contrib import admin
from django.urls import path
from app_bmstu import views
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('/posts/', permanent=True)),
    path('admin/', admin.site.urls),
    path('posts/', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('sendText', views.sendText, name='sendText'),
]

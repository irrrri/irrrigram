from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import date, datetime
from django.http import Http404
from .models import Post, Comment
import random

postsFake = [
    {'id': 1, 'nickname': 'Irina', 'text': 'Сегодня замечательный день!', 'likes_count': 25, 'comments_count': 10, 'image': '/images/photo1.jpeg', 'created_at': datetime(2024, 3, 1, 12, 30)},
    {'id': 2, 'nickname': 'Bob', 'text': 'Путешествие на горы было невероятным!', 'likes_count': 18, 'comments_count': 54, 'image': '/images/photo2.jpeg', 'created_at': datetime(2024, 2, 28, 18, 45)},
    {'id': 3, 'nickname': 'Charlie', 'text': 'Ирина в 200 метрах от вас! Хотите познакомится?', 'likes_count': 12, 'comments_count': 5, 'image': '/images/photo3.jpeg', 'created_at': datetime(2024, 2, 27, 8, 15)},
    {'id': 4, 'nickname': 'David', 'text': 'Посмотрите какая котейка!', 'likes_count': 30, 'comments_count': 104, 'image': '/images/photo4.jpeg', 'created_at': datetime(2024, 2, 26, 14, 0)},
    {'id': 5, 'nickname': 'Eva', 'text': 'Кто-нибудь отмечал 14 февраля?', 'likes_count': 8, 'comments_count': 34, 'image': '/images/photo5.jpeg', 'created_at': datetime(2024, 2, 25, 20, 30)},
    {'id': 5, 'nickname': 'Eva', 'text': 'Кто-нибудь отмечал 14 февраля?', 'likes_count': 8, 'comments_count': 34, 'image': '/images/photo5.jpeg', 'created_at': datetime(2024, 2, 25, 20, 30)},
]

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post)
    return render(request, 'post_detail.html', {'post': post, 'post_id': post_id, 'comments': comments},)

def sendText(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        num_records = request.POST.get('num_records')
        if num_records:
            limited_posts = posts[:int(num_records)]
        else:
            limited_posts = posts
        return render(request, 'posts.html', {'posts': limited_posts})

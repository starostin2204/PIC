# articles/views.py

from .models import Article
from django.shortcuts import render

def archive(request):
    # Получаем все объекты Article из базы данных
    all_articles = Article.objects.all()
    
    # Рендерим шаблон, передавая список статей в контексте как "posts"
    return render(request, 'archive.html', {"posts": all_articles})
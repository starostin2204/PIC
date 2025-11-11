from django.contrib import admin
from .models import Article

# Регистрация модели Article для доступа через Admin-панель
admin.site.register(Article)
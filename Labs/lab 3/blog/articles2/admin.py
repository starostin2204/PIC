# -*- coding: utf-8 -*-
# Файл конфигурации административной панели Django

# Импорт модуля admin из Django
# admin предоставляет функции для регистрации моделей в админ-панели
# Позволяет управлять данными через веб-интерфейс
from django.contrib import admin

# Импорт модели Article из текущего приложения
# .models означает файл models.py в той же директории
# Пример: from .models import Article, Comment
from .models import Article

# Класс конфигурации отображения модели в админке
# ModelAdmin - базовый класс для настройки админ-интерфейса
# Определяет, как модель отображается в списке и форме редактирования
# Пример: class BookAdmin(admin.ModelAdmin)
class ArticleAdmin(admin.ModelAdmin):
    # list_display - кортеж полей для отображения в списке объектов
    # Определяет колонки таблицы в админ-панели
    # Можно указывать поля модели и методы
    # Пример: list_display = ('id', 'name', 'created_date')
    list_display = ('title', 'author', 'get_excerpt', 'created_date')

# Регистрация модели Article в административной панели
# admin.site.register() добавляет модель в админку
# Первый параметр - класс модели
# Второй параметр - класс конфигурации (необязательный)
# Пример: admin.site.register(Book, BookAdmin)
admin.site.register(Article, ArticleAdmin)

# blog/urls.py

from django.contrib import admin
from django.urls import path
from articles import views as articles_views # <-- Импортируем views из articles

urlpatterns = [
    path('admin/', admin.site.urls),
    # Главная страница теперь отображает архив статей
    path('', articles_views.archive, name='archive'), # <-- ИЗМЕНЕНО
]
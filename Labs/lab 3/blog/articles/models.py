from django.db import models
from django.contrib.auth.models import User # Импорт стандартной модели пользователя

class Article(models.Model):
    # Заголовок (максимальная длина 200 символов)
    title = models.CharField(max_length=200)
    # Текст статьи (неограниченная длина)
    text = models.TextField()
    # Автор (связь с моделью User, CASCADE - удаление статьи при удалении автора)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Дата создания (auto_now_add=True - устанавливается только при создании)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Метод для удобного отображения в Admin-панели
        return self.title

    def get_excerpt(self):
        # Метод для получения краткого отрывка (для вывода в шаблоне)
        return self.text[:200] + '...' if len(self.text) > 200 else self.text
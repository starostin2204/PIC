from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # Возвращаем простой текстовый ответ. content_type="text/plain" указывает на чистый текст. 
    # return HttpResponse(u'Привет, Мир!', content_type="text/plain")
    # return HttpResponse(u'Привет, Мир!')
    # Теперь рендерим шаблон index.html
    # return render(request, 'index.html')
    return render(request, 'static_handler.html')    
from django.shortcuts import render, redirect
from .models import Articles   # из репозитория приложения ньюс (. моделс) импортируем класс с БД
from .forms import ArticlesForms

def news_home(request):
    news = Articles.objects.order_by('date')  #сортируем по дате # создаем объект, обращаемся ко всем объектам класса Articles, вызываем их. Теперь все эти объекты в переменной news
    return render(request, 'news/news_home.html', {'news': news})

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = ArticlesForms()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)

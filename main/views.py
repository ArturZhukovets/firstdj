from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', 'World!'],
        'obj': {
            'car': 'BMW',
            'age': 24,
            'hobby': 'Kickboxing'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')
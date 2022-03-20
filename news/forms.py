from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea   # на основе этого класса создается форма


class ArticlesForms(ModelForm):       # Называть как угодно, но обычно называют названием класса таблицы и добавляем слово FORM.
    class Meta:                       # Для того чтобы указать характеристики
        model = Articles    # работаем с моделью(БД) артиклс
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            })
        }

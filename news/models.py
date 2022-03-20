from django.db import models

''' Описывыем таблицу внутри базы данных. Создание происходит в тот момент когда выполняю миграции.
    Миграции - синхронизация проекта с базой данных '''
class Articles(models.Model):   #Наследуем все от класса Model
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)     # CharField - не более 250 символов
    full_text = models.TextField('Статья')                      # TextField - тип данных для текстовой информации где много символов
    date = models.DateTimeField('Дата публикации')

    def __str__(self):     # Этим методом мы указываем какая именно информация будет выводится
        return f'Новость: {self.title}'  # А выводится title нашей таблицы

    # Для того чтобы переименовать таблицу в панели админа !!! Обязательное название класса - Meta:
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = "Новости" #plural = множественном числе.
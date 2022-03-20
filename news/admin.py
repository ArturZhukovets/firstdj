from django.contrib import admin
from.models import Articles     # Импортируем созданный класс Articles
'''Здесь регистрируем созданную таблицу'''

admin.site.register(Articles)  # Регистрируем созданную таблицу при помощи метода admin.site.register

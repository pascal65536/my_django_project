from django.db import models
from datetime import date

class Message(models.Model):
    userName = models.CharField(max_length=30, verbose_name='Имя пользователя ')
    date = models.DateField(default=date.today)
    text = models.TextField(verbose_name='Текст ')

    def __str__(self):
        return self.title


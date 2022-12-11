from django.db import models


class Advantage(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.name


class Address(models.Model):
    name = models.CharField(max_length=255, verbose_name='Адрес')

    def __str__(self):
        return self.name


class Question(models.Model):
    name = models.CharField(max_length=255, verbose_name='Вопрос')
    description = models.CharField(max_length=255, verbose_name='Описание вопроса')

    def __str__(self):
        return f'{self.name}' \
               f'{self.description}'

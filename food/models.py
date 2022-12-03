from django.db import models


class FoodCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.name


class Food(models.Model):
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE,
                                 related_name='food')
    name = models.CharField(max_length=255, verbose_name='Название')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return f'{self.name} - {self.price}'


from django.db import models


class RulesCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.name


class Rules(models.Model):
    category = models.ForeignKey(RulesCategory, on_delete=models.CASCADE,
                                 related_name='food')
    name = models.CharField(max_length=255, verbose_name='Название')


    def __str__(self):
        return self.name


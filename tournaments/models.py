from django.db import models
from django.conf import settings


# Create your models here.
class Tournament(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    team_qty = models.IntegerField(verbose_name="Количество команд")
    prize = models.IntegerField(verbose_name="Призовые")


class Team(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='teams')
    players = models.ManyToManyField('Player', related_name='teams')
    is_full = models.BooleanField(default=False)


class Player(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='player')
    name = models.CharField(max_length=255, verbose_name="Никнейм")

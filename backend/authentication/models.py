from django.db import models

from django.contrib.auth.models import User


class Cards(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    description = models.CharField(max_length=160)
    collection = models.IntegerField(default=1)
    title = models.CharField(max_length=20)
    link = models.CharField(max_length=40, default='')


class Tags(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    card = models.ForeignKey(Cards, models.CASCADE)
    title = models.CharField(max_length=20)

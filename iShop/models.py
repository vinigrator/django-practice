from __future__ import unicode_literals

import datetime
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=300)
    rate = models.FloatField(default=10)

class Goods(models.Model):
    name = models.CharField(max_length=255)
    count = models.IntegerField()
    price = models.FloatField()
    description = models.TextField()
    shops = models.ManyToManyField(Shop)

class Seller(models.Model):
    name = models.CharField(max_length=255)
    characteristic = models.TextField()
    salary = models.FloatField()
    date_start = models.DateTimeField(default=datetime.datetime.now())
    shop = models.OneToOneField(Shop, null=True)
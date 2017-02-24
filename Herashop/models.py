from django.db import models

# Create your models here.

from django.db import models
from django.core import validators


class ImageFile(models.Model):
    file = models.FileField()

    def __str__(self):
        return self.file.name


class StoreType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    icon = models.CharField(max_length=40, default="")

    def __str__(self):
        return self.name


class Store(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)
    type = models.ForeignKey(StoreType, null=True)

    def __str__(self):
        return self.name


class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    image = models.ForeignKey(ImageFile, null=True)
    description = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    discount = models.FloatField(default=0)
    discountPrice = models.FloatField(default=0)
    stores = models.ManyToManyField(StoreType)
    excluded_stores = models.ManyToManyField(Store, blank=True)

    def __str__(self):
        return self.name

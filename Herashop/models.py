from django.db import models

# Create your models here.

from django.db import models


class Store(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)
    icon = models.CharField(max_length=40)

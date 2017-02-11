from django.contrib import admin

# Register your models here.

from django.contrib import admin
from Herashop.models import Store, Stock, StoreType

admin.site.register(Store)
admin.site.register(Stock)
admin.site.register(StoreType)

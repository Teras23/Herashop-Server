from django.shortcuts import render

# Create your views here.

import os
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.templatetags.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from django.db import connections
from django.core import serializers
from django.conf import settings
from Herashop.models import Store, Stock


def test(request):
    if request.method == 'GET':
        return HttpResponse("testing.eucolus.com")


def stores(request):
    return HttpResponse(serializers.serialize('json', Store.objects.all()))


def stock(request, storeid=0, excludeid=0):
    try:
        s = Stock.objects.filter(stores=storeid).exclude(excluded_stores=excludeid)
        return HttpResponse(serializers.serialize('json', s))
    except Stock.DoesNotExist:
        raise HttpResponse("Stock not found")


def icon(request, path=""):
    try:
        with open(os.path.join(settings.STATICFILES_DIRS[0], 'rademar.png'), 'rb') as f:
            return HttpResponse(f.read(), content_type='image/png')
    except IOError:
        return HttpResponse('Could not find file ' + staticfiles_storage.url('rademar.png'))

from django.shortcuts import render

# Create your views here.

import os
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.templatetags.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from django.db import connections
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
from django.conf import settings
from Herashop.models import Store, Stock, StoreType, ImageFile


def test(request):
    if request.method == 'GET':
        return HttpResponse("testing.eucolus.com")


def storetype(request):
    qs = StoreType.objects.all()
    qs_json = serializers.serialize('json', qs)
    return HttpResponse(qs_json, content_type='application/json')


def stores(request):
    qs = Store.objects.all()
    qs = Store.objects.prefetch_related().all()
    qs_json = serializers.serialize('json', qs)
    print(qs_json)
    return HttpResponse(qs_json, content_type='application/json')


def stock(request, storeid=0, excludeid=0):
    qs = Stock.objects.filter(stores=storeid).exclude(excluded_stores=excludeid)
    qs_json = serializers.serialize('json', qs)
    return HttpResponse(qs_json, content_type='application/json')


def icon(request, path=""):
    try:
        with open(os.path.join(settings.MEDIA_ROOT, path), 'rb') as file:
            return HttpResponse(file.read(), content_type='image/png')
    except IOError:
        with open(os.path.join(settings.MEDIA_ROOT, 'empty.png'), 'rb') as file:
            return HttpResponse(file.read(), content_type='image/png')


def imageId(request, id=1):
    try:
        qs = ImageFile.objects.get(id=id)
        with open(os.path.join(settings.MEDIA_ROOT, str(qs.file)), 'rb') as file:
            return HttpResponse(file.read(), content_type='image/jpg')
    except (IOError, ObjectDoesNotExist) as e:
        return HttpResponse("Error " + str(e))


def image(request, path=""):
    try:
        with open(os.path.join(settings.MEDIA_ROOT, path), 'rb') as file:
            return HttpResponse(file.read(), content_type='image/png')
    except IOError:
        with open(os.path.join(settings.MEDIA_ROOT, 'empty.png'), 'rb') as file:
            return HttpResponse(file.read(), content_type='image/png')

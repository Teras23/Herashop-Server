from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.db import connections
from django.core import serializers
from Herashop.models import Store


def test(request):
    if request.method == 'GET':
        return HttpResponse("test")


def stores(request):
    return HttpResponse(serializers.serialize('json', Store.objects.all()))

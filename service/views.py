#-*- coding:utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def filter_makeup(request):
    content = {
            }
    return render_to_response('makeup.html', RequestContext(request, content))


def filter_flower(request):
    content = {
            }
    return render_to_response('flower.html', RequestContext(request, content))

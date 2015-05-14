#-*- coding:utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

from service.models import MC

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def filter_makeup(request):
    content = {
            }
    return render_to_response('makeup.html', RequestContext(request, content))


def filter_mc(request):
    # print request.GET

    kwargs = dict()

    # gender filter
    gender = request.GET.get('gender', '0')
    if gender != '0':
        kwargs['gender'] = gender

    content = {
        'data_set': MC.objects.filter(**kwargs),
            }
    return render_to_response('mc.html', RequestContext(request, content))


def filter_flower(request):
    content = {
            }
    return render_to_response('flower.html', RequestContext(request, content))

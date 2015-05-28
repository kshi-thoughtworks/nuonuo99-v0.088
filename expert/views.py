#-*- coding:utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response

# REST framework
from rest_framework import generics
from rest_framework import permissions

from expert.models import MC, MakeUp
from expert.serializers import McSerializer, MakeUpSerializer

from base.utils import price_filter
from base.choices import MC_PARAS


def mc_home(request):
    content = {
        'paras': MC_PARAS(),
        }
    return render_to_response('mc.html', RequestContext(request, content))


class McList(generics.ListCreateAPIView):
    queryset = MC.objects.all()
    serializer_class = McSerializer


class MakeUpList(generics.ListCreateAPIView):
    queryset = MakeUp.objects.all()
    serializer_class = MakeUpSerializer

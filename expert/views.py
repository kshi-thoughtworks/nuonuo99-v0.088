#-*- coding:utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
# REST framework
from rest_framework import generics
from rest_framework import permissions

from expert.models import MC, MakeUp
from expert.serializers import McSerializer, MakeUpSerializer

from base.utils import price_filter


def mc_list(request):
    content = {
        'paras': [
            {
                'name': 'wed_sty',
                'disp_name': u'专业',
                'values': [
                    ('cn', u'中式'),
                    ('west', u'西式'),
                    ]
            },
            {
                'name': 'gender',
                'disp_name': u'性别',
                'values': [
                    ('male', u'男'),
                    ('female', u'女')
                    ]
            }
            ]
        }
    return render_to_response('mc.html', RequestContext(request, content))


class McFilter(generics.ListCreateAPIView):
    queryset = MC.objects.all()
    serializer_class = McSerializer


class MakeUpList(generics.ListCreateAPIView):
    queryset = MakeUp.objects.all()
    serializer_class = MakeUpSerializer

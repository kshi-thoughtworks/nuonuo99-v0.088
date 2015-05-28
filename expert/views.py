#-*- coding:utf-8 -*-
# REST framework
from rest_framework import generics
from rest_framework import permissions

from expert.models import MC, MakeUp
from expert.serializers import McSerializer

from base.utils import price_filter


class McList(generics.ListCreateAPIView):
    queryset = MC.objects.all()
    serializer_class = McSerializer

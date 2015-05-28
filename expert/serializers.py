#-*- coding:utf-8 -*-
from rest_framework import serializers

from expert.models import MC, MakeUp


class McSerializer(serializers.ModelSerializer):
    class Meta:
        model = MC

class MakeUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = MakeUp

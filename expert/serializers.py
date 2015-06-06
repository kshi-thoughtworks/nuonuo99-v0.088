#-*- coding:utf-8 -*-
from rest_framework import serializers

from expert.models import mc, makeup, photographer, vedioguys


class mc_serializer(serializers.ModelSerializer):
    class Meta:
        model = mc


class makeup_serializer(serializers.ModelSerializer):
    class Meta:
        model = makeup


class photographer_serializer(serializers.ModelSerializer):
    class Meta:
        model = photographer


class vedioguys_serializer(serializers.ModelSerializer):
    class Meta:
        model = vedioguys

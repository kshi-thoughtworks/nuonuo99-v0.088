#-*- coding:utf-8 -*-
from rest_framework import serializers

from expert.models import mc, makeup, photographer, vedioguys


class McSerializer(serializers.ModelSerializer):
    class Meta:
        model = mc


class MakeUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = makeup


class PhotographerSerializer(serializers.ModelSerializer):
    class Meta:
        model = photographer


class VedioGuysSerializer(serializers.ModelSerializer):
    class Meta:
        model = vedioguys

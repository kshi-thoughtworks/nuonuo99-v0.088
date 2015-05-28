#-*- coding:utf-8 -*-
from rest_framework import serializers

from expert.models import MC, MakeUp, Photographer, VedioGuys


class McSerializer(serializers.ModelSerializer):
    class Meta:
        model = MC


class MakeUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = MakeUp


class PhotographerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photographer


class VedioGuysSerializer(serializers.ModelSerializer):
    class Meta:
        model = VedioGuys

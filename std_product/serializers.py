#-*- coding:utf-8 -*-
from rest_framework import serializers

from std_product.models import flower, av, stage


class WedFlowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = flower


class WedAvSerializer(serializers.ModelSerializer):
    class Meta:
        model = av


class StageEffectSerializer(serializers.ModelSerializer):
    class Meta:
        model = stage

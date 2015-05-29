#-*- coding:utf-8 -*-
from rest_framework import serializers

from std_product.models import WedFlower, WedAv, StageEffect


class WedFlowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = WedFlower


class WedAvSerializer(serializers.ModelSerializer):
    class Meta:
        model = WedAv


class StageEffectSerializer(serializers.ModelSerializer):
    class Meta:
        model = StageEffect

#-*- coding:utf-8 -*-
from rest_framework import serializers

from wedding.models import WedScheme, WedEssential


class WedEssentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = WedEssential


class WedSchemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WedScheme

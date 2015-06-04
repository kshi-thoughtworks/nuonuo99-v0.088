#-*- coding:utf-8 -*-
from rest_framework import serializers

from provider.models import ProviderInfo


class ProviderInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderInfo

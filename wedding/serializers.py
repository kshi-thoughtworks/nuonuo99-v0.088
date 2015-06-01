#-*- coding:utf-8 -*-
from rest_framework import serializers

from wedding.models import WedScheme


class WedSchemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WedScheme

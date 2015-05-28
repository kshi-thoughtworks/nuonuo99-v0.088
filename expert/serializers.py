#-*- coding:utf-8 -*-
from rest_framework import serializers

from expert.models import MC


class McSerializer(serializers.ModelSerializer):
    class Meta:
        model = MC

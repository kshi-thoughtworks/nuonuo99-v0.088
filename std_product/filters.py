#-*- coding:utf-8 -*-
import django_filters

import base.choices as choice_set
from std_product.models import WedFlower, WedAv, StageEffect


class WedFlowerFilter(django_filters.FilterSet):
    price = django_filters.CharFilter(action=choice_set.range_action('price'))

    class Meta:
        model = WedFlower
        fields = ['price', 'category', 'style']


class WedAvFilter(django_filters.FilterSet):
    price = django_filters.CharFilter(action=choice_set.range_action('price'))

    class Meta:
        model = WedAv
        fields = ['price', 'category', 'wed_env']


class StageEffectFilter(django_filters.FilterSet):
    price = django_filters.CharFilter(action=choice_set.range_action('price'))

    class Meta:
        model = StageEffect
        fields = ['price', 'category', 'sub_category']

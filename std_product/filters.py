#-*- coding:utf-8 -*-
import django_filters

import base.choices as choice_set
from std_product.models import flower, av, stage


class flower_filter(django_filters.FilterSet):
    price = django_filters.CharFilter(action=choice_set.range_action('price'))

    class Meta:
        model = flower
        fields = ['price', 'category', 'style']


class av_filter(django_filters.FilterSet):
    price = django_filters.CharFilter(action=choice_set.range_action('price'))

    class Meta:
        model = av
        fields = ['price', 'category', 'wed_env']


class stage_filter(django_filters.FilterSet):
    price = django_filters.CharFilter(action=choice_set.range_action('price'))

    class Meta:
        model = stage
        fields = ['price', 'category', 'sub_category']

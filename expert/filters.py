#-*- coding:utf-8 -*-
import django_filters

import base.choices as choice_set
from expert.models import mc, makeup, photographer, vedioguys

class mc_filter(django_filters.FilterSet):
    price = django_filters.CharFilter(action=choice_set.range_action('price'))
    age = django_filters.CharFilter(action=choice_set.range_action('t_birth'))
    height = django_filters.CharFilter(action=choice_set.range_action('height'))
    mc_tech = django_filters.CharFilter(lookup_type='isnull')

    class Meta:
        model = mc
        fields = ['price', 'wed_sty', 'is_man', 'age', 'height', 'loc_native', 'mc_tech']


class makeup_filter(django_filters.FilterSet):
    price = django_filters.CharFilter(action=choice_set.range_action('price'))

    class Meta:
        model = makeup
        fields = ['price', 'wed_sty', 'makeup_sty']


class photographer_filter(django_filters.FilterSet):
    price = django_filters.CharFilter(action=choice_set.range_action('price'))

    class Meta:
        model = photographer
        fields = ['price', 'is_full_frame', 'no_teamwork']


class vedioguys_filter(django_filters.FilterSet):
    price = django_filters.CharFilter(action=choice_set.range_action('price'))

    class Meta:
        model = vedioguys
        fields = ['price', 'use_camera']

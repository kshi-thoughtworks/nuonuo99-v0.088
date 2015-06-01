#-*- coding:utf-8 -*-
import django_filters

import base.choices as choice_set
from expert.models import MC, MakeUp, Photographer, VedioGuys

class McFilter(django_filters.FilterSet):
    price = django_filters.CharFilter(action=choice_set.range_action('price'))
    age = django_filters.CharFilter(action=choice_set.range_action('t_birth'))
    height = django_filters.CharFilter(action=choice_set.range_action('height'))
    mc_tech = django_filters.CharFilter(lookup_type='isnull')

    class Meta:
        model = MC
        fields = ['price', 'wed_sty', 'is_man', 'age', 'height', 'loc_native', 'mc_tech']


class MakeUpFilter(django_filters.FilterSet):
    price = django_filters.CharFilter(action=choice_set.range_action('price'))

    class Meta:
        model = MakeUp
        fields = ['price', 'wed_sty', 'makeup_sty']


class PhotographerFilter(django_filters.FilterSet):
    price = django_filters.CharFilter(action=choice_set.range_action('price'))

    class Meta:
        model = Photographer
        fields = ['price', 'is_full_frame', 'no_teamwork']


class VedioGuysFilter(django_filters.FilterSet):
    price = django_filters.CharFilter(action=choice_set.range_action('price'))

    class Meta:
        model = VedioGuys
        fields = ['price', 'use_camera']

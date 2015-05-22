#-*- coding:utf-8 -*-
from base.models import DiyFilter

def get_choice_set(key):
    return [(item.value, item.value_disp) for item in DiyFilter.objects.filter(name=key)]

def get_filter_sets(key):
    kwargs = dict()
    def add_item(item):
        if item.name in kwargs:
            kwargs[item.name]['values'].append((item.value, item.value_disp))
        else:
            kwargs[item.name] = {
                'disp_name': item.get_name_display(),
                'values': [(item.value, item.value_disp)],
                }
    for item in DiyFilter.objects.filter(scen=key).order_by('order'):
        add_item(item)
    return kwargs

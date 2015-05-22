#-*- coding:utf-8 -*-
from base.models import DiyFilter

def get_choice_set(key):
    return [(item.value, item.value_disp) for item in DiyFilter.objects.get(name=key)]

#-*- coding:utf-8 -*-
from django.forms import ModelForm

from wedding.models import WedEssential


class WedEssentialForm(ModelForm):
    class Meta:
        model = WedEssential
        fields = ['boy', 'girl', 't_wed', 'expect', 'btm_table_num', 'top_table_num']


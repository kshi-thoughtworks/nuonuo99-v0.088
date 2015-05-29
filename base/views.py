#-*- coding:utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response

import base.choices as choise_set


def home(request):
    content = {
        'flower': choise_set.C_FLOWER_CATE,
        'av': choise_set.C_AV_CATE,
        'stage': choise_set.C_STAGE_CATE,
        }
    return render_to_response('home.html', RequestContext(request, content))

#-*- coding:utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response

import base.choices as choice_set
import expert.models
import expert.filters
import expert.serializers


def expert_home(request, type='mc'):
    model = getattr(expert.models, type)
    filter = getattr(expert.filters, '%s_filter' % type)
    paras = getattr(choice_set, '%s_paras' % type)

    data = filter(request.GET, queryset=model.objects.all())

    content = {
        'paras': paras(),
        'cart_url': 'add_service_%s' % type,
        'data_set': data,
        'disp_name': model._meta.verbose_name
        }
    return render_to_response('expert.html', RequestContext(request, content))

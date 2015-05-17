#-*- coding:utf-8 -*-
import json
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

from shop.models import CartInfo

from django.contrib.contenttypes.models import ContentType
import expert.models
import std_product.models

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


# login required
def add(request):
    amount = int(request.GET.get('amount'))

    obj_id = 1
    obj_model = expert.models.MakeUp

    msg = 'success'
    res_code = 0
    
    if amount and obj_model and obj_id:
        obj = obj_model.objects.get(id=obj_id)
        try:
            product_type = ContentType.objects.get_for_model(obj_model)
            item = CartInfo.objects.get(buyer=request.user, object_id=obj_id, content_type__pk=product_type.id)
        except ObjectDoesNotExist:
            CartInfo(buyer=request.user, content_object=obj, amount=amount).save()
        else:
            item.amount += amount
            item.save()
    else:
        res_code = 1
        msg = 'param error'

    response_data = {
            'res_code': '0',  # success
            'message': msg,
            }

    return HttpResponse(json.dumps(response_data), content_type="application/json")

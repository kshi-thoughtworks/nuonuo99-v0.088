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

type_map = {
    'makeup': expert.models.MakeUp,
    }

def parse_product_key(product_key):
    """return product obj

    return None, if error occurs
    raise ObjectDoesNotExist, if there is no error but obj not exist
    """
    type_key, obj_id = product_key.split('_')

    if type_key not in type_map:
        return  # type error

    try:
        obj = type_map[type_key].objects.get(id=obj_id)
    except MultipleObjectsReturned:
        return  # error

    return obj


# login required
def add(request, product_key):
    raw_amount = request.GET.get('amount', '1')

    error_msg = ''

    try:
        amount = int(raw_amount)
    except ValueError:
        error_msg += 'param error. amount is necessary and number is required.'

    try:
        product_obj = parse_product_key(product_key)
    except ObjectDoesNotExist:
        error_msg += 'param error. product_key error'
    else:
        if product_obj is None:
            error_msg += 'param error. product_key error'

    if not error_msg:
        # add product_obj, amount, user to CartInfo
        try:
            product_type = ContentType.objects.get_for_model(product_obj)
            item = CartInfo.objects.get(buyer=request.user, object_id=product_obj.id, content_type__pk=product_type.id)
        except ObjectDoesNotExist:  # add new item to cart
            CartInfo(buyer=request.user, content_object=product_obj, amount=amount).save()
        else:
            item.amount += amount
            item.save()

    content = {
        'error_msg': error_msg,
        }

    return render_to_response('my_cart.html', RequestContext(request, content))

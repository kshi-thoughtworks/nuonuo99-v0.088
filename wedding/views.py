#-*- coding:utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from wedding.models import CartInfo, WedEssential, Order

from django.contrib.contenttypes.models import ContentType
from expert.models import MC, MakeUp
import std_product.models

from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages


def wed_program(user):
    try:
        wed_info = WedEssential.objects.get(user=user)
    except ObjectDoesNotExist:
        wed_info = None

    return {
        'wed_info': wed_info,
        'cart_data': CartInfo.objects.filter(buyer=user),
        'order_data': Order.objects.filter(buyer=user),
        }


def add_service(user, obj):
    # add obj, user to CartInfo if not exists in cart
    c_type= ContentType.objects.get_for_model(obj)
    try:
        item = CartInfo.objects.get(buyer=user, object_id=obj.id, content_type__pk=c_type.id)
    except ObjectDoesNotExist:  # add new item to cart
        CartInfo(buyer=user, content_object=obj, amount=1).save()


def add_service_mc(request, obj_id):
    try:
        obj = MC.objects.get(id=obj_id)
    except ObjectDoesNotExist:
        error_msg = '司仪(id=%s)不存在!' % obj_id
        return render_to_response('error.html', RequestContext(request, {"error_msg": error_msg}))

    add_service(request.user, obj)
    messages.success(request, u'司仪(%s) 已经加入我的婚礼方案!' % obj.name)

    return HttpResponseRedirect(reverse('wedding_overview'))


def add_service_makeup(request, obj_id):
    try:
        obj = MakeUp.objects.get(id=obj_id)
    except ObjectDoesNotExist:
        error_msg = '化妆师(id=%s)不存在!' % obj_id
        return render_to_response('error.html', RequestContext(request, {"error_msg": error_msg}))

    add_service(request.user, obj)
    messages.success(request, u'化妆师 (%s) 已经加入我的婚礼方案!' % obj.name)

    return HttpResponseRedirect(reverse('wedding_overview'))


def overview(request):
    content = wed_program(request.user)
    return render_to_response('overview.html', RequestContext(request, content))


def charge(request, cart_id):
    cart_obj = CartInfo.objects.get(id=cart_id)

    t_wed = WedEssential.objects.get(user=request.user).t_wed

    kwargs = {
        "buyer": cart_obj.buyer,
        "amount": cart_obj.amount,
        "content_object": cart_obj.content_object,
        "status": 1,
        "t_wed": t_wed,
        }

    Order(**kwargs).save()
    cart_obj.delete()

    content = wed_program(request.user)
    return render_to_response('overview.html', RequestContext(request, content))

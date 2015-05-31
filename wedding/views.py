#-*- coding:utf-8 -*-
import datetime
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages

from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist

from expert.models import MC, MakeUp
from std_product.models import WedFlower
from wedding.models import CartInfo, WedEssential, Order

import base.choices as choise_set


def diy(request):
    content = {
        'flower': choise_set.C_FLOWER_CATE,
        'av': choise_set.C_AV_CATE,
        'stage': choise_set.C_STAGE_CATE,
        }
    return render_to_response('diy.html', RequestContext(request, content))



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
    c_type= ContentType.objects.get_for_model(obj)
    try:
        item = Order.objects.get(buyer=user, object_id=obj.id, content_type__pk=c_type.id)
    except ObjectDoesNotExist:  # not exists in order table
        try:
            item = CartInfo.objects.get(buyer=user, object_id=obj.id, content_type__pk=c_type.id)
            lvl = messages.WARNING
            msg = u'%s ( %s ) 已经在我的婚礼方案中, 无需重复加入!' % (c_type, obj.name)
        except ObjectDoesNotExist:  # add new item to cart
            CartInfo(buyer=user, content_object=obj, amount=1).save()
            lvl = messages.SUCCESS
            msg = u'%s ( %s ) 成功加入我的婚礼方案!' % (c_type, obj.name)
    else:
        lvl = messages.ERROR
        msg = u'%s ( %s ) 已经下单, 无需重复加入!' % (c_type, obj.name)
    return lvl, msg


def add_product(user, obj, amount):
    c_type= ContentType.objects.get_for_model(obj)
    try:
        item = CartInfo.objects.get(buyer=user, object_id=obj.id, content_type__pk=c_type.id)
    except ObjectDoesNotExist:  # add new item to cart
        CartInfo(buyer=user, content_object=obj, amount=amount).save()
        lvl = messages.SUCCESS
        msg = u'%s 件 %s ( %s ) 成功加入我的婚礼方案!' % (amount, c_type, obj.name)
    else:
        item.amount += amount
        item.save()
        lvl = messages.WARNING
        msg = u'新增 %s 件 %s ( %s ), 共计 %s 件!' % (amount, c_type, obj.name, item.amount)
    return lvl, msg


def add_service_mc(request, obj_id):
    try:
        obj = MC.objects.get(id=obj_id)
    except ObjectDoesNotExist:
        error_msg = '司仪(id=%s)不存在!' % obj_id
        return render_to_response('error.html', RequestContext(request, {"error_msg": error_msg}))

    lvl, msg = add_service(request.user, obj)
    messages.add_message(request, lvl, msg)

    return HttpResponseRedirect(reverse('wedding_overview'))


def add_service_makeup(request, obj_id):
    try:
        obj = MakeUp.objects.get(id=obj_id)
    except ObjectDoesNotExist:
        error_msg = '化妆师(id=%s)不存在!' % obj_id
        return render_to_response('error.html', RequestContext(request, {"error_msg": error_msg}))

    lvl, msg = add_service(request.user, obj)
    messages.add_message(request, lvl, msg)

    return HttpResponseRedirect(reverse('wedding_overview'))


def overview(request):
    content = wed_program(request.user)
    return render_to_response('overview.html', RequestContext(request, content))


def is_booked(t_wed, obj_id, obj_type, user=None):
    """check if a service(obj_type, obj_id) is booked on t_wed

    0: unbooked
    1: booked by others
    2: booked by user
    """
    try:
        item = Order.objects.get(t_wed=t_wed, object_id=obj_id, content_type__pk=obj_type.id)
    except ObjectDoesNotExist:
        return 0  # False
    else:  # True
        return (item.user == user) + 1


def book(request, t_wed, cart_id):

    cart_obj = CartInfo.objects.get(id=cart_id)
    c_type = cart_obj.content_type
    obj = cart_obj.content_object

    if is_booked(t_wed, obj.id, c_type):
        lvl = messages.ERROR
        msg = u'%s ( %s ) 档期不可用!' % (c_type, obj.name)
    else:
        kwargs = {
            "buyer": request.user,
            "content_object": obj,
            "t_wed": t_wed,
            "amount": 1,
            "status": 1,
            }
        Order(**kwargs).save()
        cart_obj.delete()

        lvl = messages.SUCCESS
        msg = u'%s ( %s ) 预定成功, 请尽快付款完成购买!' % (c_type, obj.name)

    messages.add_message(request, lvl, msg)
    return HttpResponseRedirect(reverse('wedding_overview'))


def add_product_flower(request, obj_id, amount_str):
    amount = int(amount_str)

    try:
        obj = WedFlower.objects.get(id=obj_id)
    except ObjectDoesNotExist:
        error_msg = '花艺(id=%s)不存在!' % obj_id
        return render_to_response('error.html', RequestContext(request, {"error_msg": error_msg}))

    lvl, msg = add_product(request.user, obj, amount)
    messages.add_message(request, lvl, msg)

    return HttpResponseRedirect(reverse('wedding_overview'))

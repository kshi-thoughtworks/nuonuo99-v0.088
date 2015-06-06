#-*- coding:utf-8 -*-
import datetime
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages

from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist 
from expert.models import MC, MakeUp, Photographer, VedioGuys
from std_product.models import WedFlower, WedAv, StageEffect
from wedding.models import WedScheme, WedEssential, Order
from provider.models import ProviderInfo

from wedding.forms import WedEssentialForm

import base.choices as choise_set

from django.contrib.auth.decorators import login_required


@login_required
def diy(request):

    user = request.user

    try:
        wed_info = WedEssential.objects.get(user=user)
    except ObjectDoesNotExist:
        wed_info = None


    mc_type= ContentType.objects.get_for_model(MC)
    makeup_type= ContentType.objects.get_for_model(MakeUp)
    photo_type= ContentType.objects.get_for_model(Photographer)
    vedio_type= ContentType.objects.get_for_model(VedioGuys)
    flower_type= ContentType.objects.get_for_model(WedFlower)
    av_type= ContentType.objects.get_for_model(WedAv)
    stage_type= ContentType.objects.get_for_model(StageEffect)

    content = {
        'flower_cate': choise_set.C_FLOWER_CATE,
        'av_cate': choise_set.C_AV_CATE,
        'stage_cate': choise_set.C_STAGE_CATE,

        'mc_item': WedScheme.objects.filter(owner=user, content_type__pk=mc_type.id),
        'makeup_item': WedScheme.objects.filter(owner=user, content_type__pk=makeup_type.id),
        'photographer_item': WedScheme.objects.filter(owner=user, content_type__pk=photo_type.id),
        'vedioguys_item': WedScheme.objects.filter(owner=user, content_type__pk=vedio_type.id),
        'flower_item': WedScheme.objects.filter(owner=user, content_type__pk=flower_type.id),
        'av_item': WedScheme.objects.filter(owner=user, content_type__pk=av_type.id),
        'stage_item': WedScheme.objects.filter(owner=user, content_type__pk=stage_type.id),

        'mc_item_order': Order.objects.filter(buyer=user, content_type__pk=mc_type.id),
        'makeup_item_order': Order.objects.filter(buyer=user, content_type__pk=makeup_type.id),
        'photographer_item_order': Order.objects.filter(buyer=user, content_type__pk=photo_type.id),
        'vedioguys_item_order': Order.objects.filter(buyer=user, content_type__pk=vedio_type.id),
        'flower_item_order': Order.objects.filter(buyer=user, content_type__pk=flower_type.id),
        'av_item_order': Order.objects.filter(buyer=user, content_type__pk=av_type.id),
        'stage_item_order': Order.objects.filter(buyer=user, content_type__pk=stage_type.id),

        'wed_info': wed_info,
        }
    return render_to_response('diy.html', RequestContext(request, content))


def scheme_overview(request):

    user = request.user

    try:
        wed_info = WedEssential.objects.get(user=user)
    except ObjectDoesNotExist:
        wed_info = None


    mc_type= ContentType.objects.get_for_model(MC)
    makeup_type= ContentType.objects.get_for_model(MakeUp)
    photo_type= ContentType.objects.get_for_model(Photographer)
    vedio_type= ContentType.objects.get_for_model(VedioGuys)
    flower_type= ContentType.objects.get_for_model(WedFlower)
    av_type= ContentType.objects.get_for_model(WedAv)
    stage_type= ContentType.objects.get_for_model(StageEffect)

    content = {
        'flower_cate': choise_set.C_FLOWER_CATE,
        'av_cate': choise_set.C_AV_CATE,
        'stage_cate': choise_set.C_STAGE_CATE,

        'mc_item': WedScheme.objects.filter(owner=user, content_type__pk=mc_type.id),
        'makeup_item': WedScheme.objects.filter(owner=user, content_type__pk=makeup_type.id),
        'photographer_item': WedScheme.objects.filter(owner=user, content_type__pk=photo_type.id),
        'vedioguys_item': WedScheme.objects.filter(owner=user, content_type__pk=vedio_type.id),
        'flower_item': WedScheme.objects.filter(owner=user, content_type__pk=flower_type.id),
        'av_item': WedScheme.objects.filter(owner=user, content_type__pk=av_type.id),
        'stage_item': WedScheme.objects.filter(owner=user, content_type__pk=stage_type.id),

        'mc_item_order': Order.objects.filter(buyer=user, content_type__pk=mc_type.id),
        'makeup_item_order': Order.objects.filter(buyer=user, content_type__pk=makeup_type.id),
        'photographer_item_order': Order.objects.filter(buyer=user, content_type__pk=photo_type.id),
        'vedioguys_item_order': Order.objects.filter(buyer=user, content_type__pk=vedio_type.id),
        'flower_item_order': Order.objects.filter(buyer=user, content_type__pk=flower_type.id),
        'av_item_order': Order.objects.filter(buyer=user, content_type__pk=av_type.id),
        'stage_item_order': Order.objects.filter(buyer=user, content_type__pk=stage_type.id),

        'wed_info': wed_info,
        }
    return render_to_response('scheme_overview.html', RequestContext(request, content))


def add_service(user, obj):
    c_type= ContentType.objects.get_for_model(obj)
    try:
        item = Order.objects.get(buyer=user, object_id=obj.id, content_type__pk=c_type.id)
    except ObjectDoesNotExist:  # not exists in order table
        try:
            item = WedScheme.objects.get(owner=user, object_id=obj.id, content_type__pk=c_type.id)
            lvl = messages.WARNING
            msg = u'%s ( %s ) 已经在我的婚礼方案中, 无需重复加入!' % (c_type, obj.name)
        except ObjectDoesNotExist:  # add new item to cart
            WedScheme(owner=user, content_object=obj, amount=1).save()
            lvl = messages.SUCCESS
            msg = u'%s ( %s ) 成功加入我的婚礼方案!' % (c_type, obj.name)
    else:
        lvl = messages.ERROR
        msg = u'%s ( %s ) 已经下单, 无需重复加入!' % (c_type, obj.name)
    return lvl, msg


def add_product(user, obj, amount):
    c_type= ContentType.objects.get_for_model(obj)
    try:
        item = WedScheme.objects.get(owner=user, object_id=obj.id, content_type__pk=c_type.id)
    except ObjectDoesNotExist:  # add new item to cart
        WedScheme(owner=user, content_object=obj, amount=amount).save()
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


def add_service_photo(request, obj_id):
    try:
        obj = Photographer.objects.get(id=obj_id)
    except ObjectDoesNotExist:
        error_msg = '化妆师(id=%s)不存在!' % obj_id
        return render_to_response('error.html', RequestContext(request, {"error_msg": error_msg}))

    lvl, msg = add_service(request.user, obj)
    messages.add_message(request, lvl, msg)

    return HttpResponseRedirect(reverse('wedding_overview'))


def add_service_vedio(request, obj_id):
    try:
        obj = VedioGuys.objects.get(id=obj_id)
    except ObjectDoesNotExist:
        error_msg = '摄影师(id=%s)不存在!' % obj_id
        return render_to_response('error.html', RequestContext(request, {"error_msg": error_msg}))

    lvl, msg = add_service(request.user, obj)
    messages.add_message(request, lvl, msg)

    return HttpResponseRedirect(reverse('wedding_overview'))


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

    cart_obj = WedScheme.objects.get(id=cart_id)
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


def buy(request, t_wed, cart_id):
    cart_obj = WedScheme.objects.get(id=cart_id)
    c_type = cart_obj.content_type
    obj = cart_obj.content_object

    try:
        item = Order.objects.get(t_wed=t_wed, object_id=obj.id, content_type__pk=c_type.id)
    except ObjectDoesNotExist:
        kwargs = {
            "buyer": request.user,
            "content_object": cart_obj.content_object,
            "t_wed": t_wed,
            "amount": cart_obj.amount,
            "status": 1,
        }
        item = Order(**kwargs)
    else:
        item.amount += cart_obj.amount

    item.save()
    cart_obj.delete()

    return HttpResponseRedirect(reverse('wedding_overview'))


def delete(request, cart_id):
    cart_obj = WedScheme.objects.get(id=cart_id)
    cart_obj.delete()
    c_type = cart_obj.content_type
    obj = cart_obj.content_object

    lvl = messages.SUCCESS
    msg = u'%s ( %s ) 删除成功!' % (c_type, obj.name)

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


def add_product_av(request, obj_id, amount_str):
    amount = int(amount_str)

    try:
        obj = WedAv.objects.get(id=obj_id)
    except ObjectDoesNotExist:
        error_msg = 'AV 工程(id=%s)不存在!' % obj_id
        return render_to_response('error.html', RequestContext(request, {"error_msg": error_msg}))

    lvl, msg = add_product(request.user, obj, amount)
    messages.add_message(request, lvl, msg)

    return HttpResponseRedirect(reverse('wedding_overview'))


def add_product_stage(request, obj_id, amount_str):
    amount = int(amount_str)

    try:
        obj = StageEffect.objects.get(id=obj_id)
    except ObjectDoesNotExist:
        error_msg = '舞台背景(id=%s)不存在!' % obj_id
        return render_to_response('error.html', RequestContext(request, {"error_msg": error_msg}))

    lvl, msg = add_product(request.user, obj, amount)
    messages.add_message(request, lvl, msg)

    return HttpResponseRedirect(reverse('wedding_overview'))


def edit_essential(request):
    try:
        obj = WedEssential.objects.get(user=request.user)
    except ObjectDoesNotExist:
        obj = WedEssential(user=request.user)

    if request.method == 'POST':
        f = WedEssentialForm(request.POST, instance=obj)
        if f.is_valid():
            f.save()
            return HttpResponseRedirect(reverse('wedding_overview'))
    else:
        f = WedEssentialForm(instance=obj)
    return render_to_response('edit-essential.html', RequestContext(request, {'data': obj}))


def update_p_wed(request, c_type, pid):
    provider = ProviderInfo.objects.get(id=pid)
    wed_info = WedEssential.objects.get(user=request.user)
    if c_type == 'flower':
        wed_info.p_flower = provider
    elif c_type == 'av':
        wed_info.p_av = provider
    else:
        wed_info.p_stage = provider
    wed_info.save()
    return HttpResponseRedirect(reverse('wedding_overview'))


def update_product(request, cart_id):
    cart_obj = WedScheme.objects.get(id=cart_id)
    cart_obj.amount = request.GET['amount']
    cart_obj.save()

    return HttpResponseRedirect(reverse('wedding_overview'))

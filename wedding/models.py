#-*- coding:utf-8 -*-
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from django.contrib.auth.models import User
from location.models import County
from base.choices import C_ORDER_STATUS
from provider.models import ProviderInfo

import datetime
import base.models as choice_set


class WedEssential(models.Model):
    boy = models.CharField(u'新郎', max_length=255)
    girl = models.CharField(u'新娘', max_length=255)
    t_wed = models.DateField(u'婚期')

    user = models.ForeignKey(User, verbose_name=u'用户')

    expect = models.TextField(u'婚礼期望', max_length=2000, blank=True)
    # loc = models.ForeignKey(County, verbose_name=u'地点')
    btm_table_num = models.IntegerField(u'桌数(最少)')
    top_table_num = models.IntegerField(u'桌数(最多)')

    p_flower = models.ForeignKey(ProviderInfo, verbose_name=u'花艺供应商', related_name="p_flower", null=True, blank=True)
    p_av = models.ForeignKey(ProviderInfo, verbose_name=u'AV 供应商', related_name="p_av", null=True, blank=True)
    p_stage = models.ForeignKey(ProviderInfo, verbose_name=u'舞台效果供应商', related_name="p_stage", null=True, blank=True)

    def __unicode__(self):
        return u'%s-%s(%s)' % (self.boy, self.girl, self.t_wed)

    class Meta:
        verbose_name = u"婚礼基本信息"
        verbose_name_plural = verbose_name
        unique_together = ('user',)


class WedScheme(models.Model):
    """under decision
    """
    owner = models.ForeignKey(User, verbose_name=u'用户')

    content_type = models.ForeignKey(ContentType, verbose_name=u'商品类型')
    object_id = models.PositiveIntegerField(u'商品 ID')
    content_object = GenericForeignKey('content_type', 'object_id')

    amount = models.PositiveIntegerField(u'数量', default=0)

    t_add = models.DateTimeField(u'加入时间', default=datetime.datetime.now)


    def charge_flower(self):
        return self.content_object.price * self.amount


    def charge_step(self):
        return self.content_object.price * self.content_object.base_amount + self.content_object.float_price * (self.amount - self.content_object.base_amount)


    def __unicode__(self):
        return self.owner.username

    class Meta:
        verbose_name = u"我的婚礼方案"
        verbose_name_plural = verbose_name
        unique_together = ("owner", "content_type", "object_id")


class Order(models.Model):
    """decided

    keypoint: status, deadline. current progress
    """
    buyer = models.ForeignKey(User, verbose_name=u'购买人')
    t_wed = models.DateField(u'婚期')
    status = models.PositiveIntegerField(u'状态', choices=C_ORDER_STATUS.CHOICES,default=C_ORDER_STATUS.NOPAY)
    t_add = models.DateTimeField(u'加入时间', default=datetime.datetime.now)
    t_paid = models.DateTimeField(u'付款时间', blank=True, null=True)
    amount = models.PositiveIntegerField(u'数量', default=0)

    content_type = models.ForeignKey(ContentType, verbose_name=u'商品类型')
    object_id = models.PositiveIntegerField(u'商品 ID')
    content_object = GenericForeignKey('content_type', 'object_id')

    progress = models.CharField(u'准备进展描述', max_length=255, blank=True)

    def __unicode__(self):
        return self.buyer.username

    class Meta:
        verbose_name = u"订单"
        verbose_name_plural = verbose_name

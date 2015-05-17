#-*- coding:utf-8 -*-
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from django.contrib.auth.models import User


class CartInfo(models.Model):
    buyer = models.ForeignKey(User, verbose_name=u'购买人')
    amount = models.PositiveIntegerField(u'数量')

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    # t_add = models.TimeField(u'加入时间', default=time.time())

    def __unicode__(self):
        return self.buyer.username

    class Meta:
        verbose_name = u"购物车"
        verbose_name_plural = verbose_name

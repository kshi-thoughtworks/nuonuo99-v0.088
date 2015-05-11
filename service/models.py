#-*- coding:utf-8 -*-
from django.db import models
from base.models import C_FlowerCategory
from provider.models import ProviderInfo

from django.conf import settings


class ServiceInfo(models.Model):
    """Abstract service info class

    TODO: SLA info
    """
    name = models.CharField(u'服务名称', max_length=255)
    provider = models.ForeignKey(ProviderInfo, verbose_name=u'供应商')
    desc = models.TextField(u'原材料介绍', blank=True)

    photo1 = models.FileField(u'样图1', upload_to=settings.SERVICE_PATH)
    photo2 = models.FileField(u'样图2', upload_to=settings.SERVICE_PATH, blank=True)
    photo3 = models.FileField(u'样图3', upload_to=settings.SERVICE_PATH, blank=True)
    photo4 = models.FileField(u'样图4', upload_to=settings.SERVICE_PATH, blank=True)

    # product TODO
    product_desc = models.TextField(u'商品描述', blank=True)
    price = models.FloatField(u'售价')

    class Meta:
        abstract = True


class S_Flower(ServiceInfo):
    """花艺服务"""
    category = models.ForeignKey(C_FlowerCategory, verbose_name=u'花艺类型')
    color = models.CharField(u'颜色', max_length=32)
    amount = models.IntegerField(u'花朵数')
    size = models.CharField(u'尺寸', max_length=32)


    class Meta:
        verbose_name = "花艺服务"
        verbose_name_plural = verbose_name

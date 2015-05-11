#-*- coding:utf-8 -*-
from django.db import models
from provider.models import ProviderInfo


class ServiceInfo(models.Model):
    """Abstract service info class

    TODO: SLA info
    """
    name = models.CharField(u'服务名称', max_length=255)
    provider = models.ForeignKey(ProviderInfo, verbose_name=u'供应商')
    desc = models.TextField(u'详细说明', blank=True)

    price = models.FloatField(u'售价')  # product TODO

    class Meta:
        abstract = True


class S_Flower(ServiceInfo):
    """花艺服务"""
    amount = models.IntegerField(verbose_name='花朵数量')

    class Meta:
        verbose_name = "花艺服务"
        verbose_name_plural = verbose_name

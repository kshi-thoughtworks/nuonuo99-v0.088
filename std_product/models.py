#-*- coding:utf-8 -*-
from django.db import models
from django.conf import settings

from base.models import C_FlowerVariety, C_Scale


class StdProduct(models.Model):
    """每个产品, 推荐 4 个样图, 最少 1 个"""

    category = models.CharField(u'产品子类', max_length=7)
    name = models.CharField(u'产品名称', max_length=255)
    price = models.IntegerField(u'单价(起步单价)')
    desc = models.TextField(u'产品描述', max_length=255)

    photo1 = models.FileField(u'样图1', upload_to=settings.SERVICE_PATH)
    photo2 = models.FileField(u'样图2', upload_to=settings.SERVICE_PATH, blank=True)
    photo3 = models.FileField(u'样图3', upload_to=settings.SERVICE_PATH, blank=True)
    photo4 = models.FileField(u'样图4', upload_to=settings.SERVICE_PATH, blank=True)

    def __unicode__(self):
        return "%s-%s" % (self.name, self.price)

    class Meta:
        abstract = True


class WedFlower(StdProduct):
    """花艺产品"""
    style = models.CharField(u'样式', max_length=7)
    color = models.CharField(u'颜色', max_length=32)
    items = models.ManyToManyField(C_FlowerVariety, through='FlowerItem', through_fields=('product', 'variety'), verbose_name=u'花材')
    scale = models.ManyToManyField(C_Scale, through='FlowerScale', through_fields=('product', 'key'), verbose_name=u'尺寸')

    class Meta:
        verbose_name = u"花艺产品"
        verbose_name_plural = verbose_name


class FlowerItem(models.Model):
    product = models.ForeignKey(WedFlower, verbose_name=u'花艺产品')
    variety = models.ForeignKey(C_FlowerVariety, verbose_name=u'鲜花品种')
    amount = models.PositiveIntegerField(u'数量')

    def __unicode__(self):
        return u'%s 朵 %s' % (self.amount, self.variety)

    class Meta:
        verbose_name = u"花艺原料组成细节"
        verbose_name_plural = verbose_name
        unique_together = ("product", "variety")


class FlowerScale(models.Model):
    product = models.ForeignKey(WedFlower, verbose_name=u'花艺产品')
    key = models.ForeignKey(C_Scale, verbose_name=u'尺寸类型')
    value = models.PositiveIntegerField(u'数值')

    def __unicode__(self):
        return '%s: %s' % (self.key, self.value)

    class Meta:
        verbose_name = u"花艺产品尺寸细节"
        verbose_name_plural = verbose_name
        unique_together = ("product", "key")

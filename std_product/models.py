#-*- coding:utf-8 -*-
from django.db import models
from django.conf import settings

import base.choices as choice_set
from base.models import C_FlowerVariety, C_Scale


class StdProduct(models.Model):
    """每个产品, 推荐 4 个样图, 最少 1 个"""

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


class flower(StdProduct):
    """花艺产品"""
    category = models.IntegerField(u'产品子类', choices=choice_set.C_FLOWER_CATE)
    style = models.IntegerField(u'样式', choices=choice_set.C_FLOWER_STYLE, null=True, blank=True)
    color = models.CharField(u'颜色', max_length=32)
    items = models.ManyToManyField(C_FlowerVariety, through='FlowerItem', through_fields=('product', 'variety'), verbose_name=u'花材')
    scale = models.ManyToManyField(C_Scale, through='FlowerScale', through_fields=('product', 'key'), verbose_name=u'尺寸')

    def validate_amount(self, amount):
        return amount > 0

    class Meta:
        verbose_name = u"花艺产品"
        verbose_name_plural = verbose_name


class FlowerItem(models.Model):
    product = models.ForeignKey(flower, verbose_name=u'花艺产品')
    variety = models.ForeignKey(C_FlowerVariety, verbose_name=u'鲜花品种')
    amount = models.PositiveIntegerField(u'数量')

    def __unicode__(self):
        return u'%s 朵 %s' % (self.amount, self.variety)

    class Meta:
        verbose_name = u"花艺原料组成细节"
        verbose_name_plural = verbose_name
        unique_together = ("product", "variety")


class FlowerScale(models.Model):
    product = models.ForeignKey(flower, verbose_name=u'花艺产品')
    key = models.ForeignKey(C_Scale, verbose_name=u'尺寸类型')
    value = models.PositiveIntegerField(u'数值')

    def __unicode__(self):
        return '%s: %s' % (self.key, self.value)

    class Meta:
        verbose_name = u"花艺产品尺寸细节"
        verbose_name_plural = verbose_name
        unique_together = ("product", "key")


class av(StdProduct):
    """AV 产品"""
    category = models.IntegerField(u'产品子类', choices=choice_set.C_AV_CATE)
    wed_env = models.IntegerField(u'使用场地', choices=choice_set.C_WED_ENV)
    power = models.PositiveIntegerField(u'功率')
    coverage = models.PositiveIntegerField(u'覆盖面积(m^2)')

    base_amount = models.PositiveIntegerField(u'起步数量')
    unit = models.CharField(u'计价单位', max_length=7)
    amount_step = models.PositiveIntegerField(u'计价数量')
    float_price = models.PositiveIntegerField(u'计价价格')

    def validate_amount(self, amount):
        return (amount > self.base_amount) and ((amount - self.base_amount) % self.amount_step) == 0

    def notes(self):
        return u'起步数量 %s, 起步单价 %s, 计价数量 %s, 计价价格 %s' % (self.base_amount, self.price, self.amount_step, self.float_price)

    class Meta:
        verbose_name = u"AV 产品"
        verbose_name_plural = verbose_name


class stage(StdProduct):
    """舞台效果"""
    category = models.IntegerField(u'产品子类', choices=choice_set.C_STAGE_CATE)
    sub_category = models.IntegerField(u'种类', choices=choice_set.C_STAGE_SUB_CATE, null=True, blank=True)
    wed_env = models.IntegerField(u'使用场地', choices=choice_set.C_WED_ENV)

    base_amount = models.PositiveIntegerField(u'起步数量')
    unit = models.CharField(u'计价单位', max_length=7)
    amount_step = models.PositiveIntegerField(u'计价数量')
    float_price = models.PositiveIntegerField(u'计价价格')

    def validate_amount(self, amount):
        return (amount > self.base_amount) and ((amount - self.base_amount) % self.amount_step) == 0

    def notes(self):
        return u'起步数量 %s, 起步单价 %s, 计价数量 %s, 计价价格 %s' % (self.base_amount, self.price, self.amount_step, self.float_price)

    class Meta:
        verbose_name = u"舞台效果"
        verbose_name_plural = verbose_name

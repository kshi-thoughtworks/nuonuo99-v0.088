#-*- coding:utf-8 -*-
from django.db import models
from django.conf import settings

import base.models as choice_set

from location.models import County


_help_text_charge = u'-1 -- 不提供该服务. 0 -- 免费提供. > 0 -- 提供且收取对应的费用'


class Expert(models.Model):
    name = models.CharField(u'姓名', max_length=255)
    price = models.DecimalField(u'基础报价', max_digits=8, decimal_places=2)
    avatar = models.FileField(u'头像', upload_to=settings.SERVICE_PATH)

    # basic info
    gender = models.IntegerField(u'性别', choices=choice_set.C_GENDER)  # use boolean field instead

    # https://github.com/kugua456/nuonuo99-v0.88/issues/13
    # t_birth_age = models.IntegerField(u'年龄', choices=choice_set.C_AGE)  # TODO

    # service info
    wed_style = models.IntegerField(u'专业', choices=choice_set.C_WEDDING_STYLE)
    t_start = models.DateField(u'工作开始时间', help_text=u'从业时间 = 当前时间-工作开始时间)')
    desc = models.TextField(u'服务理念', max_length=255)

    # more info
    honor = models.TextField(u'所获荣誉', blank=True)

    def product_key(self):
        return '%s_%s' % (self._meta.object_name.lower(), self.id)


    def __unicode__(self):
        return "%s-%s" % (self.name, self.price)

    class Meta:
        abstract = True


class MC(Expert):
    """司仪服务 master of ceremonies"""
    loc_native = models.ForeignKey(County, verbose_name=u'祖籍')
    language = models.IntegerField(u'语言', choices=choice_set.C_LANG, default=0)
    height = models.IntegerField(u'身高')

    photo_chinse = models.FileField(u'中式定妆照', upload_to=settings.SERVICE_PATH, blank=True)
    photo_west = models.FileField(u'西式定妆照', upload_to=settings.SERVICE_PATH, blank=True)
    photo_life = models.FileField(u'生活照', upload_to=settings.SERVICE_PATH, blank=True)

    vcr = models.CharField(u'自我介绍视频 url', max_length=255, blank=True)

    class Meta:
        verbose_name = u"司仪服务"
        verbose_name_plural = verbose_name


class MakeUp(Expert):
    """化妆师"""

    cosmetics_brand = models.CharField(u'常用化妆品品牌', max_length=255)
    is_cosmetics_imported = models.BooleanField(u'进口化妆品', default=False)
    photo_life = models.FileField(u'生活照', upload_to=settings.SERVICE_PATH, blank=True)
    vcr = models.FileField(u'自我介绍视频', upload_to=settings.SERVICE_PATH, blank=True)

    charge_decoration = models.FloatField(u'提供饰品, 加价',
        help_text=_help_text_charge)
    charge_hair = models.FloatField(u'提供盘头, 加价',
        help_text=_help_text_charge)
    charge_dress_mum = models.FloatField(u'提供妈妈装, 加价',
        help_text=_help_text_charge)
    charge_dress_peer = models.FloatField(u'提供伴娘装, 加价',
        help_text=_help_text_charge)

    class Meta:
        verbose_name = u"化妆师"
        verbose_name_plural = verbose_name

#-*- coding:utf-8 -*-
from django.db import models
import base.models as choice_set
from provider.models import ProviderInfo

from django.conf import settings


_help_text_charge = u'-1 -- 不提供该服务. 0 -- 免费提供. > 0 -- 提供且收取对应的费用'


class AvatarBase(models.Model):
    avatar = models.FileField(u'头像', upload_to=settings.SERVICE_PATH)

    def avatar_html(self):
        return '<img src="%s" style="width:180px;" title="%s"/>' % (self.avatar.url, self.name)

    avatar_html.short_description = "头像"
    avatar_html.allow_tags = True

    class Meta:
        abstract = True

class StdProduct(AvatarBase):
    """Abstract service info class

    TODO: SLA info
    """
    name = models.CharField(u'服务名称', max_length=255)
    provider = models.ForeignKey(ProviderInfo, verbose_name=u'供应商')

    # product TODO
    product_desc = models.TextField(u'商品描述', blank=True)
    price = models.FloatField(u'售价')


    class Meta:
        abstract = True


class S_Flower(StdProduct):
    """花艺服务"""
    category = models.ForeignKey(choice_set.C_FlowerCategory, verbose_name=u'花艺类型')
    color = models.CharField(u'颜色', max_length=32)
    amount = models.IntegerField(u'花朵数')
    size = models.CharField(u'尺寸', max_length=32)

    desc = models.TextField(u'原材料介绍', blank=True)
    photo1 = models.FileField(u'样图1', upload_to=settings.SERVICE_PATH)
    photo2 = models.FileField(u'样图2', upload_to=settings.SERVICE_PATH, blank=True)
    photo3 = models.FileField(u'样图3', upload_to=settings.SERVICE_PATH, blank=True)
    photo4 = models.FileField(u'样图4', upload_to=settings.SERVICE_PATH, blank=True)


    class Meta:
        verbose_name = u"花艺服务"
        verbose_name_plural = verbose_name


class Expert(AvatarBase):
    name = models.CharField(u'姓名', max_length=255)
    gender = models.IntegerField(u'性别', choices=choice_set.C_GENDER)
    t_birth_age = models.DateField(u'出生年')

    desc = models.TextField(u'服务理念', max_length=255)
    wed_style = models.IntegerField(u'专业', choices=choice_set.C_WEDDING_STYLE, default=0)
    honor = models.TextField(u'所获荣誉', blank=True)

    t_start = models.DateField(u'工作开始时间',
        help_text=u'用于计算从业时间(当前时间 - 工作开始时间)')

    price = models.FloatField(u'基础报价')

    class Meta:
        abstract = True


class MC(Expert):
    """司仪服务 master of ceremonies"""
    language = models.IntegerField(u'语言', choices=choice_set.C_LANG, default=0)
    height = models.IntegerField(u'身高')

    photo_chinse = models.FileField(u'中式定妆照', upload_to=settings.SERVICE_PATH, blank=True)
    photo_west = models.FileField(u'西式定妆照', upload_to=settings.SERVICE_PATH, blank=True)
    photo_life = models.FileField(u'生活照', upload_to=settings.SERVICE_PATH, blank=True)
    vcr = models.FileField(u'自我介绍视频', upload_to=settings.SERVICE_PATH, blank=True)

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

#-*- coding:utf-8 -*-
from django.db import models
from django.conf import settings
from base.models import SlaProvider

from location.models import County
from base.choices import C_LANGUAGE, C_ProductTypeChoices, C_CAMERA_STYLE, C_CAMERA_BRAND, C_VIDEO_DEVICE_TYPE


_help_text_charge = u'-1 -- 不提供该服务. 0 -- 免费提供. > 0 -- 提供且收取对应的费用'


class Expert(models.Model):
    """婚礼人的公共属性, 10 字段

    - 姓名
    - 基础价格
    - 头像
    - 性别
    - 年龄 / 出生日期
    - 服务理念
    - 从业时间 / 从业开始时间
    - 级别
    - 自我介绍视频
    - 荣誉
    """

    name = models.CharField(u'姓名', max_length=255)
    price = models.IntegerField(u'基础价格')
    avatar = models.FileField(u'头像', upload_to=settings.SERVICE_PATH)

    # basic info
    gender = models.CharField(u'性别', max_length=7)
    t_birth = models.DateField(u'出生日期')

    # service info
    t_start = models.DateField(u'从业开始时间', help_text=u'从业时间 = 当前时间-从业开始时间')
    wed_sty = models.CharField(u'专业', max_length=7)
    desc = models.TextField(u'服务理念', max_length=255)
    # SLAtype = models.ForeignKey(SlaProvider,verbose_name='供应商评级',blank=True)

    # more info
    honor = models.TextField(u'所获荣誉', blank=True)
    vcr = models.CharField(u'自我介绍视频 url', max_length=255, blank=True)

    def product_key(self):
        return '%s_%s' % (self._meta.object_name.lower(), self.id)

    def __unicode__(self):
        return "%s-%s" % (self.name, self.price)

    class Meta:
        abstract = True


class MC(Expert):
    """司仪服务 master of ceremonies"""
    loc_native = models.ForeignKey(County, verbose_name=u'祖籍')
    language = models.IntegerField(u'语言', choices=C_LANGUAGE.CHOICES, default=C_LANGUAGE.PUTONG)
    height = models.IntegerField(u'身高(cm)')

    photo_chinse = models.FileField(u'中式定妆照', upload_to=settings.SERVICE_PATH, blank=True)
    photo_west = models.FileField(u'西式定妆照', upload_to=settings.SERVICE_PATH, blank=True)
    photo_life = models.FileField(u'生活照', upload_to=settings.SERVICE_PATH, blank=True)



    class Meta:
        verbose_name = u"司仪服务"
        verbose_name_plural = verbose_name


class MakeUp(Expert):
    """化妆师"""

    cosmetics_brand = models.CharField(u'常用化妆品品牌', max_length=255, blank=True)
    is_cosmetics_imported = models.BooleanField(u'进口化妆品', default=False)
    photo_life = models.FileField(u'生活照', upload_to=settings.SERVICE_PATH, blank=True)


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


class photo(Expert):
    """摄影师"""

    camera_brand = models.PositiveIntegerField(u'使用相机品牌',choices=C_CAMERA_BRAND.CHOICES)
    size = models.IntegerField(u'设备类型', choices=C_CAMERA_STYLE.CHOICES)

    class Meta:
        verbose_name = u"摄影师"
        verbose_name_plural = verbose_name


class video(Expert):
    """摄像师"""

    VIDEO_DEVICE_TYPE = models.PositiveIntegerField(u'使用设备类型',choices=C_VIDEO_DEVICE_TYPE.CHOICES)

    charge_yaobi=models.FloatField(u'提供摇臂,加价',
        help_text=_help_text_charge)

    class Meta:
        verbose_name = u"摄像师"
        verbose_name_plural = verbose_name

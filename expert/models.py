#-*- coding:utf-8 -*-
from django.db import models
from django.conf import settings
from base.models import SlaExpert

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
    desc = models.TextField(u'服务理念', max_length=255)
    sla = models.ForeignKey(SlaExpert, verbose_name='等级')

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
    """司仪 master of ceremonies"""
    wed_sty = models.CharField(u'专业', max_length=7)
    lang = models.CharField(u'主持语言', max_length=7)
    height = models.IntegerField(u'身高(cm)')
    loc_native = models.ForeignKey(County, verbose_name=u'籍贯')

    photo_chinse = models.FileField(u'中式定妆照', upload_to=settings.SERVICE_PATH, blank=True)
    photo_west = models.FileField(u'西式定妆照', upload_to=settings.SERVICE_PATH, blank=True)
    photo_life = models.FileField(u'生活照', upload_to=settings.SERVICE_PATH, blank=True)

    # mc_num = models.IntegerField(u'主持场次')
    mc_tech = models.CharField(u'主持才艺', max_length=255, blank=True)
    mc_sty = models.CharField(u'主持风格', max_length=255, blank=True)

    class Meta:
        verbose_name = u"司仪"
        verbose_name_plural = verbose_name


class MakeUp(Expert):
    """化妆师"""

    wed_sty = models.CharField(u'专业', max_length=7)
    cosmetics_brand = models.CharField(u'常用化妆品品牌', max_length=255, blank=True)
    is_cosmetics_imported = models.BooleanField(u'进口化妆品', default=False)
    makeup_sty = models.CharField(u'化妆风格', max_length=7)

    charge_decoration = models.FloatField(u'饰品加价',
        help_text=_help_text_charge)
    charge_hair = models.FloatField(u'盘头加价',
        help_text=_help_text_charge)
    charge_dress_mum = models.FloatField(u'妈妈装加价',
        help_text=_help_text_charge)
    charge_dress_peer = models.FloatField(u'伴娘装加价',
        help_text=_help_text_charge)

    class Meta:
        verbose_name = u"化妆师"
        verbose_name_plural = verbose_name


class Photographer(Expert):
    """摄影师"""

    device_brand = models.CharField(u'相机品牌', max_length=255, blank=True)
    is_full_frame = models.BooleanField(u'全画幅', default=False)
    no_teamwork = models.BooleanField(u'不与他人合作', default=False)

    class Meta:
        verbose_name = u"摄影师"
        verbose_name_plural = verbose_name


class VedioGuys(Expert):
    """摄像师"""

    use_camera = models.BooleanField(u'使用照相机', default=False)

    charge_arm = models.FloatField(u'摇臂加价',
        help_text=_help_text_charge)

    class Meta:
        verbose_name = u"摄像师"
        verbose_name_plural = verbose_name

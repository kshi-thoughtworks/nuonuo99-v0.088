#-*- coding:utf-8 -*-
from django.db import models
from django.conf import settings
from choices import C_ORDER_STATUS, C_LANGUAGE, C_ProductTypeChoices


# ---------------- Scenario 大类信息 ----------------------------

class Scenario(models.Model):
    sid = models.CharField(u'唯一标识码', primary_key=True,
        max_length=31,
        help_text=u'接口间传递数据时, 使用该字段区分业务类型')
    name = models.CharField(u'名称', max_length=255,
        help_text=u'用户友好的名称, 用于界面展示等')
    parent = models.ForeignKey('self', verbose_name=u'父节点', null=True)
    desc = models.TextField(u'备注说明', blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'业务类型'
        verbose_name_plural = verbose_name


# ----------------- Key - value of DIY Filter -------------------

class DiyFilter(models.Model):
    Q_KEYS = (
            ('gender', u'性别'),
            ('wed_sty', u'专业'),
            ('t_birth', u'年龄'),
            )
    scen = models.ForeignKey(Scenario, verbose_name=u'业务类型')
    name = models.CharField(u'查询字段名', max_length=7, choices=Q_KEYS)
    value = models.CharField(u'值', max_length=255,
        help_text=u'取值, 用于接口间传递数据, 代码友好')
    value_disp = models.CharField(u'显示值', max_length=255,
        help_text=u'取值, 用于界面显示, 用户友好')
    order = models.PositiveIntegerField(u'顺序号',
        help_text=u'界面展示时, 按序列号从小到大显示 value')
    desc = models.TextField(u'备注说明', blank=True)

    def __unicode__(self):
        return '%s=%s' % (self.name, self.value_disp)

    class Meta:
        verbose_name = u'DIY 过滤器'
        verbose_name_plural = verbose_name

# ---------------------------------------------------------------

class SlaBase(models.Model):
    """Abstract Choice info class"""
    order = models.PositiveIntegerField(u'排序等级', default=5)
    name = models.CharField(u'名称', max_length=255)
    desc = models.TextField(u'详细说明', blank=True)
    # type = models.PositiveIntegerField(u'供应商类型', choices=C_ProductTypeChoices.CHOICES)


    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True


class SlaProvider(SlaBase):

    class Meta:
        verbose_name = "供应商星级"
        verbose_name_plural = verbose_name


class SlaExpert(SlaBase):

    class Meta:
        verbose_name = "婚礼人等级"
        verbose_name_plural = verbose_name

# ------------------- Choice --------------------------


class Choice(models.Model):
    """Abstract Choice info class"""
    keyword = models.CharField(u'keyword', max_length=31)
    name = models.CharField(u'名称', max_length=255)

    brief = models.TextField(u'简要说明', blank=True)
    # desc = models.TextField(u'详细说明', blank=True)

    # photo1 = models.FileField(u'样图1', upload_to=settings.DEMO_PATH)
    # photo2 = models.FileField(u'样图2', upload_to=settings.DEMO_PATH, blank=True)
    # photo3 = models.FileField(u'样图3', upload_to=settings.DEMO_PATH, blank=True)
    # photo4 = models.FileField(u'样图4', upload_to=settings.DEMO_PATH, blank=True)

    def __unicode__(self):
        return '%s-%s' % (self.keyword, self.name)

    class Meta:
        abstract = True


class C_Scale(Choice):
    """尺寸规格"""
    class Meta:
        verbose_name = "尺寸"
        verbose_name_plural = verbose_name


class C_FlowerVariety(Choice):
    """鲜花品种"""

    # startDate=models.DateField(u'花材可用起始日期',null=True)
    # endDate=models.DateField(u'花材可用结束日期',null=True)
    class Meta:
        verbose_name = "鲜花品种"
        verbose_name_plural = verbose_name


class C_AvType(Choice):
    """AV 类型库"""
    class Meta:
        verbose_name = "AV 类型"
        verbose_name_plural = verbose_name


class C_ChangBuType(Choice):
    """场布类型"""
    class Meta:
        verbose_name = '场布类型'
        verbose_name_plural = verbose_name

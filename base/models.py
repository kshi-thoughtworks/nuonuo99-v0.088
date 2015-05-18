#-*- coding:utf-8 -*-
from django.db import models
from django.conf import settings
from choices import C_FLOWER_STYLE_DOOR,C_ORDER_STATUS,C_WEDDINGSTYLE,C_LANGUAGE

class SlaBase(models.Model):
    """Abstract Choice info class"""
    order = models.PositiveIntegerField(u'排序等级', default=5)
    name = models.CharField(u'名称', max_length=255)
    desc = models.TextField(u'详细说明', blank=True)


    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        abstract = True


class SlaProvider(SlaBase):
    class Meta:
        verbose_name = "供应商星级"
        verbose_name_plural = verbose_name


# ------------------- Choice --------------------------



class Choice(models.Model):
    """Abstract Choice info class"""
    name = models.CharField(u'名称', max_length=255)
    brief = models.TextField(u'简要说明', blank=True)
    desc = models.TextField(u'详细说明', blank=True)
    demo1 = models.FileField(u'样图1', upload_to=settings.DEMO_PATH)
    demo2 = models.FileField(u'样图2', upload_to=settings.DEMO_PATH, blank=True)
    demo3 = models.FileField(u'样图3', upload_to=settings.DEMO_PATH, blank=True)
    demo4 = models.FileField(u'样图4', upload_to=settings.DEMO_PATH, blank=True)

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        abstract = True


class C_FlowerCategory(Choice):
    """花艺产品类型库"""

    class Meta:
        verbose_name = "花艺类型"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '%s' % self.name


class C_AvType(Choice):
    """AV 类型库"""
    class Meta:
        verbose_name = "AV 类型"
        verbose_name_plural = verbose_name



class C_FlowerType(Choice):
    """花品种库"""
    startDate=models.DateField(u'花材可用起始日期',null=True)
    endDate=models.DateField(u'花材可用结束日期',null=True)
    class Meta:
            verbose_name=u'花品种'
            verbose_name_plural=verbose_name


class C_Color(Choice):
    RGB=models.CharField(max_length=255,verbose_name=u'RGB值')
    class Meta:
            verbose_name=u'色彩'
            verbose_name_plural=verbose_name




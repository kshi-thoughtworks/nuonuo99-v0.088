#-*- coding:utf-8 -*-
from django.db import models
from django.conf import settings


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


class SLA_Provider(Choice):
    class Meta:
        verbose_name = "供应商星级"
        verbose_name_plural = verbose_name


# 类型库

class C_FlowerCategory(Choice):
    """花艺类型库"""
    class Meta:
        verbose_name = "花艺类型"
        verbose_name_plural = verbose_name

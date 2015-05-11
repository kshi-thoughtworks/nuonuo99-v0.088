#-*- coding:utf-8 -*-
from django.db import models


class Choice(models.Model):
    """Abstract Choice info class"""
    name = models.CharField(u'名称', max_length=255)
    desc = models.TextField(u'详细说明', blank=True)

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        abstract = True

#-*- coding:utf-8 -*-
from django.db import models


class Province(models.Model):
    zipcode = models.CharField(u'邮编', max_length=6)
    name = models.CharField(u'省', max_length=50)

    def __unicode__(self):
        return '%s(%s)' % (self.zipcode, self.name)

    class Meta:
        verbose_name = "省"
        verbose_name_plural = verbose_name
        ordering = ['id']

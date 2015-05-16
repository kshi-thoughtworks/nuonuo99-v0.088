#-*- coding:utf-8 -*-
from django.db import models


class Province(models.Model):
    zipcode = models.CharField(u'邮编', max_length=6)
    name = models.CharField(u'省份', max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "省份"
        verbose_name_plural = verbose_name
        ordering = ['id']


class City(models.Model):
    zipcode = models.CharField(u'邮编', max_length=6)
    name = models.CharField(u'城市', max_length=50)
    province = models.ForeignKey(Province, verbose_name=u'省份')

    def __unicode__(self):
        return '%s - %s' % (self.province, self.name)

    class Meta:
        verbose_name = "城市"
        verbose_name_plural = verbose_name
        ordering = ['id']


class County(models.Model):
    zipcode = models.CharField(u'邮编', max_length=6)
    name = models.CharField(u'区县', max_length=50)
    city = models.ForeignKey(City, verbose_name=u'省-市')

    def __unicode__(self):
        return u'%s - %s' % (self.city, self.name)

    class Meta:
        verbose_name = "区县"
        verbose_name_plural = verbose_name
        ordering = ['id']

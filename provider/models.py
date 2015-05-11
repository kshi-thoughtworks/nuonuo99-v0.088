#-*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class ProviderInfo(models.Model):
    """供应商基本信息

    """
    name = models.CharField(u'供应商名', max_length=255)
    contact = models.CharField(u'联系人', max_length=255)
    phone = models.CharField(u'手机号', max_length=16)
    address = models.TextField(u'地址', max_length=255)
    level = models.IntegerField(u'星级', default=0)  # SLA
    desc = models.TextField(u'详细描述', blank=True)

    def __unicode__(self):
        return '%s-%s(%s)' % (self.name, self.contact, self.phone)

    class Meta:
        verbose_name = u"供应商信息"
        verbose_name_plural = verbose_name

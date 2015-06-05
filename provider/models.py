#-*- coding:utf-8 -*-
from django.db import models

from django.contrib.auth.models import User
from base.models import SlaProvider

from django.conf import settings
import base.choices as choice_set


class ProviderInfo(models.Model):
    """供应商基本信息

    """
    avatar = models.FileField(u'头像', upload_to=settings.AVATAR_PATH)
    type = models.CharField(u'业务类型', choices=choice_set.C_PRODUCT_TYPE, max_length=7)
    name = models.CharField(u'供应商名', max_length=255)
    contact = models.CharField(u'联系人', max_length=255)
    phone = models.CharField(u'手机号', max_length=16)
    address = models.TextField(u'地址', max_length=255)
    level = models.ForeignKey(SlaProvider, verbose_name=u'供应商星级')
    desc = models.TextField(u'详细描述', blank=True)

    def __unicode__(self):
        return '%s-%s(%s)' % (self.name, self.contact, self.phone)

    class Meta:
        verbose_name = u"供应商信息"
        verbose_name_plural = verbose_name

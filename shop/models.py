#-*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

from expert.models import Expert


class Cart(models.Model):
    buyer = models.ForeignKey(User, verbose_name=u'购买人')
    price = models.DecimalField(u'单价', max_digits=8, decimal_places=2)

    def __unicode__(self):
        return self.buyer.username

    class Meta:
        verbose_name = u"购物车"
        verbose_name_plural = verbose_name

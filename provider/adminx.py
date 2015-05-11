#-*- coding:utf-8 -*-
import xadmin
from provider.models import SLA_Provider
from provider.models import ProviderInfo


class SLA_ProviderAdmin(object):
    list_display = ("name", "desc")


class ProviderInfoAdmin(object):
    list_display = ("name", "contact", "phone", "address", "level", "desc")


xadmin.site.register(SLA_Provider, SLA_ProviderAdmin)
xadmin.site.register(ProviderInfo, ProviderInfoAdmin)

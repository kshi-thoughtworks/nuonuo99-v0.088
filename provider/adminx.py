#-*- coding:utf-8 -*-
import xadmin
from provider.models import ProviderInfo


class ProviderInfoAdmin(object):
    list_display = ("name", "contact", "phone", "address", "level", "desc")


xadmin.site.register(ProviderInfo, ProviderInfoAdmin)

#-*- coding:utf-8 -*-
import xadmin
from service.models import S_Flower


class ServiceAdmin(object):
    list_display = ("name", "provider", "price")


xadmin.site.register(S_Flower, ServiceAdmin)

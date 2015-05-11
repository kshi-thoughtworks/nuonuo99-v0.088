#-*- coding:utf-8 -*-
import xadmin
from service.models import S_Flower, C_FlowerCategory


class ServiceAdmin(object):
    list_display = ("name", "provider", "price")


class C_FlowerCategoryAdmin(object):
    list_display = ("name", "desc")


xadmin.site.register(S_Flower, ServiceAdmin)
xadmin.site.register(C_FlowerCategory, C_FlowerCategoryAdmin)

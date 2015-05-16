#-*- coding:utf-8 -*-
import xadmin
from location.models import Province


class ProvinceAdmin(object):
    list_display = ("id", "name", "zipcode")


xadmin.site.register(Province, ProvinceAdmin)

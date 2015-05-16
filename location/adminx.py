#-*- coding:utf-8 -*-
import xadmin
from location.models import Province, City, County


class ProvinceAdmin(object):
    list_display = ("id", "name", "zipcode")


class CityAdmin(object):
    list_display = ("id", "name", "province", "zipcode")


class CountyAdmin(object):
    list_display = ("id", "name", "city", "zipcode")


xadmin.site.register(Province, ProvinceAdmin)
xadmin.site.register(City, CityAdmin)
xadmin.site.register(County, CountyAdmin)

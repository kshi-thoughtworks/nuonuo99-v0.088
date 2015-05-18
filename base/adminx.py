#-*- coding:utf-8 -*-
import xadmin
from base.models import SlaProvider, C_FlowerCategory, C_FlowerStyle


class SlaAdmin(object):
    list_display = ("order", "name", "desc")


class ChoiceAdmin(object):
    list_display = ("keyword", "name", "brief")


class C_FlowerStyleAdmin(object):
    list_display = ("keyword", "name", "category", "brief")


xadmin.site.register(SlaProvider, SlaAdmin)

xadmin.site.register(C_FlowerCategory, ChoiceAdmin)
xadmin.site.register(C_FlowerStyle, C_FlowerStyleAdmin)

#xadmin.site.register(c_model.C_Color,ChoiceAdmin)
#xadmin.site.register(c_model.C_FlowerType,ChoiceAdmin)

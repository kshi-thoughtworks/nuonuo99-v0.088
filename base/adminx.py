#-*- coding:utf-8 -*-
import xadmin
from base.models import Scenario, DiyFilter
from base.models import SlaProvider, C_FlowerStyle, C_FlowerVariety, C_Color, C_ChangBuType, C_Scale


class ScenarioAdmin(object):
    list_display = ("sid", "name", "parent", "desc")


class DiyFilterAdmin(object):
    list_display = ("scen", "name", "value_disp", "order")


class SlaAdmin(object):
    list_display = ("order", "name", "desc")


class ChoiceAdmin(object):
    list_display = ("keyword", "name", "brief")


class C_FlowerStyleAdmin(object):
    list_display = ("keyword", "name", "category", "brief")


xadmin.site.register(Scenario, ScenarioAdmin)
xadmin.site.register(DiyFilter, DiyFilterAdmin)

xadmin.site.register(SlaProvider, SlaAdmin)


xadmin.site.register(C_Color, ChoiceAdmin)
xadmin.site.register(C_Scale, ChoiceAdmin)

xadmin.site.register(C_FlowerStyle, C_FlowerStyleAdmin)
xadmin.site.register(C_FlowerVariety, ChoiceAdmin)
xadmin.site.register(C_ChangBuType,ChoiceAdmin)

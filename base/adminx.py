#-*- coding:utf-8 -*-
import xadmin
from base.models import Scenario
from base.models import C_FlowerVariety, C_ChangBuType, C_Scale
from base.models import SlaProvider, SlaExpert


class ScenarioAdmin(object):
    list_display = ("sid", "name", "parent", "desc")


class SlaAdmin(object):
    list_display = ("order", "name", "desc")


class ChoiceAdmin(object):
    list_display = ("keyword", "name", "brief")


xadmin.site.register(Scenario, ScenarioAdmin)

xadmin.site.register(SlaProvider, SlaAdmin)
xadmin.site.register(SlaExpert, SlaAdmin)


xadmin.site.register(C_Scale, ChoiceAdmin)

xadmin.site.register(C_FlowerVariety, ChoiceAdmin)
xadmin.site.register(C_ChangBuType,ChoiceAdmin)

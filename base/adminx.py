#-*- coding:utf-8 -*-
import xadmin
import base.models as c_model


class SlaAdmin(object):
    list_display = ("order", "name", "desc")


class ChoiceAdmin(object):
    list_display = ("name", "desc")




xadmin.site.register(c_model.SlaProvider, SlaAdmin)
xadmin.site.register(c_model.C_FlowerCategory, ChoiceAdmin)
xadmin.site.register(c_model.C_Color,ChoiceAdmin)
xadmin.site.register(c_model.C_FlowerType,ChoiceAdmin)

#-*- coding:utf-8 -*-
import xadmin
import base.models as c_model


class ChoiceAdmin(object):
    list_display = ("name", "desc")



xadmin.site.register(c_model.SLA_Provider, ChoiceAdmin)
xadmin.site.register(c_model.C_FlowerCategory, ChoiceAdmin)

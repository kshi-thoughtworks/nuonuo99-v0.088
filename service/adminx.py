#-*- coding:utf-8 -*-
import xadmin
import service.models as S


class ServiceAdmin(object):
    list_display = ("name", "product_desc", "price")


class ExpertAdmin(object):
    list_display = ("name", "avatar_html", "gender", "wed_style", "price")


xadmin.site.register(S.S_Flower, ServiceAdmin)
xadmin.site.register(S.MC, ExpertAdmin)
xadmin.site.register(S.MakeUp, ExpertAdmin)

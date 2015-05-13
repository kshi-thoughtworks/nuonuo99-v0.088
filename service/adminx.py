#-*- coding:utf-8 -*-
import xadmin
import service.models as S


class ServiceAdmin(object):
    list_display = ("name", "provider", "price")


class ExpertAdmin(object):
    list_display = ("name", "avatar_html", "gender", "wed_style", "price")


xadmin.site.register(S.S_Flower, ServiceAdmin)
xadmin.site.register(S.MC, ExpertAdmin)

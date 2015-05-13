#-*- coding:utf-8 -*-
import xadmin
import service.models as S


class ServiceAdmin(object):
    list_display = ("name", "provider", "price")


class McAdmin(object):
    list_display = ("name", "avatar_html", "gender", "style", "price")


xadmin.site.register(S.S_Flower, ServiceAdmin)
xadmin.site.register(S.MC, McAdmin)

#-*- coding:utf-8 -*-
import xadmin
from provider.models import ProviderInfo


class ProviderInfoAdmin(object):

    def show_avatar(self, ins):
        return '<img src="%s" style="width:180px;" title="%s"/>' % (ins.avatar.url, ins.name)

    show_avatar.short_description = "运营商头像"
    show_avatar.allow_tags = True
    show_avatar.is_column = True

    list_display = ("name", "show_avatar", "contact", "phone", "address", "level")


xadmin.site.register(ProviderInfo, ProviderInfoAdmin)

#-*- coding:utf-8 -*-
import xadmin
from expert.models import MC, MakeUp


def full_cols(*args):
    return ("product_key", "avatar_html", "name", "price") + args + ("gender", "wed_style", "desc")


class ExpertAdmin(object):

    def avatar_html(self, ins):
        return '<img src="%s" style="width:180px;" title="%s"/>' % (ins.avatar.url, ins.name)

    avatar_html.short_description = "头像"
    avatar_html.allow_tags = True


class McAdmin(ExpertAdmin):
    list_display = full_cols('loc_native', 'language')


class MakeUpAdmin(ExpertAdmin):
    list_display = full_cols('is_cosmetics_imported')


xadmin.site.register(MC, McAdmin)
xadmin.site.register(MakeUp, MakeUpAdmin)

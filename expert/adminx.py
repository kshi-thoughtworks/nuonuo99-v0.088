#-*- coding:utf-8 -*-
import xadmin
from expert.models import MC, MakeUp, Photographer, VedioGuys


def full_cols(*args):
    return ("product_key", "avatar_html", "name", "price") + args + ("is_man", "sla", "desc")


class ExpertAdmin(object):

    def avatar_html(self, ins):
        return '<img src="%s" style="width:180px;" title="%s"/>' % (ins.avatar.url, ins.name)

    avatar_html.short_description = "头像"
    avatar_html.allow_tags = True


class McAdmin(ExpertAdmin):
    list_display = full_cols('wed_sty', 'loc_native', 'lang')


class MakeUpAdmin(ExpertAdmin):
    list_display = full_cols('wed_sty', 'is_cosmetics_imported')


class PhotographerAdmin(ExpertAdmin):
    list_display = full_cols('device_brand', 'is_full_frame', 'no_teamwork')


class VedioGuysAdmin(ExpertAdmin):
    list_display = full_cols('use_camera',)


xadmin.site.register(MC, McAdmin)
xadmin.site.register(MakeUp, MakeUpAdmin)
xadmin.site.register(Photographer, PhotographerAdmin)
xadmin.site.register(VedioGuys, VedioGuysAdmin)

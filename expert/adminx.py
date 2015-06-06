#-*- coding:utf-8 -*-
import xadmin
from expert.models import mc, makeup, photographer, vedioguys


def edit_cols(group1, group2):
    return ("name", "price", "avatar", "is_man", "t_birth") + group1 + ("t_start", "sla", "desc", "honor", "vcr") + group2


def full_cols(*args):
    return ("product_key", "avatar_html", "name", "price") + args + ("is_man", "sla", "desc")


class ExpertAdmin(object):

    def avatar_html(self, ins):
        return '<img src="%s" style="width:180px;" title="%s"/>' % (ins.avatar.url, ins.name)

    avatar_html.short_description = "头像"
    avatar_html.allow_tags = True


class McAdmin(ExpertAdmin):
    fields = edit_cols(
        ('height', 'loc_native', 'wed_sty', 'lang', 'mc_tech', 'mc_sty'),
        ('photo_chinse', 'photo_west', 'photo_life')
        )
    list_display = full_cols('wed_sty', 'loc_native', 'lang')


class MakeUpAdmin(ExpertAdmin):
    fields = edit_cols(
        ('wed_sty', 'makeup_sty', 'is_cosmetics_imported', 'cosmetics_brand', 'charge_decoration', 'charge_hair', 'charge_dress_mum', 'charge_dress_peer'),
        ()
        )
    list_display = full_cols('wed_sty', 'is_cosmetics_imported')


class PhotographerAdmin(ExpertAdmin):
    fields = edit_cols( ('device_brand', 'is_full_frame', 'no_teamwork'), ())
    list_display = full_cols('device_brand', 'is_full_frame', 'no_teamwork')


class VedioGuysAdmin(ExpertAdmin):
    fields = edit_cols(('use_camera', 'charge_arm'), ())
    list_display = full_cols('use_camera',)


xadmin.site.register(mc, McAdmin)
xadmin.site.register(makeup, MakeUpAdmin)
xadmin.site.register(photographer, PhotographerAdmin)
xadmin.site.register(vedioguys, VedioGuysAdmin)

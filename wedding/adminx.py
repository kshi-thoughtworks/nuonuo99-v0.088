#-*- coding:utf-8 -*-
import xadmin
from wedding.models import WedScheme, WedEssential, Order


class WedEssentialAdmin(object):
    list_display = ("user", "boy", "girl", "t_wed", "loc", "expect")


class WedSchemeAdmin(object):

    def product_name(self, ins):
        return ins.content_object.name

    product_name.short_description = u"商品名称"
    product_name.allow_tags = True

    def product_price(self, ins):
        return ins.content_object.price

    product_price.short_description = u"商品单价"
    product_price.allow_tags = True

    list_display = ("owner", "content_type", "product_name", "product_price", "amount", "object_id", "t_add")


class OrderAdmin(object):

    def product_name(self, ins):
        return ins.content_object.name

    product_name.short_description = u"商品名称"
    product_name.allow_tags = True

    def product_price(self, ins):
        return ins.content_object.price

    product_price.short_description = u"商品单价"
    product_price.allow_tags = True

    list_display = ("buyer", "status", "t_add", "t_wed", "content_type", "product_name", "product_price", "amount", "object_id", "progress")


xadmin.site.register(WedEssential, WedEssentialAdmin)
xadmin.site.register(WedScheme, WedSchemeAdmin)
xadmin.site.register(Order, OrderAdmin)

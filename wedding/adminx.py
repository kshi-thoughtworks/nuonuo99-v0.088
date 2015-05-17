#-*- coding:utf-8 -*-
import xadmin
from wedding.models import CartInfo


class CartInfoAdmin(object):

    def product_name(self, ins):
        return ins.content_object.name

    product_name.short_description = u"商品名称"
    product_name.allow_tags = True

    def product_price(self, ins):
        return ins.content_object.price

    product_price.short_description = u"商品单价"
    product_price.allow_tags = True

    list_display = ("buyer", "content_type", "product_name", "product_price", "amount", "object_id")


xadmin.site.register(CartInfo, CartInfoAdmin)

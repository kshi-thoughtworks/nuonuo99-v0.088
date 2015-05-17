#-*- coding:utf-8 -*-
import xadmin
from shop.models import CartInfo


class CartInfoAdmin(object):

    def product_name(self, ins):
        return ins.content_object.name

    list_display = ("buyer", "amount", "content_type", "product_name")


xadmin.site.register(CartInfo, CartInfoAdmin)

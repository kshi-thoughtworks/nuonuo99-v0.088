#-*- coding:utf-8 -*-
import xadmin
from shop.models import Cart


class CartInfo(object):
    list_display = ("buyer", "price")


xadmin.site.register(Cart, CartInfo)

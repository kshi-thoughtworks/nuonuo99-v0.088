#-*- coding:utf-8 -*-
import xadmin
from std_product.models import WedFlower, FlowerItem

def full_cols(*args):
    return ('name', 'price') + args + ('desc',)

class StdProductAdmin(object):
    pass


class WedFlowerAdmin(StdProductAdmin):
    list_display = full_cols('color', 'items')


class FlowerItemAdmin(object):
    list_display = ("product", "variety", "amount")


xadmin.site.register(FlowerItem, FlowerItemAdmin)
xadmin.site.register(WedFlower, WedFlowerAdmin)

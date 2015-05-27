#-*- coding:utf-8 -*-
import xadmin
from std_product.models import WedFlower, FlowerItem, FlowerScale

def full_cols(*args):
    return ('category', 'name', 'price') + args + ('desc',)


class StdProductAdmin(object):
    pass


class WedFlowerAdmin(StdProductAdmin):
    list_display = full_cols('style', 'color', 'items', 'scale')


class FlowerItemAdmin(object):
    list_display = ("product", "variety", "amount")


class FlowerScaleAdmin(object):
    list_display = ("product", "key", "value")


xadmin.site.register(WedFlower, WedFlowerAdmin)

xadmin.site.register(FlowerItem, FlowerItemAdmin)
xadmin.site.register(FlowerScale, FlowerScaleAdmin)

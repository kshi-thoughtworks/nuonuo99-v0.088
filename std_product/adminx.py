#-*- coding:utf-8 -*-
import xadmin
from std_product.models import WedFlower

def full_cols(*args):
    return ('name', 'price') + args + ('desc',)

class StdProductAdmin(object):
    pass


class WedFlowerAdmin(StdProductAdmin):
    list_display = full_cols('color', 'material')


xadmin.site.register(WedFlower, WedFlowerAdmin)

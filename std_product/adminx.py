#-*- coding:utf-8 -*-
import xadmin
from std_product.models import WedFlower, FlowerItem, FlowerScale, WedAv, StageEffect

def full_cols(*args):
    return ('category', 'name', 'price') + args + ('desc',)


def edit_cools(group1, group2):
    return group1 + ('name', 'price') + group2+ ('desc', 'photo1', 'photo2', 'photo3', 'photo4')


class StdProductAdmin(object):
    pass


class WedFlowerAdmin(StdProductAdmin):
    fields = edit_cools(
        ('category', 'style'),
        ('color',)
        )
 
    list_display = full_cols('style', 'color', 'items', 'scale')


class FlowerItemAdmin(object):
    list_display = ("product", "variety", "amount")


class FlowerScaleAdmin(object):
    list_display = ("product", "key", "value")


class WedAvAdmin(StdProductAdmin):
    fields = edit_cools(
        ('category', 'wed_env'),
        ('base_amount', 'unit', 'amount_step', 'float_price',
         'power', 'coverage')
        )
    list_display = full_cols('wed_env', 'power', 'base_amount', 'unit', 'amount_step', 'float_price')


class StageEffectAdmin(StdProductAdmin):
    fields = edit_cools(
        ('category', 'sub_category', 'wed_env'),
        ('base_amount', 'unit', 'amount_step', 'float_price')
        )
 
    list_display = full_cols('wed_env', 'sub_category', 'base_amount', 'unit', 'amount_step', 'float_price')


xadmin.site.register(WedAv, WedAvAdmin)
xadmin.site.register(StageEffect, StageEffectAdmin)
xadmin.site.register(WedFlower, WedFlowerAdmin)

xadmin.site.register(FlowerItem, FlowerItemAdmin)
xadmin.site.register(FlowerScale, FlowerScaleAdmin)

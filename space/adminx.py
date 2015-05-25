#-*- coding:utf-8 -*-
import xadmin
from space.models import Hotel, Banquet


class HotelAdmin(object):
    list_display = ('name', 'star', 'foodstyle', 'loc',
        'hall_num', 'lawn_num', 'min_price')


class BanquetAdmin(object):
    list_display = ('name', 'hotel', 'floor', 'column_num',
        'size', 'wed_sty', 'tel', 'loc', 'lbsinfo',
        'best_num', 'min_num', 'max_num', 'desc')


xadmin.site.register(Hotel, HotelAdmin)
xadmin.site.register(Banquet, BanquetAdmin)

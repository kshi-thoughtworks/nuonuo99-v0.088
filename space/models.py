#-*- coding:utf-8 -*-
from django.db import models
from base import settings
from location.models import Province,City,County
from base.choices import C_HOTEL_STAR


class Space(models.Model):
    """场地基本信息

    酒店宴会厅、教堂、户外
    """
    # basic info
    name = models.CharField(u'场地名称', max_length=100)
    size = models.IntegerField(u'场地面积(平方米)')
    wed_sty = models.CharField(u'专业', max_length=7)
    tel = models.CharField(u'联系电话', max_length=15)

    # location info
    loc = models.ForeignKey(County, verbose_name=u'归属地')
    lbsinfo = models.CharField(u'LBS 信息', max_length=100, null=True, blank=True)

    best_num = models.IntegerField(u'最佳容纳桌数')
    min_num = models.IntegerField(u'最小容纳桌数')
    max_num = models.IntegerField(u'最大容纳桌数')

    desc = models.TextField(u'场地描述', blank=True)

    pic_main = models.FileField(u'主图片', upload_to=settings.SPACE_PATH)
    pic_plane = models.FileField(u'场地平面图',  upload_to=settings.DEMO_PATH, null=True, blank=True)
    pic_1 = models.FileField(u'场地图片1', upload_to=settings.SPACE_PATH)
    pic_2 = models.FileField(u'场地图片2', upload_to=settings.SPACE_PATH, null=True, blank=True)
    pic_3 = models.FileField(u'场地图片3', upload_to=settings.SPACE_PATH, null=True, blank=True)
    pic_4 = models.FileField(u'场地图片4', upload_to=settings.SPACE_PATH, null=True, blank=True)
    pic_5 = models.FileField(u'场地图片5', upload_to=settings.SPACE_PATH, null=True, blank=True)
    pic_6 = models.FileField(u'场地图片6', upload_to=settings.SPACE_PATH, null=True, blank=True)
    pic_7 = models.FileField(u'场地图片7', upload_to=settings.SPACE_PATH, null=True, blank=True)
    pic_8 = models.FileField(u'场地图片8', upload_to=settings.SPACE_PATH, null=True, blank=True)
    pic_9 = models.FileField(u'场地图片9', upload_to=settings.SPACE_PATH, null=True, blank=True)
    pic_10 = models.FileField(u'场地图片10', upload_to=settings.SPACE_PATH, null=True, blank=True)

    class Meta:
        abstract=True

    def __unicode__(self):
        return '%s(%s)' % (self.name, self.tel)


class Hotel(models.Model):
    """酒店信息

    """

    name = models.CharField(u'场地名称', max_length=100)
    star = models.IntegerField(u'星级', choices=C_HOTEL_STAR.CHOICES)  # 酒店星级
    foodstyle = models.CharField(u'菜系描述', max_length=100)
    tel = models.CharField(u'联系电话', max_length=15)

    # location info
    loc = models.ForeignKey(County, verbose_name=u'归属地')
    lbsinfo = models.CharField(u'LBS 信息', max_length=100, null=True, blank=True)

    hall_num = models.IntegerField(u'宴会厅数量')
    lawn_num = models.IntegerField(u'草坪数量')

    min_price = models.PositiveIntegerField(u'最低婚宴价格')
    max_price = models.PositiveIntegerField(u'最高婚宴价格')

    pic_1 = models.FileField(u'场地图片1', upload_to=settings.SPACE_PATH)
    pic_2 = models.FileField(u'场地图片2', upload_to=settings.SPACE_PATH, null=True, blank=True)
    pic_3 = models.FileField(u'场地图片3', upload_to=settings.SPACE_PATH, null=True, blank=True)
    pic_4 = models.FileField(u'场地图片4', upload_to=settings.SPACE_PATH, null=True, blank=True)
    pic_5 = models.FileField(u'场地图片5', upload_to=settings.SPACE_PATH, null=True, blank=True)
    pic_6 = models.FileField(u'场地图片6', upload_to=settings.SPACE_PATH, null=True, blank=True)
    pic_7 = models.FileField(u'场地图片7', upload_to=settings.SPACE_PATH, null=True, blank=True)
    pic_8 = models.FileField(u'场地图片8', upload_to=settings.SPACE_PATH, null=True, blank=True)

    class Meta:
        verbose_name = u"酒店"
        verbose_name_plural =verbose_name

    def __unicode__(self):
        return '%s(%s)' % (self.name, self.tel)


class Banquet(Space):
    """宴会厅信息

    """
    hotel = models.ForeignKey(Hotel, verbose_name = u'所属酒店')
    floor = models.IntegerField(u'层高')
    column_num = models.IntegerField(u'立柱数量')

    class Meta:
        verbose_name = u"宴会厅"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return "%s-%s" % (self.hotel.name, self.name)

#coding:utf-8
__author__ = 'shikai'

class BaseChoices(object):
    CHOICES = ()

    @classmethod
    def get_value(cls, field):
        """ActiveChoices.get_value(0) >> 'ACTIVE'
        """
        for choice in cls.CHOICES:
            if choice[0] == field:
                return choice[1]
        return ""

    @classmethod
    def get_inner_value(cls, value):
        """ActiveChoices.get_value('ACTIVE') >> 0
        """
        for choice in cls.CHOICES:
            if choice[1] == value:
                return choice[0]
        return None



class C_GenderChoices(BaseChoices):
    MALE = 0
    FEMALE = 1
    UNKNOWN = 2

    CHOICES = (
        (MALE, "男"),
        (FEMALE, "女"),
    )

class C_ProductTypeChoices(BaseChoices):
    SIYI = 0 #司仪
    HUAYI = 1 #花艺
    CHANGDI = 2 #场地布置
    SHOOTING = 3 #摄像
    HOTEL = 4 #酒店
    PHOTOGRAPHER = 5 #摄影
    AV = 6 #灯光音响AV
    HUAZHUANG = 7 #化妆师

    CHOICES = (
        (SIYI, "司仪"),
        (HUAYI, "花艺"),
        (CHANGDI, "场布"),
        (SHOOTING, "摄像"),
        (HOTEL, "酒店"),
        (PHOTOGRAPHER, "摄影"),
        (AV, "AV工程"),
        (HUAZHUANG, "化妆师"),
    )


class C_WEDDINGSTYLE(BaseChoices):
    DEFAULT= -1#不限
    CHINESE = 0#中式
    WEST = 1#西式
    OUTDOOR = 2#户外

    CHOICES = (
        (DEFAULT,'不限'),
        (CHINESE, "中式"),
        (WEST, "西式"),
        (OUTDOOR, "户外"),
    )

class C_LANGUAGE(BaseChoices):
    PUTONG = 0#普通话
    GUANGDONG = 1#广东话
    ENGLISH = 2#英语
    OTHERS = 3#其他方言

    CHOICES = (
        (PUTONG, "普通话"),
        (GUANGDONG, "广东话"),
        (ENGLISH, "英语"),
        (OTHERS, "其他方言"),
    )



class C_ORDER_STATUS(BaseChoices):
    NOPAY = 0 #未付款
    PAYED = 1 #已付款
    CHECKING = 2 #订单正在确认
    PROCESSING = 3 #正在准备中
    WEDDING = 4 #婚礼执行中
    COMPLETED = 5 #执行完毕
    COMMENTING = 6 #评价期


    CHOICES = (
        (NOPAY, "未付款"),
        (PAYED, "已付款"),
        (CHECKING, "已付款确认中"),
        (PROCESSING, "备货准备中"),
        (WEDDING, "婚礼执行中"),
        (COMPLETED, "执行完毕"),
        (COMMENTING, "评价期"),
    )


class C_FLOWER_STYLE_DOOR(BaseChoices):
    ALL = 0 #全花门
    HALF = 1 #半花门
    THREEPOINT = 2 #三点式
    FIVEPOINT = 3 #五点式
    OTHERS = 4 #其他异形

    CHOICES = (
        (ALL, "全花门"),
        (HALF, "半花门"),
        (THREEPOINT, "三点式"),
        (FIVEPOINT, "五点式"),
        (OTHERS, "异形"),

    )

class C_FLOWER_STYLE_DOOR(BaseChoices):
    GLOBAL = 0 #球形
    RADIO = 1 #放射形
    OTHERS = 2 #异形

    CHOICES = (
        (GLOBAL, "球形"),
        (RADIO, "放射形"),
        (OTHERS, "异形"),
    )


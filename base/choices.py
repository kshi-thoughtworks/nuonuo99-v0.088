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


class C_ProductTypeChoices(BaseChoices):
    SIYI = 0  # 司仪
    HUAZHUANG = 1  # 化妆师
    PHOTOGRAPHER = 2  # 摄影
    SHOOTING = 3  # 摄像
    HUAYI = 4  # 花艺
    CHANGDI = 5  # 场地布置
    HOTEL = 6  # 酒店
    AV = 7  # 灯光音响AV
    CAR = 8  # 婚车


    CHOICES = (
        (SIYI, "司仪"),
        (HUAYI, "花艺"),
        (CHANGDI, "场布"),
        (SHOOTING, "摄像"),
        (HOTEL, "酒店"),
        (PHOTOGRAPHER, "摄影"),
        (AV, "AV工程"),
        (HUAZHUANG, "化妆师"),
        (CAR, '婚车'),
    )


class C_LANGUAGE(BaseChoices):
    PUTONG = 0  # 普通话
    GUANGDONG = 1  # 广东话
    ENGLISH = 2  # 英语
    OTHERS = 3  # 其他方言

    CHOICES = (
        (PUTONG, "普通话"),
        (GUANGDONG, "广东话"),
        (ENGLISH, "英语"),
        (OTHERS, "其他方言"),
    )


class C_ORDER_STATUS(BaseChoices):
    NOPAY = 0 # 未付款
    PAYED = 1 # 已付款
    CHECKING = 2 # 订单正在确认
    PROCESSING = 3  # 正在准备中
    WEDDING = 4  # 婚礼执行中
    COMPLETED = 5  # 执行完毕
    COMMENTING = 6  # 评价期

    CHOICES = (
        (NOPAY, "未付款"),
        (PAYED, "已付款"),
        (CHECKING, "已付款确认中"),
        (PROCESSING, "备货准备中"),
        (WEDDING, "婚礼执行中"),
        (COMPLETED, "执行完毕"),
        (COMMENTING, "评价期"),
    )


class C_FLOWER_CATEGORY(BaseChoices):
    CHOICES = (
        ("door", "花门"),
        ("road", "路引"),
        ("desk", "桌花"),
        ("other", "其他"),
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


class C_FLOWER_STYLE_OTHERS(BaseChoices):
    GLOBAL = 0 #球形
    RADIO = 1 #放射形
    OTHERS = 2 #异形

    CHOICES = (
        (GLOBAL, "球形"),
        (RADIO, "放射形"),
        (OTHERS, "异形"),
    )


class C_CAMERA_STYLE(BaseChoices):
    ALL = 0 #全类型
    FULL = 1 #全画幅
    HALF = 2 #非全画幅

    CHOICES = (
        (ALL, "全类型"),
        (FULL, "全画幅"),
        (HALF, "非全画幅"),
    )


class C_CAMERA_BRAND(BaseChoices):
    ALL = 0 #全类型
    CANON = 1 #佳能
    NIKON = 2 #尼康

    CHOICES = (
        (ALL, "全类型"),
        (CANON, "佳能"),
        (NIKON, "尼康"),
    )


class C_VIDEO_DEVICE_TYPE(BaseChoices):
    ALL = 0 #全类型
    CAMERA = 1 #照相机
    VIDEO = 2 #摄像机

    CHOICES = (
        (ALL, "全类型"),
        (CAMERA, "照相机"),
        (VIDEO, "摄像机"),
    )

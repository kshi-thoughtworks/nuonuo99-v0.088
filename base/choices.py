#-*- coding:utf-8 -*-
from location.models import Province


def int_choice(values, start=1):
    return [(i, v) for i, v in zip(range(start, start+len(values)), values)]


def bool_choice(values):
    return (
            (0, values[0]),
            (1, values[1]),
            )

_c_wed_sty = (u'中式', u'西式')
C_WED_STY = int_choice(_c_wed_sty)

_c_lang = (u"普通话", u"广东话", u"英语", u"其他方言")
C_LANG = int_choice(_c_lang)

_gender = (u'男', u'女')

_age = (
    ('60-69', '60 后'),
    ('70-79', '70 后'),
    ('80-89', '80 后'),
    ('90-99', '90 后'),
    )

_height = (
    ('-170', '170 以下'),
    ('170-175', '170-175'),
    ('175-', '175以上'),
    )

_skill = (
    ('has', '有'),
    ('null', '无'),
    )

_mc_price = (
    ('-2000', '2000 以下'),
    ('2000-4000', '2000-4000'),
    ('4000-', '4000 以上'),

        )


def MC_PARAS():
    return [
    {
        'name': 'price',
        'disp_name': u'价格',
        'values': _mc_price,
    },
    {
        'name': 'wed_sty',
        'disp_name': u'专业',
        'values': C_WED_STY,
    },
    {
        'name': 'is_man',
        'disp_name': u'性别',
        'values': bool_choice(_gender),
    },
    {
        'name': 'age',
        'disp_name': u'年龄',
        'values': _age,
    },
    {
        'name': 'height',
        'disp_name': u'身高',
        'values': _height,
    },
    {
        'name': 'skill',
        'disp_name': u'才艺',
        'values': _skill,
    },
    {
        'name': 'native_loc',
        'disp_name': u'籍贯',
        'values': [(item.pk, item.name) for item in Province.objects.all()],
    },
    ]


# -------------------------------------------------

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


class C_HOTEL_STAR(BaseChoices):  # 酒店星级
    NONE = 0 # 普通酒店
    ECNOMIC = 1  # 经济型酒店
    THREESTAR = 3  # 三星
    FOURSTAR = 4  # 四星
    FIVESTAR = 5  # 五星
    LAX = 7  # 超豪华

    CHOICES = (
        (NONE, '普通酒店'),
        (ECNOMIC, '经济型酒店'),
        (THREESTAR, '三星'),
        (FOURSTAR, '四星'),
        (FIVESTAR, '五星'),
        (LAX, '超豪华'),
    )

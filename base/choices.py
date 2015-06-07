#-*- coding:utf-8 -*-
from location.models import Province


C_PRODUCT_TYPE = (
    ('flower', u'花艺'),
    ('av', u'AV 工程'),
    ('stage', u'舞台效果'),
    )


def range_action(name):
    def action(queryset, value):
        if not value:
            return queryset

        kwargs = dict()
        bottom, top = value.split('~')
        if bottom:
            kwargs['%s__gte' % name] = bottom
        if top:
            kwargs['%s__lte' % name] = top
        return queryset.filter(**kwargs)
    return action


def int_choice(values, start=1):
    return [(i, v) for i, v in zip(range(start, start+len(values)), values)]


def bool_choice(values):
    return (
            ('True', values[0]),
            ('False', values[1]),
            )

_c_wed_sty = (u'中式', u'西式')
C_WED_STY = int_choice(_c_wed_sty)

_c_lang = (u"普通话", u"广东话", u"英语", u"其他方言")
C_LANG = int_choice(_c_lang)

_gender = (u'男', u'女')

_age = (
    ('1960-1-1~1969-12-31', '60 后'),
    ('1970-1-1~1979-12-31', '70 后'),
    ('1980-1-1~1989-12-31', '80 后'),
    ('1990-1-1~1999-12-31', '90 后'),
    )

_height = (
    ('~170', '170 以下'),
    ('170~175', '170~175'),
    ('175~', '175以上'),
    )

_skill = ('无', '有')

_mc_price = (
    ('~2000', '2000 以下'),
    ('2000~4000', '2000~4000'),
    ('4000~', '4000 以上'),
    )


_c_makeup_sty = (u'韩系', u'日系')
C_MAKEUP_STY = int_choice(_c_makeup_sty)


_makeup_price = (
    ('~2000', '2000 以下'),
    ('2000~4000', '2000~4000'),
    ('4000~', '4000 以上'),
    )


def mc_paras():
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
        'name': 'mc_tech',
        'disp_name': u'才艺',
        'values': bool_choice(_skill),
    },
    {
        'name': 'loc_native',
        'disp_name': u'籍贯',
        'values': [(item.pk, item.name) for item in Province.objects.all()],
    },
    ]


def makeup_paras():
    return [
    {
        'name': 'price',
        'disp_name': u'价格',
        'values': _makeup_price,
    },
    {
        'name': 'wed_sty',
        'disp_name': u'专业',
        'values': C_WED_STY,
    },
    {
        'name': 'makeup_sty',
        'disp_name': u'化妆风格',
        'values': C_MAKEUP_STY,
    },
    ]


def photographer_paras():
    return [
    {
        'name': 'price',
        'disp_name': u'价格',
        'values': _mc_price,
    },
    {
        'name': 'is_full_frame',
        'disp_name': u'画幅',
        'values': bool_choice([u'全画幅', u'半画幅']),
    },
    {
        'name': 'no_teamwork',
        'disp_name': u'不与他人合作',
        'values': bool_choice([u'是', u'否']),
    },
    ]


def vedioguys_paras():
    return [
    {
        'name': 'price',
        'disp_name': u'价格',
        'values': _mc_price,
    },
    {
        'name': 'use_camera',
        'disp_name': u'器材',
        'values': bool_choice([u'照相机', u'摄像机']),
    },
    ]


# ----------------------------------------------

_flower_cate = (u'花门', u'路引', u'桌花', u'手捧花', u'合影区', u'司仪台', u'车花', u'签到台', u'香槟塔', u'迎宾水牌', u'烛台桌花', u'背景花艺', u'碎花', u'胸花')
C_FLOWER_CATE = int_choice(_flower_cate, start=1)

def get_disp_flower_cate(cate):
    return u'花艺-%s' % _flower_cate[int(cate)-1]

C_FLOWER_STYLE = (
    (1, u'全花门'),
    (2, u'半花门'),
    (3, u'三点式'),
    (4, u'五点式'),
    (5, u'异形'),
    (6, u'球形'),
    (7, u'放射形'),
    (8, u'花球'),
    (9, u'花环'),
    )

_cate_style = {
    '1': (  # 花门
        (1, u'全花门'),
        (2, u'半花门'),
        (3, u'三点式'),
        (4, u'五点式'),
        (5, u'异形'),
        ),
    '2': (  # 路引
        (6, u'球形'),
        (7, u'放射形'),
        (5, u'异形'),
        ),
    '3': (  # 桌花
        (6, u'球形'),
        (7, u'放射形'),
        (5, u'异形'),
        ),
    'other': (  # 其他
        (8, u'花球'),
        (9, u'花环'),
        (5, u'异形'),
        ),
    }


def flower_paras(cate):
    return [
    {
        'name': 'price',
        'disp_name': u'价格',
        'values': _mc_price,
    },
    {
        'name': 'style',
        'disp_name': u'花艺样式',
        'values': _cate_style.get(cate, _cate_style['other']),
    },
    ]


_av_cate = (u'灯光', u'音响', u'LED大屏')
C_AV_CATE = int_choice(_av_cate, start=1)

def get_disp_av_cate(cate):
    return u'AV-%s' % _av_cate[int(cate)-1]

_wed_env = (u'室内', u'室外')
C_WED_ENV = int_choice(_wed_env)


def av_paras(cate):
    paras = [
        {
            'name': 'price',
            'disp_name': u'价格',
            'values': _mc_price,
        },
        ]
    if cate == '2':  # 音响
        paras.append(
            {
                'name': 'wed_env',
                'disp_name': u'使用场地',
                'values': C_WED_ENV,
            },
            )
    return paras

_stage_cate = (u'舞台背景', u'投影仪', u'地毯', u'T 台', u'烛台', u'香槟台', u'干冰机', u'磁悬浮幕布')
C_STAGE_CATE = int_choice(_stage_cate)

def get_disp_stage_cate(cate):
    return u'舞台效果-%s' % _stage_cate[int(cate)-1]


C_STAGE_SUB_CATE = (
    # 舞台背景
    (1, u'舞台背景-宝丽布喷绘'),
    (2, u'舞台背景-纱幔'),
    (3, u'舞台背景-景片制作'),
    # 投影仪
    (4, u'投影仪-120 寸'),
    (5, u'投影仪-150 寸'),
    # 地毯
    (6, u'地毯-镜面地毯'),
    (7, u'地毯-白地毯'),
    (8, u'地毯-红地毯'),
    (9, u'地毯-长毛地毯'),
    )

_stage_sub_cate = {
    '1': (
        (1, u'宝丽布喷绘'),
        (2, u'纱幔'),
        (3, u'景片制作'),
        ),
    '2': (
        (4, u'120 寸'),
        (5, u'150 寸'),
        ),
    '3': (
        (6, u'镜面地毯'),
        (7, u'白地毯'),
        (8, u'红地毯'),
        (9, u'长毛地毯'),
        ),
    }


def stage_paras(cate):
    paras = [
        {
            'name': 'price',
            'disp_name': u'价格',
            'values': _mc_price,
        },
        ]
    if cate in _stage_sub_cate:
        paras.append(
            {
                'name': 'sub_category',
                'disp_name': u'种类',
                'values': _stage_sub_cate[cate],
            }
            )
    return paras


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

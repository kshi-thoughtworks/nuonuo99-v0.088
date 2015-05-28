#-*- coding:utf-8 -*-


def price_filter(query_set):
    kwargs = dict()
    p_min, p_max = query_set.get('price', '-').split('-')

    if p_min:
        kwargs['price__gte'] = p_min

    if p_max:
        kwargs['price__lte'] = p_max

    return kwargs


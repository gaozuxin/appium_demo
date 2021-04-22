# coding=utf-8
import time


def date_time_chinese():
    return time.strftime("%Y{y}%m{m}%d{d} %H{h}%M{f}%S{s}", time.localtime()).format(y='年', m='月', d='日',
                                                                                     h='时', f='分', s='秒')


def date_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def date_time_log():
    return time.strftime("%Y-%m-%d", time.localtime())

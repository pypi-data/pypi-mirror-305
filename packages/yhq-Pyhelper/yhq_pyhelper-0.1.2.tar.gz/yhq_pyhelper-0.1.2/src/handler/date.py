#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : HuiQing Yu
# @Date   : 2024/10/30
# @Description:
import datetime


def datetime_str(fmt: str='%Y-%m-%d %H:%M:%S'):
    """
    格式化日期
    :param fmt:
        %Y：四位数的年份;
        %m：月份（01-12;
        %d：月份中的天数（01-31）。
        %H：小时（24小时制，00-23）。
        %M：分钟（00-59）。
        %S：秒（00-59）
        除了上述常用的格式选项外，strftime 还支持许多其他的格式选项。例如：
        %y：两位数的年份。
        %b：月份的缩写形式。
        %B：月份的全称。
        %a：星期的缩写形式。
        %A：星期的全称。
        %p：AM 或 PM。
        %I：小时（12小时制，01-12）
    :return:
    """
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime(fmt)
    return formatted_datetime

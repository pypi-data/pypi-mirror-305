#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : HuiQing Yu
# @Date   : 2024/5/24
# @Description:
import logging
from decimal import Decimal, ROUND_HALF_UP, ROUND_DOWN, ROUND_UP

logger = logging.getLogger()


class PercentHandler:

    def __init__(self, num, p):
        if not isinstance(num, Decimal) or not isinstance(p, int):
            raise TypeError("num must be Decimal And p must be int")
        self.num = num
        self.p = p

    def round_none(self):
        """
        不处理精度
        """
        return self.num

    def round_half_up(self):
        """
        四舍五入
        :return:
        """
        return self.num.quantize(Decimal('0.' + '0' * self.p), rounding=ROUND_HALF_UP)

    def round_down(self):
        """
        舍去：指定精度位数后面的都舍去
        :return:
        """

        return self.num.quantize(Decimal('0.' + '0' * self.p), rounding=ROUND_DOWN)

    def round_up(self):
        """
        进位：指定精度位数后面的直接进位
        :return:
        """
        return self.num.quantize(Decimal('0.' + '0' * self.p), rounding=ROUND_UP)


def call_round(num, method_name, p: int = 2):
    """

    :param num: 要计算的数
    :param method_name: 精度方法
    :param p: 精度值
    :return:
    """
    # 检查确保 method_name 是字符串类型
    if method_name not in ['round_none', 'round_half_up', 'round_down', 'round_up']:
        raise ValueError("method_name must be in ('round_none', 'round_half_up', 'round_down', 'round_up')")
    if not isinstance(num, Decimal):
        num = Decimal(str(num))
    # 获取方法
    method_to_call = getattr(PercentHandler(num, p), method_name, None)

    # 检查确保获取到了有效的方法
    if callable(method_to_call):
        return method_to_call()
    else:
        logger.error(f"Method {method_name} does not exist or is not callable.")

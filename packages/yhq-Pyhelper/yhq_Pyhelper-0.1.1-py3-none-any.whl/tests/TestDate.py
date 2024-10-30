#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : HuiQing Yu
# @Date   : 2024/10/30
# @Description:
# test_calculator.py
import unittest

from src.handler.date import datetime_str


class TestDate(unittest.TestCase):

    def test_dt_str(self):
        self.assertIsNotNone(datetime_str())

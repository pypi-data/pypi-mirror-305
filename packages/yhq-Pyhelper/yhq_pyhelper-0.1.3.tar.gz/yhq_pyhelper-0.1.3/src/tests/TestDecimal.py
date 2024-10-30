#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : HuiQing Yu
# @Date   : 2024/10/30
# @Description:

import unittest
from decimal import Decimal

from src.yhq_pyhelper.decimalUtils import call_round


class TestDecimal(unittest.TestCase):

    def test_call_round(self):
        self.assertEqual(call_round(1.23456, 'round_none'), Decimal('1.23456'))
        self.assertEqual(call_round(1.23456, 'round_half_up'), Decimal('1.23'))
        self.assertEqual(call_round(1.23656, 'round_half_up'), Decimal('1.24'))
        self.assertEqual(call_round(1.23356, 'round_up'), Decimal('1.24'))
        self.assertEqual(call_round(1.23656, 'round_down'), Decimal('1.23'))
        self.assertRaises(ValueError, call_round, 1.23456, 'round__up')

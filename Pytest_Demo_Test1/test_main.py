# -*- coding: utf-8 -*-
# @File   : test_samelp
# @Time   : 2021/4/8 20:22 
# @Author : BLUE_JUZIUPUP
import pytest

from .Open_Test_Case import add_list,sub_list,add_value,sub_value


class Testone:
    def setup_class(self):
        print("开始运行")
    def teardown_class(self):
        print("结束运行")

    def setup(self):
        print("开始计算了")

    def teardown(self):
        print("结束计算了")

    @pytest.mark.parametrize('a,b,expect', argvalues = add_list() , ids = add_value())
    def test_add(self, a, b, expect):
        assert expect == a + b

    @pytest.mark.parametrize('a,b,expect', argvalues = sub_list() , ids = sub_value())
    def test_sub(self, a, b, expect):
        assert expect == a - b



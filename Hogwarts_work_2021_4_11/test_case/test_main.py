# -*- coding: utf-8 -*-
# @File   : test_samelp
# @Time   : 2021/4/8 20:22 
# @Author : BLUE_JUZIUPUP

import pytest
import allure

#from Hogwarts_work_2021_4_11.test_data.test_data_list import add_list,sub_list,add_value,sub_value

@pytest.fixture(scope="module")
def module_setup():
    print("开始运行")
    yield
    print("结束运行")

@pytest.fixture()
def function_setup():
    print("开始计算了")
    yield
    print("结束计算了")

#加法
@allure.feature("参数化数据运算")
class Testadd:

    @allure.story("加法")
    @pytest.mark.run(order=1)
    def test_add(module_setup,function_setup,add_list):
        try:
            assert add_list[2] == add_list[0] + add_list[1]
            print(f"{add_list[0]} + {add_list[1]} = {add_list[2]}")
        except :
            print("用例执行错误")


    #减法
    @allure.story("减法")
    @pytest.mark.run(order=2)
    def test_sub(module_setup,function_setup,sub_list):
        try:
            assert sub_list[2] == sub_list[0] - sub_list[1]
            print(f"{sub_list[0]} - {sub_list[1]} = {sub_list[2]}")
        except :
            print("用例执行错误")


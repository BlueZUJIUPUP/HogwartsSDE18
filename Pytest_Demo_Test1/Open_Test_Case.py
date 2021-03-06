# -*- coding: utf-8 -*-
# @File   : Open_Test
# @Time   : 2021/4/8 22:08 
# @Author : BLUE_JUZIUPUP
import yaml

import os

path = os.path.dirname(__file__)

#读取yaml文件的用例集
def open_test():
    with open(f'{path}/test_case.yaml',encoding="utf-8") as f:
        a = yaml.load(f)
        add = a['add_test']
        sub = a['sub_test']
        return add,sub


#输出加法用例的值
def add_list():
    test_case = open_test()[0]
    test_add_list=[]
    for k in test_case:
        test_add_list.append(test_case[k])
    return test_add_list


#输出减法用例的值
def sub_list():
    test_case = open_test()[1]
    test_sub_list = []
    for k in test_case:
        test_sub_list.append(test_case[k])
    return test_sub_list


#输出加法用例名
def add_value():
    test_case = open_test()[0]
    add_value = list(test_case)
    return add_value


#输出减法用例名
def sub_value():
    test_case = open_test()[1]
    sub_value = list(test_case)
    return sub_value



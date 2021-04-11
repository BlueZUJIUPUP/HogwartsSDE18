# -*- coding: utf-8 -*-
# @File   : Open_Test
# @Time   : 2021/4/11 22:08
# @Author : BLUE_JUZIUPUP
import os

import pytest
import allure

def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")



if __name__ == '__main__':
    pytest.main(['-vs','-q','--alluredir','./report/result'])
    os.system("allure generate ./report/result/ -o ./report/html --clean")
    os.system("allure serve ./report/result/ -o ./report/html --clean")
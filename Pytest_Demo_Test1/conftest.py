# -*- coding: utf-8 -*-
# @File   : Open_Test
# @Time   : 2021/4/11 22:08
# @Author : BLUE_JUZIUPUP
import logging

import pytest
import requests

from Work_Wechat_GUI_App.page.App import App
from Work_Wechat_GUI_App.page.BasePage import BasePage
logging.basicConfig(level=logging.INFO)


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
        print('用例名：', item.name)
        print('用例节点：', item.nodeid)
        data = {'nodeID': item.nodeid, 'remark': '自动化添加'}
        r = requests.post("http://127.0.0.1:5000/testcase", json=data)
        print(r.text)



# @pytest.fixture(scope="session")
# def get_init():
#     logging.info("开始测试_class")
#     app = App().start()
#     yield app
#     app.stop()
#
# @pytest.fixture(scope="function")
# def run_case():
#     logging.info("开始测试_func")
#     yield
#     logging.info("结束测试_func")



# -*- coding: utf-8 -*-
# @Time    : 2021/5/23 11:14
# @Author  : BLUE_JUZIUPUP
# @Email   : z1003033614@163.com
# @File    : conftest.py
# @Software: PyCharm
import logging

import pytest

from wechat_api_test_2021_05_21.WeWorkApi.Base import Base


@pytest.fixture(scope="class")
def get_init():
    logging.info("************开始测试*************")
    wework = Base()
    access_token = wework.get_access_token()
    yield access_token
    logging.info("************结束测试*************")


# -*- coding: utf-8 -*-
# @File   : test_API_case
# @Time   : 2021/5/22 20:10 
# @Author : BLUE_JUZIUPUP
import json

import requests

from wechat_api_test_2021_05_21.WeWork import WeWork


class TestWework:
    def setup_class(self):
        self.wework = WeWork()
        self.wework.get_access_token()

    def test_search(self):
        r = self.wework.search()
        r.json()
        assert r.json()["errcode"] == 0

    def test_add_tag(self):
        r = self.wework.add_tag()
        assert r.json()["errcode"] == 0
        self.test_search()

    def test_del_tag(self):
        r = self.wework.del_tag()
        assert r.json()["errcode"] == 0
        self.test_search()

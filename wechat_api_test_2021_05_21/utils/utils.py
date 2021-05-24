# -*- coding: utf-8 -*-
# @Time    : 2021/5/23 0:34
# @Author  : BLUE_JUZIUPUP
# @Email   : z1003033614@163.com
# @File    : utils.py
# @Software: PyCharm
import json

from wechat_api_test_2021_05_21.WeWorkApi.tag_API import Tag_Api


class Utils(Tag_Api):
    def select(self,name1,name2,f = None):
        select = self.search()
        data = json.dumps(select.json(), indent=2, ensure_ascii=False)
        if f == "in":
            assert name1 in data and name2 in data
        else:
            assert name1 not in data and name2 not in data

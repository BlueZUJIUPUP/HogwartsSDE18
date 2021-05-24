# -*- coding: utf-8 -*-
# @Time    : 2021/5/23 10:47
# @Author  : BLUE_JUZIUPUP
# @Email   : z1003033614@163.com
# @File    : User_API.py
# @Software: PyCharm
import requests

from wechat_api_test_2021_05_21.WeWorkApi.Base import Base
from wechat_api_test_2021_05_21.WeWorkApi.WorkApi import WeWork


class User_API(WeWork):
    def create_User(self, userid, name, mobile, department, email, **kwargs):
        if "json" in kwargs:
            json = kwargs["json"]
        else:
            json = {
                "userid": userid,
                "name": name,
                "alias": "jackzhang",
                "mobile": mobile,
                "department": department,
                "order": [10, 40],
                "email": email,
            }
        data = {
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/user/create',
            'method': "post",
            'params': {
                "access_token": self.access_token
            },
            'json': json
        }
        r = self.request(data)
        return r

    def del_User(self, userid):
        data = {"url": "https://qyapi.weixin.qq.com/cgi-bin/user/delete",
                'method': "post",
                "params" : {"access_token": self.access_token,
                            "userid": userid
                            }
                }
        r = self.request(data)
        return r

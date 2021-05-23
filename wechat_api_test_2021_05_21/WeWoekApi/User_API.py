# -*- coding: utf-8 -*-
# @Time    : 2021/5/23 10:47
# @Author  : BLUE_JUZIUPUP
# @Email   : z1003033614@163.com
# @File    : User_API.py
# @Software: PyCharm
import requests

from wechat_api_test_2021_05_21.WeWoekApi.Base import Base


class User_API(Base):
    def create_User(self,userid,name,mobile,department,email):
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create",
                          params ={"access_token":self.access_token},
                          json = {
                                    "userid": userid,
                                    "name": name,
                                     "alias": "jackzhang",
                                    "mobile": mobile,
                                    "department": department,
                                      "order": [10, 40],
                                      "position": "产品经理",
                                      "gender": "1",
                                    "email": email,
                                    "telephone": "020-123456",
                                    "main_department": 1
                                })
        return r
    def del_User(self,userid):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/delete",
                          params =({"access_token":self.access_token,
                                    "userid" : userid
                                   }))
        print(r.json())
        return r

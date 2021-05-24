# -*- coding: utf-8 -*-
# @Time    : 2021/5/23 11:50
# @Author  : BLUE_JUZIUPUP
# @Email   : z1003033614@163.com
# @File    : department_API.py
# @Software: PyCharm
import requests

from wechat_api_test_2021_05_21.WeWorkApi.WorkApi import WeWork


class department_API(WeWork):


    def get_department(self):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/department/list",params ={"access_token":self.access_token})
        print(r.json())
        return r

    def del_department(self,id):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/department/delete",
                         params=({"access_token": self.access_token,
                                  "id" : id
                                  }))
        print(r.json())
        return r

    def get_department_uesr(self):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/simplelist",
                         params =({"access_token":self.access_token,
                                  "department_id" : 2
                                  }))
        print(r.json())
        return r

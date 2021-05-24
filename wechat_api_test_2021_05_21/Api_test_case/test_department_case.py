# -*- coding: utf-8 -*-
# @Time    : 2021/5/23 13:22
# @Author  : BLUE_JUZIUPUP
# @Email   : z1003033614@163.com
# @File    : test_department_case.py
# @Software: PyCharm
import json

from faker import Faker

from wechat_api_test_2021_05_21.WeWorkApi.department_API import department_API



class Testdepartment():
    def setup_class(self):
        self.fake = Faker(locale='zh_CN')
        self.department = department_API()
        self.access_token = self.department.get_access_token()

    def test_del_department(self):
        del_department_id = self.department.get_department().json()['department'][-1]['id']
        print(del_department_id)
        print(type(del_department_id))
        e = self.department.del_department(del_department_id)
        assert e.json()["errcode"] == 0
        assert del_department_id not in json.dump(self.department.get_department().json(), indent=2, ensure_ascii=False)
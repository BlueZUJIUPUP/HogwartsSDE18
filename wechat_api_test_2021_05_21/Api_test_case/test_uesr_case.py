# -*- coding: utf-8 -*-
# @Time    : 2021/5/23 11:12
# @Author  : BLUE_JUZIUPUP
# @Email   : z1003033614@163.com
# @File    : test_uesr_case.py
# @Software: PyCharm
import json

from faker import Faker

from wechat_api_test_2021_05_21.WeWorkApi.User_API import User_API
from wechat_api_test_2021_05_21.WeWorkApi.department_API import department_API


class TestWework:
    def setup_class(self):
        self.fake = Faker(locale='zh_CN')
        self.wework = User_API()
        self.access_token = self.wework.get_access_token()
        self.department = department_API()
        self.access_token = self.department.get_access_token()


    def test_Adduesr(self):
        userid = self.fake.user_name()
        name = self.fake.name()
        mobile = "+86 "+ self.fake.phone_number()
        department =[self.department.get_department().json()['department'][0]['id']]
        email = self.fake.ascii_company_email()
        print(f"userid:{userid},name:{name},mobile:{mobile},department:{department},email:{email}")
        e = self.wework.create_User(userid,name,mobile,department,email)
        print(e.json())
        assert e.json()["errcode"] == 0
    def test_delUser(self):
        print(self.department.get_department().json())
        userid = self.department.get_department_uesr().json()["userlist"][0]["userid"]
        print(userid)
        a = self.wework.del_User(userid)
        assert a.json()["errcode"] == 0
        assert userid not in json.dumps(self.department.get_department_uesr().json(), indent=2, ensure_ascii=False)


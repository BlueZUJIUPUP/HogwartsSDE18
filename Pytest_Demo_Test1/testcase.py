# -*- coding: utf-8 -*-
# @File   : testcase
# @Time   : 2021/7/12 15:35 
# @Author : BLUE_JUZIUPUP
import requests

class Test_one:
    def test_01(self):
        headers = {"Content-Type": "application/json"}
        data = {"email": "1003033614@qq.com",
                "password": "zyy123",
                "userName": "zyy1233"}
        r = requests.post("http://stuq.ceshiren.com:8089/user/register", json=data, headers=headers)
        print(r.text)

    def test_02(self):
        headers = {"Content-Type": "application/json"}
        data = {"password": "zyy123",
                "userName": "zyy1233"}
        r = requests.post("http://stuq.ceshiren.com:8089/user/login", json=data, headers=headers)
        print(r.text)

    def test_03(self):
        headers = {
            "Content-Type": "application/json",
            "token":"f762e83f8662e7985aa5cb557a2dd026"
            }
        data = {}
        r = requests.get("http://stuq.ceshiren.com:8089/user/isLogin", headers=headers)
        print(r.text)


    def test_04(self):
        headers = {
            "Content-Type": "application/json",
            # "token": "f762e83f8662e7985aa5cb557a2dd026"
        }
        data = {"activityShopId": "15676785713",
                "password": "123456",
                'name':'Eidolon'}
        r = requests.get('http://api-test.baojun.net/base/activity/apply/record/save',params=data,headers=headers)
        print(r.text)

    def test_05(self):
        headers = {
            "Content-Type": "application/json",
            # "token": "f762e83f8662e7985aa5cb557a2dd026"
        }
        data = {"pageNo": "10",
                "pageSize": '10'}
        r = requests.get('https://api-test.baojun.net/base/activity/shop/all/list',params=data,headers=headers)
        print(r.text)


# -*- coding: utf-8 -*-
# @File   : testcase
# @Time   : 2021/7/12 15:35 
# @Author : BLUE_JUZIUPUP
import requests


class Testcase:
    def setup_class(self):
        self.url = "http://127.0.0.1:5000/testcase"

    def test_get(self):
        r = requests.get(url=self.url)
        print(r.text)
        assert r.status_code == 200

    def test_get2(self):
        data = {"id": 4}
        r = requests.get(url=self.url, params=data)
        print(r.text)
        assert r.status_code == 200

    def test_post(self):
        data = {"id": 98, 'nodeID': 'nmslwsnd', 'remark': 'nmml'}
        r = requests.post(url=self.url, json=data)
        assert r.status_code == 200

    def test_put(self):
        r = requests.put(url=self.url)
        assert r.status_code == 200
        print(r.text)

    def test_put2(self):
        data = {
            'oldData':{
                "id": '213',
            },
            'newData':{
                "id":66,
                'nodeID': '221',
                'remark': '1'
            }
        }
        r = requests.put(url=self.url, json=data)
        assert r.status_code == 200
        print(r.text)

    def test_delete(self):
        data = {"id": 4}
        r = requests.delete(url=self.url, params=data)
        print(r.text)

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


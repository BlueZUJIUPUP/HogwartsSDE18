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
        data = {'nodeID': 'nmslwsnd', 'remark': 'nmml'}
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











# -*- coding: utf-8 -*-
# @File   : task
# @Time   : 2021/8/2 10:09 
# @Author : BLUE_JUZIUPUP
import requests


class Testcase:
    def setup_class(self):
        self.url = "http://127.0.0.1:5000/task"

    def test_get(self):
        r = requests.get(url=self.url)
        print(r.text)
        assert r.status_code == 200

    # def test_get2(self):
    #     data = {"id": 4}
    #     r = requests.get(url=self.url, params=data)
    #     print(r.text)
    #     assert r.status_code == 200

    def test_post(self):
        # data = {"id": 98, 'nodeID': 'nmslwsnd', 'remark': 'nmml'}
        data = {'remark': 'test_main.py'}
        r = requests.post(url=self.url,json=data)
        print(r.text)
        assert r.status_code == 200

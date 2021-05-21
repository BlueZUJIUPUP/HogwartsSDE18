# -*- coding: utf-8 -*-
# @File   : test_weWorkApi
# @Time   : 2021/5/21 10:18 
# @Author : BLUE_JUZIUPUP
import json

import requests


class TestWework:
    def setup_class(self):
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken',
                         params=({
                             "corpid": "wwf443a769ec9a969f",
                             "corpsecret": "vMWlkH8N-37OO4rm8qMk-279RjECOsogSin_I9kE-AA"}))
        assert r.json()["errcode"] == 0
        print(r.json()["access_token"])
        self.access_token = r.json()["access_token"]

    def test_search(self):
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
                          params ={"access_token":self.access_token},
                          json = {})
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        assert r.json()["errcode"] == 0

    def test_add_tag(self):
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
                          params ={"access_token":self.access_token},
                          json = {
                                    "group_name": "nmsl3",
                                    "order": 1,
                                    "tag": [{
                                            "name": "nmsl3-1",
                                        }],
                                })
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        assert r.json()["errcode"] == 0
        self.test_search()

    def test_del_tag(self):
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
                          params={"access_token": self.access_token},
                          json={
                                "tag_id": [
                                    "etSh86BgAAu9DHE8k_GeAir0E57YJtrg",
                                ],
                                "group_id": [
                                    "etSh86BgAAviLNsY7PeSBZoRtFNIJraw",
                                ]
                          })
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        assert r.json()["errcode"] == 0
        self.test_search()

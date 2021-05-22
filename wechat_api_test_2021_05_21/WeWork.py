# -*- coding: utf-8 -*-
# @File   : api
# @Time   : 2021/5/22 20:10 
# @Author : BLUE_JUZIUPUP
import json

import requests


class WeWork:

    def get_access_token(self):
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken',
                         params=({
                             "corpid": "wwf443a769ec9a969f",
                             "corpsecret": "vMWlkH8N-37OO4rm8qMk-279RjECOsogSin_I9kE-AA"}))
        assert r.json()["errcode"] == 0
        print(r.json()["access_token"])
        self.access_token = r.json()["access_token"]
        return self.access_token

    def search(self):
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
                          params ={"access_token":self.access_token},
                          json = {})
        return r

    def add_tag(self):
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
                          params ={"access_token":self.access_token},
                          json = {
                                    "group_name": "nmsl3",
                                    "order": 1,
                                    "tag": [{
                                            "name": "nmsl3-1",
                                        }],
                                })
        return r


    def del_tag(self):
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
        return r
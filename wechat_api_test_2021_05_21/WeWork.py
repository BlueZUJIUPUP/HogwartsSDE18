# -*- coding: utf-8 -*-
# @File   : api
# @Time   : 2021/5/22 20:10 
# @Author : BLUE_JUZIUPUP
import json

import requests


class WeWork:
    def __init__(self):
        self.corpid = "wwf443a769ec9a969f"
        self.corpsecret = "vMWlkH8N-37OO4rm8qMk-279RjECOsogSin_I9kE-AA"


    def get_access_token(self):
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken',
                         params=({
                             "corpid": self.corpid,
                             "corpsecret": self.corpsecret}))
        assert r.json()["errcode"] == 0
        print(r.json()["access_token"])
        self.access_token = r.json()["access_token"]
        return self.access_token

    def search(self,tag_id = None , group_id = None):
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
                          params ={"access_token":self.access_token},
                          json = {
                                    "tag_id":
                                    [
                                        tag_id
                                    ],
                                    "group_id":
                                    [
                                        group_id
                                    ]
                                })
        #print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r

    def add_tag(self,group_name,tag_name):
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
                          params ={"access_token":self.access_token},
                          json = {
                                    "group_name": group_name,
                                    "order": 1,
                                    "tag": [{
                                            "name": tag_name,
                                        }],
                                })
        #print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r

    def del_tag(self,tag_id = None , group_id = None):
        if tag_id != None or group_id != None:
            r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
                              params={"access_token": self.access_token},
                              json={
                                    "tag_id": [
                                        tag_id,
                                    ],
                                    "group_id": [
                                        group_id,
                                    ]
                              })
            #print(json.dumps(r.json(), indent=2, ensure_ascii=False))
            return r
        else:
            print("需要一个tagid或者groupid")

    def edit_tag(self,TAG_ID,name):
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
                          params={"access_token": self.access_token},
                          json={
                                "id": TAG_ID,
                                "name": name
                            })
        # print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r



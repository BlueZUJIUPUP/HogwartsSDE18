# -*- coding: utf-8 -*-
# @File   : api
# @Time   : 2021/5/22 20:10 
# @Author : BLUE_JUZIUPUP
import json

import requests

from wechat_api_test_2021_05_21.WeWoekApi.Base import Base


class Tag_Api(Base):
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



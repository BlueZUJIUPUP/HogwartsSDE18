# -*- coding: utf-8 -*-
# @File   : api
# @Time   : 2021/5/22 20:10 
# @Author : BLUE_JUZIUPUP
import json

import requests
from wechat_api_test_2021_05_21.WeWorkApi.WorkApi import WeWork


class Tag_Api(WeWork):
    def search(self, tag_id=None, group_id=None):
        data = {
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            'method': "post",
            'params': {"access_token": self.access_token},
            "json": {
                "tag_id": [tag_id],
                "group_id": [group_id]
            }
        }
        r = self.request(data)
        return r

    def add_tag(self, tag_list, group_name,**kwargs):
        if "json" in kwargs:
            json_data = kwargs['json']
        else:
            json_data = {
                'group_name': group_name,
                'tag': tag_list
            }
        data = {
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
            'method': "post",
            'params': {"access_token": self.access_token},
            "json":  json_data
        }
        r = self.request(data)
        return r

    def del_tag(self, tag_id=None, group_id=None):
        if tag_id != None or group_id != None:
            data = {
                "url": 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
                'method': "post",
                'params': {"access_token": self.access_token},
                "json": {"tag_id": [tag_id],
                         "group_id": [group_id, ]
                         }
            }
            r = self.request(data)
            return r

        else:
            print("需要一个tagid或者groupid")

    def edit_tag(self, TAG_ID, name):
        data = {
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
            'method': "post",
            'params': {"access_token": self.access_token},
            "json": {"id": TAG_ID,
                     "name": name
                     }
        }
        r = self.request(data)
        return r

    def clear_tag(self):
        r = self.search()
        tag_id_liat = [tag['id'] for group in r.json()['tag_group'] for tag in group['tag']]
        if len(tag_id_liat) != 0:
            self.del_tag(tag_id_liat)
            print("清理完成")
            return r
        else:
            print("没有数据需要清理")
    def select(self,name1,name2,f = None):
        select = self.search()
        data = json.dumps(select.json(), indent=2, ensure_ascii=False)
        if f == "in":
            assert name1 in data and name2 in data
        else:
            assert name1 not in data and name2 not in data

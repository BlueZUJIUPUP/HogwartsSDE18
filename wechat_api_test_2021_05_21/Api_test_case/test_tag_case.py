# -*- coding: utf-8 -*-
# @File   : test_API_case
# @Time   : 2021/5/22 20:10 
# @Author : BLUE_JUZIUPUP
import json
import time

from faker import Faker

from wechat_api_test_2021_05_21.utils.utils import Utils


class TestWework():
    def setup_class(self):
        self.fake = Faker()
        self.wework = Utils()
        self.access_token = self.wework.get_access_token()

    def test_search(self):
        r = self.wework.search()
        assert r.json()["errcode"] == 0

    def test_add_tag(self):
        self.tag_name = self.fake.date(pattern="%Y-%m-%d", end_datetime=None)
        r = self.wework.add_tag(self.tag_name,self.tag_name+"_1")
        assert r.json()["errcode"] == 0
        self.wework.select(self.tag_name,self.tag_name+"_1","in")

    def test_del_tag(self):
        r = self.wework.search().json()
        group_id = r["tag_group"][0]["group_id"]
        tag_id = r["tag_group"][0]["tag"][0]['id']
        print("del的group_id是："+group_id)
        print("del的tag_id是："+tag_id)
        deltag = self.wework.del_tag(tag_id,group_id)
        assert deltag.json()["errcode"] == 0
        self.wework.select(group_id, tag_id)

    def test_edit_tag(self):
        r = self.wework.search().json()
        tag_id = r["tag_group"][0]["tag"][0]['id']
        old_tag_name = r["tag_group"][0]["tag"][0]['name']
        new_tag_name = f"new_tag_{int(time.time())}"
        print(f"tag_id:{tag_id}的name：{old_tag_name}修改为：{new_tag_name}" )
        r = self.wework.edit_tag(tag_id,new_tag_name)
        assert r.json()["errcode"] == 0
        select = self.wework.search()
        data = json.dumps(select.json(), indent=2, ensure_ascii=False)
        assert old_tag_name not in data and  new_tag_name in data

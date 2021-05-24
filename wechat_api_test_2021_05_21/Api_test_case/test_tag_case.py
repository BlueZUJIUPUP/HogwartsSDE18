# -*- coding: utf-8 -*-
# @File   : test_API_case
# @Time   : 2021/5/22 20:10 
# @Author : BLUE_JUZIUPUP
import json
import time

from faker import Faker

from wechat_api_test_2021_05_21.WeWorkApi.externalcontact.tag_API import Tag_Api


class TestWework():
    def setup_class(self):
        corpid = "wwf443a769ec9a969f"
        extrnalcontac_corpsecret = "vMWlkH8N-37OO4rm8qMk-279RjECOsogSin_I9kE-AA"

        self.fake = Faker()
        self.wework = Tag_Api()
        self.wework.get_access_token(corpid,extrnalcontac_corpsecret)
        self.wework.clear_tag()

    def test_search(self):
        r = self.wework.search()
        assert r.json()["errcode"] == 0

    def test_add_tag(self):
        self.tag_name = "测试" + self.fake.date(pattern="%Y%m%d", end_datetime=None)
        print(self.tag_name + "****************")
        tag_list = [{"name" : f"{self.tag_name}"}]
        r = self.wework.add_tag(tag_list = tag_list, group_name = self.tag_name)
        assert r.json()["errcode"] == 0

        r = self.wework.search()
        assert r.json()["errcode"] == 0
        assert self.tag_name in [group['group_name'] for group in r.json()['tag_group']]

    def test_del_tag(self):
        self.tag_name = "测试" + self.fake.date(pattern="%Y%m%d", end_datetime=None)
        print(self.tag_name + "****************")
        tag_list = [{"name": f"{self.tag_name}"}]
        r = self.wework.add_tag(tag_list=tag_list, group_name=self.tag_name)
        assert r.json()["errcode"] == 0

        r = self.wework.search().json()
        group_id = r["tag_group"][0]["group_id"]
        tag_id = r["tag_group"][0]["tag"][0]['id']
        print("del的group_id是：" + group_id)
        print("del的tag_id是：" + tag_id)

        deltag = self.wework.del_tag(tag_id, group_id)
        assert deltag.json()["errcode"] == 0
        self.wework.select(group_id, tag_id)

    def test_edit_tag(self):
        self.tag_name = "测试" + self.fake.date(pattern="%Y%m%d", end_datetime=None)
        print(self.tag_name + "****************")
        tag_list = [{"name": f"{self.tag_name}"}]
        r = self.wework.add_tag(tag_list=tag_list, group_name="ceshi")
        assert r.json()["errcode"] == 0

        r = self.wework.search().json()
        tag_id = r["tag_group"][0]["tag"][0]['id']
        old_tag_name = r["tag_group"][0]["tag"][0]['name']
        new_tag_name = f"new_tag_{int(time.time())}"
        print(f"tag_id:{tag_id}的name：{old_tag_name}修改为：{new_tag_name}")
        r = self.wework.edit_tag(tag_id, new_tag_name)
        assert r.json()["errcode"] == 0

        select = self.wework.search()
        data = json.dumps(select.json(), indent=2, ensure_ascii=False)
        assert old_tag_name not in data and new_tag_name in data

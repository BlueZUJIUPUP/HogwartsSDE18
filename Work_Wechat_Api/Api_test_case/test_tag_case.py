# -*- coding: utf-8 -*-
# @File   : test_API_case
# @Time   : 2021/5/22 20:10 
# @Author : BLUE_JUZIUPUP
import json
import time

import allure
from faker import Faker

from Work_Wechat_Api.WeWorkApi.externalcontact.tag_API import Tag_Api

@allure.feature("企业标签模块")
class TestWework():
    @allure.story("模块初始化")
    def setup_class(self):
        corpid = "XXXXXXXXXXXXXXXXXXXXXXXXX"
        contact_corpsecret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

        self.fake = Faker()
        self.wework = Tag_Api()
        self.wework.get_access_token(corpid,extrnalcontac_corpsecret)
        self.wework.clear_tag()
    def setup(self):
        self.wework.clear_tag()

    @allure.story("测试搜索功能")
    def test_search(self):
        with allure.step("搜索全部的tag"):
            r = self.wework.search()
            assert r.json()["errcode"] == 0

    @allure.story("测试添加标签")
    def test_add_tag(self):
        self.tag_name = "测试" + self.fake.date(pattern="%Y%m%d", end_datetime=None)
        print(self.tag_name + "****************")
        tag_list = [{"name" : f"{self.tag_name}"}]
        with allure.step(f"添加tab：{tag_list}"):
            r = self.wework.add_tag(tag_list = tag_list, group_name = self.tag_name)
            assert r.json()["errcode"] == 0
        with allure.step(f"搜索全部的标签"):
            r = self.wework.search()
            assert r.json()["errcode"] == 0
        with allure.step(f"判断是否已经添加{tag_list}"):
            assert self.tag_name in [group['group_name'] for group in r.json()['tag_group']]

    @allure.story("测试删除标签")
    def test_del_tag(self):

        self.tag_name = "测试" + self.fake.date(pattern="%Y%m%d", end_datetime=None)
        print(self.tag_name + "****************")
        tag_list = [{"name": f"{self.tag_name}"}]
        with allure.step(f"添加tab：{tag_list}"):
            r = self.wework.add_tag(tag_list=tag_list, group_name=self.tag_name)
            assert r.json()["errcode"] == 0
        with allure.step("搜索全部的tag"):
            r = self.wework.search().json()
        group_id = r["tag_group"][0]["group_id"]
        tag_id = r["tag_group"][0]["tag"][0]['id']
        with allure.step(f"del的group_id是：{group_id}，del的tag_id是：{tag_id}"):
            deltag = self.wework.del_tag(tag_id, group_id)
        with allure.step("删除是否成功"):
            assert deltag.json()["errcode"] == 0
            self.wework.select(group_id, tag_id)

    def test_edit_tag(self):
        self.tag_name = "测试" + self.fake.date(pattern="%Y%m%d", end_datetime=None)
        print(self.tag_name + "****************")
        tag_list = [{"name": f"{self.tag_name}"}]
        with allure.step(f"添加tab：{tag_list}"):
            r = self.wework.add_tag(tag_list=tag_list, group_name="ceshi")
            assert r.json()["errcode"] == 0
        with allure.step("搜索全部的tag"):
            r = self.wework.search().json()
        tag_id = r["tag_group"][0]["tag"][0]['id']
        old_tag_name = r["tag_group"][0]["tag"][0]['name']
        new_tag_name = f"new_tag_{int(time.time())}"
        with allure.step(f"tag_id:{tag_id}的name：{old_tag_name}修改为：{new_tag_name}"):
            r = self.wework.edit_tag(tag_id, new_tag_name)
            assert r.json()["errcode"] == 0
        with allure.step("搜索全部的tag,看下是否添加成功"):
            select = self.wework.search()
            data = json.dumps(select.json(), indent=2, ensure_ascii=False)
            assert old_tag_name not in data and new_tag_name in data

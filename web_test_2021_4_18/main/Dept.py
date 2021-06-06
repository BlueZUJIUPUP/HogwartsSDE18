# -*- coding: utf-8 -*-
# @File   : Open_Test
# @Time   : 2021/4/21 22:08
# @Author : BLUE_JUZIUPUP

from selenium.webdriver.common.by import By

from web_test_2021_4_18.main.base_page import BasePage
from web_test_2021_4_18.main.main import mian_list


class dept(BasePage):
    # 点击"+"
    def clickadd(self,dept_name):
        self.find(By.CSS_SELECTOR, ".member_colLeft_top_addBtn").click()
        self.find(By.CSS_SELECTOR, '.js_create_party').click()
        self.find(By.CSS_SELECTOR,'[name="name"]').send_keys(dept_name)
        self.find(By.CSS_SELECTOR,'.qui_btn.ww_btn.ww_btn_Dropdown.js_toggle_party_list').click()
        self.find(By.CSS_SELECTOR, ".qui_dialog_body.ww_dialog_body [id='1688851345985345_anchor']").click()
        self.find(By.CSS_SELECTOR,'.qui_dialog_foot.ww_dialog_foot .qui_btn.ww_btn.ww_btn_Blue').click()
        return mian_list(self.driver)



class dept_1(BasePage):
    # 点击"+"
    def clickadd(self):
        self.find(By.CSS_SELECTOR, ".member_colLeft_top_addBtn").click()
        return self.add_dept_btn()


    # 点击添加部门
    def add_dept_btn(self):
        self.find(By.CSS_SELECTOR, '.js_create_party').click()
        return self.sendkey_dept_name()

    # 输入部门名称
    def sendkey_dept_name(self):
        self.driver.find_element_by_xpath('//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[1]/input').send_keys(
            "ceshi03")
        return self.dept_select()
    # 部门下拉框
    def dept_select(self):
        self.driver.find_element_by_xpath('//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[3]/a').click()
        return self.select_dept()

    # 选择部门
    def select_dept(self):
        self.find(By.CSS_SELECTOR, ".qui_dialog_body.ww_dialog_body [id='1688851345985345_anchor']").click()
        return self.add_finish_btn()
    # 点击确定按钮
    def add_finish_btn(self):
        self.driver.find_element_by_xpath('//*[@id="__dialog__MNDialog__"]/div/div[3]/a[1]').click()
        return mian_list(self.driver)

    # 点击取消按钮
    def add_cancel_btn(self):
        self.driver.find_element_by_xpath('//*[@id="__dialog__MNDialog__"]/div/div[3]/a[2]').click()
        return print("12")
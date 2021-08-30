# -*- coding: utf-8 -*-
# @File   : Open_Test
# @Time   : 2021/4/21 22:08
# @Author : BLUE_JUZIUPUP

import time
import yaml
from selenium import webdriver


class Testcookie:

    def setup(self):
        print("开始运行")

    def teardown(self):
        self.driver.quit()
        print("结束运行")


    def test_save_cookei(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        time.sleep(20)
        cookie = self.driver.get_cookies()
        # 把cookie存如yaml文件内
        with open("data.yaml", "w", encoding="UTF-8") as f:
            yaml.dump(cookie, f)



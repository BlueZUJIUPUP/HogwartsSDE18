import time

import yaml
from selenium import webdriver


def test_save_cookei():
    driver = webdriver.Chrome()
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
    time.sleep(20)
    cookie = driver.get_cookies()
    # ��cookie����yaml�ļ���
    with open("data.yaml", "w", encoding="UTF-8") as f:
        yaml.dump(cookie, f)

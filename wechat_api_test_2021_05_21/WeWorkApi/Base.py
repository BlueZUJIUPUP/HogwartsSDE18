# -*- coding: utf-8 -*-
# @Time    : 2021/5/23 10:48
# @Author  : BLUE_JUZIUPUP
# @Email   : z1003033614@163.com
# @File    : Base.py
# @Software: PyCharm
import requests

class Base:
    def __init__(self):
        self.corpid = "wwf443a769ec9a969f"
        self.corpsecret = "vMWlkH8N-37OO4rm8qMk-279RjECOsogSin_I9kE-AA"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
        }


    def get_access_token(self):
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken',
                         params=({
                             "corpid": self.corpid,
                             "corpsecret": self.corpsecret}),
                         headers = self.headers)
        assert r.json()["errcode"] == 0
        print(r.json()["access_token"])
        self.access_token = r.json()["access_token"]
        return self.access_token

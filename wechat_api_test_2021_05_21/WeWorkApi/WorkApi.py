# -*- coding: utf-8 -*-
# @Time    : 2021/5/24 20:24
# @Author  : BLUE_JUZIUPUP
# @Email   : z1003033614@163.com
# @File    : WorkApi.py
# @Software: PyCharm
import logging

from wechat_api_test_2021_05_21.WeWorkApi.Base import Base
logging.basicConfig(level=logging.INFO)

class WeWork(Base):

    def get_access_token(self,corpid,corpsecret):
        data={
            "url" : 'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            'method' : "get",
            'params' :  {
                "corpid": corpid,
                "corpsecret": corpsecret
            }
        }
        r = self.request(data)
        assert r.json()["errcode"] == 0
        self.access_token = r.json()["access_token"]
        logging.info(self.access_token)

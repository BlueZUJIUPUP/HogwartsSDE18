# -*- coding: utf-8 -*-
# @Time    : 2021/5/23 10:48
# @Author  : BLUE_JUZIUPUP
# @Email   : z1003033614@163.com
# @File    : Base.py
# @Software: PyCharm
import json
import logging

import requests
logging.basicConfig(level=logging.INFO)


class Base:

    def request(self, datas : dict):
        if "url" in datas:
            return self.http_request(datas)

        elif 'rpc' == datas.get("protocol"):
            return self.rpc_request(datas)



    def http_request(self, datas):
        r = requests.request(**datas)
        logging.info(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r

    def rpc_request(self,datas):
        pass

    def tcp_request(self):
        pass
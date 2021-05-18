# -*- coding: utf-8 -*-
# @File   : recursion
# @Time   : 2021/5/18 15:50 
# @Author : BLUE_JUZIUPUP

# -*- coding: utf-8 -*-
# @File   : rewrite1
# @Time   : 2021/5/18 14:38
# @Author : BLUE_JUZIUPUP
"""HTTP-specific events."""
import json

import mitmproxy.http


class Events:

    def response(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP response has been read.
        """
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url:
            print("-"*30)
            print(flow.response.text)


            old_data = json.loads(flow.response.text)
            new_data = self.fload_date_chauns_modify(old_data,4)
            flow.response.text = json.dumps(new_data)


    def fload_date_chauns_modify(self,data,index):
        if isinstance(data,dict):
            for k,v in data.items():
                data[k] = self.fload_date_chauns_modify(v,index)
        elif isinstance(data,list):
            data = [self.fload_date_chauns_modify(i,index) for i in data]
        elif isinstance(data,float):
            data = data * index
        else:
            data = data
        return data



addons = [
    Events()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump
    #使用debug模式启动mitmdump
    mitmdump(['-p', '8080', '-s', __file__])

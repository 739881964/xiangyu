# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:xiangyu
# phone：19942429056
# datetime:2019/9/4 10:45
# software: PyCharm
import json
import requests
from scripts.log_class import loger


class HttpRequest(object):

    def __init__(self):
        self.session = requests.Session()

    def get_method(self, method, url, data=None, is_json=False, **kw):

        method = method.upper()
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except Exception as e:
                loger.error(f'Params data format is not right: {e}')
                data = eval(data)

        res = None
        if method == 'GET':
            res = self.session.request(method, url, params=data, **kw)
        elif method == 'POST':
            if is_json:
                res = self.session.request(method, url, json=data, **kw)
            else:
                res = self.session.request(method, url, data=data, **kw)
        else:
            print(f'Method {method} is not define')
            loger.error(f'Method {method} is not define')

        # return res.json()
        return res

    def close_session(self):
        self.session.close()


if __name__ == '__main__':
    http = HttpRequest()
    _url = 'www.baidu.com'
    _data = {'kw': 'Python'}
    http.get_method('delete', _url, _data)

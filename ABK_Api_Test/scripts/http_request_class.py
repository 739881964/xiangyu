# coding=utf-8
import json
import requests
from scripts.log_class import loger


class HttpRequest(object):

    def __init__(self):
        self.session = requests.session()

    def get_method(self, method, url, data=None, is_json=False, **kw):
        method = method.upper()

        if isinstance(data, str):
            try:
                data = json.loads(data)
            except Exception as e:
                loger.error('参数数据格式不正确: %s' % e)
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
            print('%s is not define' % method)
            loger.error('%s is not define' % method)

        return res.json()
        # return res

    def close_session(self):
        self.session.close()

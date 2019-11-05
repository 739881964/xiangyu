# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:xiangyu
# phone：19942429056
# datetime:2019/9/4 10:45
# software: PyCharm


from suds.client import Client
from scripts.log_class import loger
import json
# import xml.etree.ElementTree as ET
from suds.sudsobject import asdict
import suds


class WebServiceRequest(object):

    @classmethod
    def to_data(cls, url, method, data):

        if isinstance(data, str):
            try:
                data = json.loads(data)
            except Exception as e:
                loger.error('参数格式不正确：%s' % e)
                data = eval(data)

        try:
            res = eval(f'Client("{url}").service.{method}({data})')
            res = str(asdict(res))  # str字典
        except suds.WebFault as e:
            res = str(e.fault['faultstring'])  # 同上
            # print(res)

        return res


if __name__ == '__main__':
    params = {"uid": "", "true_name": "yuxiang", "cre_id": "342921199411244416"}
    # params = {"client_ip": "172.1.1.1", "tmpl_id": "1", "mobile": "1825696625"}
    # params = {"verify_code": "2134", "user_id": "123", "channel_id": "3", "pwd": "",
    #           "mobile": "13625696627", "ip": "172.1.1.1"}
    _url = "http://120.24.235.105:9010/finance-user_info-war-1.0/ws/financeUserInfoFacade.ws?wsdl"
    result = WebServiceRequest().to_data(_url, 'verifyUserAuth', params)

    print(result)

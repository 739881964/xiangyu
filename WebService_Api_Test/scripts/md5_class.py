# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:xiangyu
# phone：19942429056
# datetime:2019/9/4 10:45
# software: PyCharm
import hashlib
# from scripts.http_request_class import HttpRequest
import base64


class MD5(object):

    # 加密方法
    @staticmethod
    def generate_md5(data):

        hs = hashlib.md5()  # md5对象
        hs.update(data.encode(encoding='utf-8'))  # 声明encode

        return hs.hexdigest()

    # 解密方法
    @staticmethod
    def decode_base_md5(data):

        return base64.b64decode(data)


if __name__ == '__main__':
    string = 'Yx201308'
    print(MD5().generate_md5(string))
    # print(MD5.decode_base_md5('5eb63bbbe01eeed093cb22bb8f5acdc3'))

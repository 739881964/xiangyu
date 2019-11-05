# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/21 9:15
# @Author  : Xiang Yu
# @File    : get_dict_content.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


"""
请写一段代码，向http://httpbin.org/json这个API发送一个Get请求，
并打印响应里的title字段的值，和slides字段里元素的个数。
输出格式：titile: xxx, slides count: x
"""


import json

import requests


json_data = {
  "slideshow": {
    "author": "Yours Truly",
    "date": "date of publication",
    "slides": [
      {
        "title": "Wake up to WonderWidgets!",
        "type": "all"
      },
      {
        "items": [
          "Why <em>WonderWidgets</em> are great",
          "Who <em>buys</em> WonderWidgets"
        ],
        "title": "Overview",
        "type": "all"
      }
    ],
    "title": "Sample Slide Show"
  }
}


# 1.类属性保存变量
class GetDictContent(object):
    """ get dict content what need """

    def __init__(self, dic=None):
        self.dic = dic
        self.value_list = []
        self.length_list = []

    def get_value(self, string: str, a_dict: (str, dict)) -> str:
        """ get dict_valve """
        # dic = None
        try:
            if isinstance(a_dict, dict):
                self.dic = a_dict
            else:
                self.dic = eval(a_dict)
        except TypeError as e:
            print(e)

        for key, value in self.dic.items():
            if key == string:
                self.value_list.append(value)
            else:
                if isinstance(value, dict):
                    self.get_value(string, value)
                elif isinstance(value, list):
                    for one_data in value:
                        if isinstance(one_data, dict):
                            self.get_value(string, one_data)

        return '{}: {}'.format(string, ''.join(self.value_list))

    def get_value_len(self, string: str, a_dict: (str, dict)) -> str:
        """ get dic_value length """
        # dic = None
        try:
            if isinstance(a_dict, dict):
                self.dic = a_dict
            else:
                self.dic = eval(a_dict)
        except TypeError as e:
            print(e)

        for key, value in self.dic.items():
            if key == string:
                if isinstance(value, str):
                    self.length_list.append(1)
                elif isinstance(value, (list, dict)):
                    self.length_list.append(len(value))
            else:
                if isinstance(value, dict):
                    self.get_value_len(string, value)
                elif isinstance(value, list):
                    for one_data in value:
                        if isinstance(one_data, dict):
                            self.get_value_len(string, one_data)

        len_value = sum(self.length_list)

        return '{} count: {}'.format(string, len_value)

    def main(self, url, v_data, l_data):
        result = requests.get(url).json()
        ts = self.get_value(v_data, result)
        ss = self.get_value_len(l_data, result)
        print('{}, {}'.format(ts, ss))


# 2.global全局变量
title = []


def get_title(string, data):
    # global title

    dic = None
    try:
        if isinstance(data, dict):
            dic = data
        else:
            dic = eval(data)
    except TypeError as e:
        print(e)

    for key, value in dic.items():
        if key == string:
            title.append(value)
        else:
            if isinstance(value, dict):
                get_title(string, value)
            elif isinstance(value, list):
                for one_data in value:
                    if isinstance(one_data, dict):
                        get_title(string, one_data)

    return '{}: {}'.format(string, ''.join(title))
    # return title


# 闭包
def factory():
    titles = []

    def go(string, data):
        # nonlocal titles
        dic = None
        try:
            if isinstance(data, dict):
                dic = data
            else:
                dic = eval(data)
        except TypeError as e:
            print(e)

        for key, value in dic.items():
            if key == string:
                titles.append(value)
            else:
                if isinstance(value, dict):
                    go(string, value)
                elif isinstance(value, list):
                    for one_data in value:
                        if isinstance(one_data, dict):
                            go(string, one_data)

        return '{}: {}'.format(string, ''.join(titles))
    return go


if __name__ == "__main__":
    __url = 'http://httpbin.org/json'
    __v_data, __l_data = 'title', 'slides'
    obj = GetDictContent()
    obj.main(url=__url, v_data=__v_data, l_data=__l_data)

    result = requests.get(__url).json()
    res = get_title('title', result)
    print(res)

    f = factory()
    r = f('title', result)
    print(r)


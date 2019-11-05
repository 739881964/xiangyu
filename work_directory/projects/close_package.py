# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/23 9:50
# @Author  : Xiang Yu
# @File    : close_package.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


import requests


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


if __name__ == "__main__":
    __url = 'http://httpbin.org/json'
    result = requests.get(__url).json()

    res = get_title('title', result)
    print(res)

    f = factory()
    r = f('title', result)
    print(r)


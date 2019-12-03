#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-05 22:45
# @Author  : Yu xiang
# @File    : calculate_error_rate.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


import json
import re


def read_rs_trip_data(file_name):
    """abandon \n from data to list"""
    try:
        with open(file_name, 'r', encoding='gbk') as f:
            f_data = list(map(lambda line: line.rstrip('\n'), f.readlines()))
    except:
        with open(file_name, 'r', encoding='utf-8') as f:
            f_data = list(map(lambda line: line.rstrip('\n'), f.readlines()))

    return f_data


if __name__ == "__main__":
    path = 'D:\\123.txt'
    data = read_rs_trip_data(path)
    pattern = re.compile('[\u4e00-\u9fa5]+')
    _data = list(filter(lambda x: pattern.findall(x)[0] if pattern.findall(x) else False, data))
    __data = list(map(lambda x: pattern.findall(x)[0], _data))
    command = set(__data)
    num = 0
    dic = {}
    for i in command:
        if len(i) > 1:
            num += __data.count(i)
            dic[i] = str(__data.count(i)) + '次'

    print('误识别总数: ' + str(num))
    print(json.dumps(dic, ensure_ascii=False, sort_keys=2, indent=True))


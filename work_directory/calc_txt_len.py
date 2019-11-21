# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 14:06
# @Author  : Xiang Yu
# @File    : calc_txt_len.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE

import json
import os
import re
from functools import reduce
from scripts.text_manual import read_rs_trip_data
from scripts.pandas_manual import PandasManual

""""""

# path = 'D:\\65.xlsx'
# panda = PandasManual(path)
# data = panda.get_data(sheet='all_com_wav')['start_time'].tolist()
# list1 = []
# for i in data:
#     x = data.count(i)
#     if x != 1:
#         print(i)
# print(len(set(data)))


#
#
# data = read_rs_trip_data(path)
# one_list = list()
# for one_data in data:
#     pattern = re.compile('.*\.wav')
#     if pattern.findall(one_data):
#         one_list.append(pattern.findall(one_data)[0])
#
# _list = []
# for i in one_list:
#     if i not in _list:
#         _list.append(i)
#
# print(len(_list))
# print(len(set(one_list)))

src_path = r'C:\Users\xiangyu\Desktop\new_1_60'

files = os.listdir(src_path)
files_path = list(map(lambda x: os.path.join(src_path, x), files))

one_list = list(map(lambda x: len(read_rs_trip_data(x)), files_path))
count = reduce(lambda x, y: x + y, one_list)
print(count)

one_dict = {}
for i in range(len(files)):
    one_dict[files[i].split('.')[0]] = one_list[i]

# print(one_dict)
for k, v in one_dict.items():
    if (v == 60) or (v == 180):
        pass
    else:
        print(k, v)

data = json.dumps(one_dict, ensure_ascii=False, sort_keys=2, indent=True)
print(data)

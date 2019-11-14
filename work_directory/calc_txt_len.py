# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 14:06
# @Author  : Xiang Yu
# @File    : calc_txt_len.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


import os

from functools import reduce
from scripts.text_manual import read_rs_trip_data


src_path = r'C:\Users\xiangyu\Desktop\finally_list'

files = os.listdir(src_path)
files_path = list(map(lambda x: os.path.join(src_path, x), files))

one_list = list(map(lambda x: len(read_rs_trip_data(x)), files_path))
count = reduce(lambda x, y: x + y, one_list)
print(count)

one_dict = {}
for i in range(len(files)):
    one_dict[files[i]] = one_list[i]

# print(one_dict)
for k, v in one_dict.items():
    if (v == 60) or (v == 180):
        pass
    else:
        print(k, v)

# print(count)
# print(one_dict)

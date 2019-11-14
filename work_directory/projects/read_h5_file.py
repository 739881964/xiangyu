# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/31 12:57
# @Author  : Xiang Yu
# @File    : read_h5_file.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


import h5py


# HDf5文件读取
h5_file_path = r'C:\Users\xiangyu\Documents\model.v2.0.h5'
f = h5py.File(h5_file_path, 'r')
data = f.items()


# 可以查看所有的主键
# for key in f.keys():
# for key, value in data:
    # print(key, value)
    # print(f[key].name)
    # print(f[key].shape)
    # print(f[key].value)


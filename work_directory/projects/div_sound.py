# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/10 10:38
# @Author  : Xiang Yu
# @File    : div_sound.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE

import os


def read_bin(file_path):
    with open(file_path, 'rb') as f:
        print(f.readlines())
        # data_size = os.path.getsize(file_path)
        # print(data_size)
        # for i in range(data_size):
        #     one_data = f.read(100)
        #     print(one_data)


if __name__ == "__main__":
    bin_path = r'C:\Users\xiangyu\Desktop\bin\Bach_20191122_102254 (2).pcm'
    read_bin(bin_path)

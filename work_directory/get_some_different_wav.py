# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/11 14:16
# @Author  : Xiang Yu
# @File    : get_some_different_wav.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


from scripts.text_manual import read_rs_trip_data, write_txt_once


map_path = r'C:\Users\xiangyu\Desktop\new_wav_url\wav_test.map'
txt_path = r'D:\dl_wl\设置为灯带.txt'
__txt_path = r'D:\dl_wl\灯带.txt'


map_data = read_rs_trip_data(map_path)[::-1]
txt_data = read_rs_trip_data(txt_path)


for i in map_data:
    for j in txt_data:
        map_zh = i.split()[2]
        one_map = i.split()[0]
        one_txt = j.split('\\')[-1][:-4]
        if map_zh == '设置为灯带':
            if one_map != one_txt:
                write_txt_once(__txt_path, one_map)
                content = read_rs_trip_data(__txt_path)
                if len(content) == 10:
                    break


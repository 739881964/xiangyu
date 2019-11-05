# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/11 10:23
# @Author  : Xiang Yu
# @File    : find_lost_wav.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


import os
from scripts.text_manual import get_all_file_path, read_rs_trip_data
from concurrent.futures import ThreadPoolExecutor
from functools import reduce


word_path = r'D:\dl_wl'
wav_path = r'\\192.168.1.12\hftest\hfwav\tongyongduolian'


name = [r'\\192.168.1.12\hftest\hfwav\tongyongduolian\TJ0041063@TJ0041063B01_0147.wav',
        r'\\192.168.1.12\hftest\hfwav\tongyongduolian\TJ0041079@TJ0041079B01_0147.wav']


wav_name = os.listdir(wav_path)
word_name = os.listdir(word_path)

wav_name_path = get_all_file_path(wav_path, wav_name)
word_name_path = get_all_file_path(word_path, word_name)

content = list(map(read_rs_trip_data, word_name_path))
data = reduce(lambda x, y: x + y, content)
length = list(map(lambda x: len(set(x)), content))

# for i in data:
#     if data.count(i) > 1:
#         print(i)

for i in name:
    for j in word_name_path:
        res = read_rs_trip_data(j)
        if i in res:
            print(j)


# print(length)
# print(len(data))
# print(len(wav_name_path))
# print(len(set(data)))
#
#
# for i in range(len(word_name_path)):
#     content = read_rs_trip_data(word_name_path[i])
#     for one_data in content:
#         if one_data not in wav_name_path:
#             print(word_name_path[i], one_data)
#

# def find_lost(i):
#     word_content = read_rs_trip_data(word_name_path[i])
#     for data in word_content:
#         # for wav in wav_name_path:
#         #     if data == wav:
#         #         break
#         if data not in wav_name_path:
#             print("{} 中 {} 音频不存在！！！".format(word_name_path[i], data))
#         else:
#             # print(data)
#             pass
#
#
# def main():
#     with ThreadPoolExecutor(max_workers=30) as pool:
#         for i in range(len(word_name_path)):
#             pool.map(find_lost, [i])
#
#
# if __name__ == "__main__":
#     main()


# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 9:22
# @Author  : Xiang Yu
# @File    : practice_re.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE

import time

import pandas as pd
import re

import yaml
import os
from scripts.base_path import RESULT_LOG, COMPARE_FILE, DATA_PATH, EXCEL_PATH
# from scripts.text_manual import *
from scripts.conf_manual import config
from scripts.excel_manual import ExcelManual
from scripts.text_manual import (read_rstrip_data,
                                 get_res_count_data,
                                 get_all_command_times,
                                 )


a = [1, 2, 3, 4, 5]
print(a[:0])


# with open('path.yaml', 'r', encoding='utf-8') as f:
#     content = yaml.load(f, Loader=yaml.FullLoader)
#     print(content)


# e = []
# g = [1, 3, 3, 4, 4]
# for i in g:
#     if i not in e:
#         e.append(i)
# print(e)


# def _get_all_command_times(a_list):
#     # 统计每个命令次出现的次数-list
#     one_list = list()
#     for i in a:
#         if i not in one_list:
#             one_list.append(i)
#
#     times = list(map(lambda y: a_list.count(y), one_list))
#
#     return one_list, times


# def if_in_func(data):
#     """获取compare时间列表，根据 '[' or ']' 判断"""
#     time_list = list(map(lambda y: y[1:-1], list(filter(lambda x: '[' in x, data))))
#
#     return time_list


# a = [1, 1, 1, 3, 3, 4]
#
# c, d = _get_all_command_times(a)
# print(c, d)


# times = list(map(lambda x: a.count(x), set(a)))
#
# print(times)


# if r'\\192.168.200.20\backup\Algorithm\speech_data\wav\small\tj20190311\wav\anjianjun@anjianjun_tj20190311_01_01.wav':
#     print(1)

#     os.remove(RESULT_EXCEL_PATH)
#     os.mkdir(DATA_PATH + '\\' + 'result_excel.xlsx')
# else:
#     os.mkdir(DATA_PATH + '\\' + 'result_excel.xlsx')


# df = pd.DataFrame([1, 2, 3, 4, 5, 6, 7])
# df.to_csv(r'C:\Users\xiangyu\xiangyu_git\work_dir\datas\test', mode='a', index=False)
#
# a = ['sa', 'wq'] * 2
# b = ['w', 'f'] * 3
# c = a + b
# print(c)
# url = 'https://www.baidu.com/get_list?name=1&age=2&hshs=3'
# data = re.findall('(\w+)=(\w+)', url)
# print(data)

# for i in range(0, 101, 2):
#   time.sleep(0.1)
#   num = i // 2
#   if i == 100:
#     process = "\r[%3s%%]: |%-50s|\n" % (i, '|' * num)
#   else:
#     process = "\r[%3s%%]: |%-50s|" % (i, '|' * num)
#   print(process, end='', flush=True)

# a = list(range(10))
# b = list(range(8))
#
# for i in a:
#     for j in b:
#         if i == j:
#             pass
#             # print(i)
#         elif i != j:
#             print(i)

# print(list(dp()))


# content = read_rs_trip_data(r'C:\Users\xiangyu\xiangyu_git\work_dir\files\compare2.log')
# data = "[2019-09-15 09:25:54.878]  dxsz_isr_index_result SpottingWordList[1][28584] 森歌森歌"
# d = '[2019-09-15 12:47:28.935]  dxsz_isr_index_result SpottingWordList[28][23020] 打开延迟'
#
# res = data.split()
# resp = d.split()
# a = res[0] + ' ' + res[1]
# print(a)
# # print(resp)
# a = (res[0] + ' ' + res[1])[1:-1]
# b = (resp[0] + ' ' + resp[1])[1:-1]
# print(a < b)
# all_res_list = read_rstrip_data(RESULT_LOG)[8::2]
# print(all_res_list)
# res = read_rs_trip_data(Info.commands_file)
# resp = get_split_zh(res)
# resp = get_one_time(data)
# print(resp)


# def write_in_txt():
#     start_time = time.ctime()
#     with open(r'C:\Users\xiangyu\xiangyu_git\work_dir\datas\data.txt', 'r', encoding='utf-8') as f:
#         content = f.read().strip()
#     end_time = start_time, time.ctime()
#     print(end_time, len(content))


if __name__ == '__main__':

    # write_in_txt()

    pass

    # all_count_data = read_rstrip_data(RESULT_LOG)  # 获取result日志的内容-list
    # count_data = get_res_count_data(all_count_data)  # 获取需要的日志内容
    # a_list = []
    # for data in count_data:
    #     if re.findall('[[](.*?)[]]', data):
    #         res = re.findall('[[](.*?)[]]', data)[0]
    #         a_list.append(res)


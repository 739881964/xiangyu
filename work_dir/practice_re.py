# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 9:22
# @Author  : Xiang Yu
# @File    : practice_re.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE

import re
from scripts.base_path import RESULT_LOG, COMPARE_FILE
from scripts.text_manual import *
from scripts.conf_manual import config
from scripts.excel_manual import ExcelManual
from path.test_path import Info


# content = read_rs_trip_data(r'C:\Users\xiangyu\xiangyu_git\work_dir\files\compare2.log')
data = "[2019-09-15 09:25:54.878]  dxsz_isr_index_result SpottingWordList[1][28584] 森歌森歌"
d = '[2019-09-15 12:47:28.935]  dxsz_isr_index_result SpottingWordList[28][23020] 打开延迟'

res = data.split()
resp = d.split()
a = res[0] + ' ' + res[1]
print(a)
# print(resp)
a = (res[0] + ' ' + res[1])[1:-1]
b = (resp[0] + ' ' + resp[1])[1:-1]
print(a < b)
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
    '''
    all_count_data = read_rstrip_data(RESULT_LOG)  # 获取result日志的内容-list
    count_data = get_res_count_data(all_count_data)  # 获取需要的日志内容
    list = []
    for data in count_data:
        if re.findall('[[](.*?)[]]', data):
            res = re.findall('[[](.*?)[]]', data)[0]
            list.append(res)
    '''

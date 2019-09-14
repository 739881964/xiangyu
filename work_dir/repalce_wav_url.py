# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/12 18:34
# @Author  : Xiang Yu
# @File    : repalce_wav_url.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE

from path.test_path import Info
from scripts.text_manual import *
import re
from scripts.base_path import ALL_TXT_PATH
from scripts.log_manual import log

all_file = get_all_file(Info.all_txt)  # 55个txt文件
all_file_path = get_all_file_path(Info.all_txt, all_file)  # 55个txt文件路径
one_data = read_log_to_list(all_file_path[0])  # 一个txt文件的内容
# print(len(one_data))  # 100
new_txt_file = [Info.new_txt_file + i  for i in all_file]  # 新的txt文件路径

for num in range(len(new_txt_file)):  # 55个文件
    for data in one_data:
        pos = 0
        st = 0
        while True:
            index = data.find('\\', st)
            if index == -1:
                break
            pos = index
            st  = index + 1
        wav_name = data[pos+1:-1]  # 文件名称
        wav_info = Info.new_path + wav_name
        write_txt_once(new_txt_file[num], wav_info)
        log.error(wav_info)

    pass

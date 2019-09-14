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

all_file = get_all_file(Info.all_txt)  # txt文件个数
all_file_path = get_all_file_path(Info.all_txt, all_file)  # 55个txt文件路径
new_txt_file = [Info.new_txt_file + i  for i in all_file]  # 新的txt文件路径

for num in range(len(new_txt_file)):  # 文件l个数
    # for num in [0, 2]:
    data = read_log_to_list(all_file_path[num])
    for one_data in data:
        pos = 0
        st = 0
        while True:
            index = one_data.find('\\', st)
            if index == -1:
                break
            pos = index
            st  = index + 1
        wav_name = one_data[pos+1:-1]  # 文件名称
        wav_info = Info.new_path + wav_name
        write_txt_once(new_txt_file[num], wav_info)
        log.error(wav_info)

    pass

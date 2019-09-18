# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-05 22:45
# @Author  : 余翔
# @File    : get_word_list_use_replace.py
# @Company : BEIJING INTENGINE

import time
from scripts.excel_manual import ExcelManual
from scripts.conf_manual import config
from scripts.log_manual import log
from path.test_path import Info
from scripts.text_manual import write_txt_once, read_rs_trip_data, get_split_zh, read_log_to_list


if __name__ == '__main__':
    """从.map文件获取命令词的语音"""
    one_time = time.ctime()
    print('starting......')
    data = read_rs_trip_data(Info.commands_file)
    commands = get_split_zh(data)  # 获取命令词

    one_txt_name = [Info.new_word_list_path + '\\' + commands[i] + '.txt' for i in range(len(commands))]
    map_content = read_log_to_list(Info.local_map_file)  # get .map data
    for one_row in map_content:
        row = one_row.split()
        for j in range(len(commands)):
            if commands[j] == row[2]:
                after_replace = row[1].replace(Info.be_replaced, Info.replace_else)
                write_data = after_replace.replace('/', '\\')
                write_txt_once(one_txt_name[j], write_data)
                # log.error(write_data)

    print("SUCCESS")
    print(one_time, '   ', time.ctime())

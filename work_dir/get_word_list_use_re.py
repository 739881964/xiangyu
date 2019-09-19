# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-05 22:45
# @Author  : Xiang Yu
# @File    : get_word_list_use_replace.py
# @Company : BEIJING INTENGINE

import time
from scripts.excel_manual import ExcelManual
from scripts.conf_manual import config
import re
from scripts.log_manual import log
from path.test_path import Info
from scripts.text_manual import write_txt_once, read_rs_trip_data, get_one_key, get_split_zh


if __name__ == '__main__':
    """从.map文件获取命令词的语音"""
    print('Beginning......')
    one_time = time.ctime()
    data = read_rs_trip_data(Info.commands_file)
    commands = get_split_zh(data)  # 获取命令词
    all_txt_name = [Info.new_word_list_path + '\\' + commands[i] + '.txt' for i in range(len(commands))]

    rows = read_rs_trip_data(Info.local_map_file)  # map文件路径
    for one_row in rows:
        word = get_one_key(one_row)
        for i in range(len(commands)):
            if word == commands[i]:
                wav_url = re.search('/.*\.wav', one_row).group()
                final_data = wav_url.replace(Info.be_replaced, Info.replace_else)
                final_data = final_data.replace('/', '\\')
                write_txt_once(all_txt_name[i], final_data)
                print(final_data)
                # log.error(final_data)

    print("Finished")
    print(one_time, '   ', time.ctime())

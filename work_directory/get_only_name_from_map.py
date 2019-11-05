# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/26 12:18
# @Author  : Xiang Yu
# @File    : get_only_name_from_map.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


import os
import time
from path.test_path import Info
from scripts.text_manual import (write_txt_once,
                                 read_log_to_list,
                                 get_all_word,
                                 read_rs_trip_data,
                                 remove_txt
                                 )


com_path = r'C:\Users\xiangyu\Documents\WeChat Files\yxlxlfr\FileStorage\File\2019-09\word_lists.txt'
map_path = r'C:\Users\xiangyu\Documents\WeChat Files\yxlxlfr\FileStorage\File\2019-09\wav_test.map'


now = lambda: time.ctime()


if __name__ == '__main__':
    """从.map文件获取命令词的语音"""
    # 执行前存在txt即会删除
    remove_txt(Info.new_word_list_path)

    print('Test start ......')
    one_time = now()

    # 获取命令词
    __m = 2  # 唤醒词个数
    __n = 60  # 其他命令词音频个数
    __m__ = __n * 3  # 唤醒词音频数

    # commands = get_all_word(Info.command_file)
    commands = get_all_word(com_path)
    one_txt_name = [os.path.join(Info.new_word_list_path, commands[i] + '.txt') for i in range(len(commands))]
    # map_content = read_log_to_list(Info.local_map_file)
    map_content = read_log_to_list(map_path)  # get .map data

    for j in range(len(commands)):
        for one_row in map_content:
            row = one_row.split()
            if j in range(__m):
                if commands[j] == row[2]:
                    if row[0][0] == 'T' or row[0][0] == 'S':
                        """
                        after_replace = row[1].replace(Info.be_replaced, Info.replace_else)
                        write_data = after_replace.replace('/', '\\')
                        write_txt_once(one_txt_name[j], write_data)
                        """
                        write_txt_once(one_txt_name[j], row[0])
                        if len(read_rs_trip_data(one_txt_name[j])) == __m__:
                            break
            else:
                if commands[j] == row[2]:
                    if row[0][0] == 'T' or row[0][0] == 'S':
                        """
                        after_replace = row[1].replace(Info.be_replaced, Info.replace_else)
                        write_data = after_replace.replace('/', '\\')
                        write_txt_once(one_txt_name[j], write_data)
                        """
                        write_txt_once(one_txt_name[j], row[0])
                        if len(read_rs_trip_data(one_txt_name[j])) == __n:
                            break
                        # log.error(write_data)

    print("Test finished !!!")
    print(one_time, '   ', now())

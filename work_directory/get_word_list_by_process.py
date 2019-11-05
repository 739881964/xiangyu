# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/12 14:02
# @Author  : Xiang Yu
# @File    : get_word_list_by_threading.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE

import multiprocessing
import os
import sys
from scripts.text_manual import (
    read_log_to_list,
    write_txt_once,
    remove_txt,
    run_time,
    read_rs_trip_data,
    get_all_file_path,
    get_all_word,
)
from scripts.log_manual import log
from scripts.excel_manual import ExcelManual
from scripts.conf_manual import config
from scripts.thread_manual import MYThread, MYProcess
from path.test_path import Info


def create_wav_txt(q, i, commands, map_content, one_txt_name,  __m, __n, __o):
    """ 替换wav路径 """
    # for i in range(len(commands)):
    for one_row in map_content:
        row = one_row.split()
        if i in range(__m):
            if commands[i] == row[2]:
                try:
                    after_replace = row[1].replace(Info.be_replaced, Info.replace_else)
                    write_data = after_replace.replace('/', '\\')
                    write_txt_once(one_txt_name[i], write_data)
                    if len(read_rs_trip_data(one_txt_name[i])) == __o:
                        q.put(one_txt_name[i])
                        break
                except Exception as e:
                    print(e)
                    log.error(e)
        else:
            try:
                if commands[i] == row[2]:
                    after_replace = row[1].replace(Info.be_replaced, Info.replace_else)
                    write_data = after_replace.replace('/', '\\')
                    write_txt_once(one_txt_name[i], write_data)
                    if len(read_rs_trip_data(one_txt_name[i])) == __n:
                        q.put(one_txt_name[i])
                        break
            except Exception as e:
                print(e)
                log.error(e)


@run_time()
def main(m, n, o, t):
    print('开始......')
    commands = get_all_word(Info.command_file)  # 命令词txt路径
    file_name = list(map(lambda x: x + '.txt', commands))
    one_txt_name = get_all_file_path(Info.new_word_list_path, file_name)  # 新存放word_list 路径
    map_content = read_log_to_list(Info.local_map_file)  # map 文件路径

    # 创建一个进程池
    po = multiprocessing.Pool(t)
    # 创建一个队列
    q = multiprocessing.Manager().Queue()
    for i in range(len(commands)):
        po.apply_async(create_wav_txt, args=(q, i, commands, map_content, one_txt_name, m, n, o))
    po.close()

    finished_num = 0
    while True:
        q.get()
        finished_num += 1
        _number = round(finished_num * 100 / len(commands), 2)
        process = '\r提取 word_list 的进度为: [%-50s] : [%.2f%%]' % ('>' * int(_number/2), (finished_num*100/len(commands)))
        print(process, end='', flush=True)
        if finished_num >= len(commands):
            break
    print()
    print('完成!!!')


if __name__ == '__main__':
    ''' 创建之前删除以前的txt文件 '''
    remove_txt(Info.new_word_list_path)

    __m__ = 1  # 唤醒词个数
    __n__ = 70  # 其他命令词音频个数
    __o__ = __n__ * 3  # 唤醒词音频数
    __t__ = 8  # 进程池进程数

    main(__m__, __n__, __o__, __t__)

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/12 14:02
# @Author  : Xiang Yu
# @File    : get_word_list_by_threading.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE

import os
from queue import Queue
import sys
import threading
import multiprocessing
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


def create_wav_txt(i, commands, map_content, one_txt_name,  __m, __n, __o):
    """ 替换url方法 """
    # for i in range(len(commands)):
    for one_row in map_content:
        row = one_row.split()
        if 'SPEAK' not in row[1]:
            if i in range(__m):
                if commands[i] == row[2]:
                    try:
                        after_replace = row[1].replace(Info.be_replaced, Info.replace_else)
                        write_data = after_replace.replace('/', '\\')
                        write_txt_once(one_txt_name[i], write_data)
                        if len(read_rs_trip_data(one_txt_name[i])) == __o:
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
                            break
                except Exception as e:
                    print(e)
                    log.error(e)


@run_time()
def main(m, n, o):
    print('开始......')
    # commands = get_all_word(Info.command_file)  # 命令词txt路径
    commands = ['小白你好', '你好小白', '你好小美', '打开壁灯',
                '打开餐厅灯', '打开厨房灯', '打开窗帘', '打开灯带', '打开大灯', '打开吊顶灯', '打开客厅灯',
                '打开纱帘', '打开筒灯', '打开卧室灯', '打开走廊灯', '大点声', '大声点',
                '关闭壁灯', '关闭餐厅灯', '关闭厨房灯', '关闭窗帘', '关闭大灯', '关闭灯带', '关闭吊顶灯',
                '关闭客厅灯', '关闭纱帘', '关闭筒灯', '关闭卧室灯', '关闭阅读灯',
                '关闭走廊灯', '减小音量', '进入开关设置', '进入开关设置模式', '设置二号开关', '设置三号开关',
                '设置为壁灯', '设置为餐厅灯', '设置为厨房灯', '设置为大灯', '设置为灯带',
                '设置为吊灯', '设置为客厅灯', '设置为纱帘', '设置为筒灯', '设置为卧室灯',
                '设置为阅读灯', '设置为走廊灯', '设置一号开关', '声音大一点', '声音小一点', '小点声', '小声点',
                '音量大一点', '音量小一点', '增大音量', '设置为窗帘', '开关设置模式', '打开阅读灯',
                '打开全部灯光', '关闭全部灯光'
                ]

    file_name = list(map(lambda x: x + '.txt', commands))
    one_txt_name = get_all_file_path(Info.new_word_list_path, file_name)  # 新存放word_list 路径
    map_content = read_log_to_list(Info.local_map_file)  # map 文件路径

    threads = []
    for i in range(len(commands)):
        t = MYThread(create_wav_txt, args=(i, commands, map_content, one_txt_name,  m, n, o))
        threads.append(t)

    for i in range(len(commands)):
        threads[i].start()

    for i in range(len(commands)):
        threads[i].join()

    print('完成!!!')


if __name__ == '__main__':
    ''' 创建之前删除以前的txt文件 '''
    remove_txt(Info.new_word_list_path)

    __m__ = 3  # 唤醒词个数
    __n__ = 120  # 其他命令词音频个数
    __o__ = __n__ * 3  # 唤醒词音频数

    main(__m__, __n__, __o__)


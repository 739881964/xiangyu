# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/12 14:02
# @Author  : Xiang Yu
# @File    : get_word_list_by_threading.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE

from scripts.text_manual import read_log_to_list, write_txt_once
from scripts.excel_manual import ExcelManual
from scripts.conf_manual import config
import re
from scripts.thread_manual import MYThread
import time
from scripts.log_manual import log
from path.test_path import Info

command_path = config.get_value('excel', 'command_path')
excel = ExcelManual(command_path, config.get_value('excel', 'sheet_name'))
data = excel.read_data()
commands = [i['命令词'] for i in data]  # 命令词
map_content = read_log_to_list(Info.normalize_file_path)  # get .map data


def create_wav_txt(i):
    one_txt_name = Info.new_word_list_path + '\\' + commands[i] + '.txt'  # txt_name
    for one_row in map_content:
        row = one_row.split()
        if commands[i] == row[2]:
            # after_replace = re.sub(Info.be_replaced, Info.replace_else, row[1])
            after_replace = row[1].replace(Info.be_replaced, Info.replace_else)
            last_data = after_replace
            if re.findall('/', after_replace):
                last_data = re.sub('/', r'\\', after_replace)
            write_txt_once(one_txt_name, last_data)
            log.error(last_data)


def main():
    print('starting......')
    start_time = time.ctime()
    threads = []

    for i in range(len(commands)):
        # for i in [0, 1]:
        t = MYThread(create_wav_txt, (i, ), create_wav_txt.__name__)
        threads.append(t)
        # 启动线程
        threads[i].start()
        # 守护线程， 等待结束
        threads[i].join()

    print("[", start_time, '——————', time.ctime(), "]" + '\n' + 'SUCCESS!!!')


if __name__ == '__main__':
    main()

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-05 22:45
# @Author  : Yu xiang
# @File    : count_all_command_rate.py
# @Company : BEIJING INTENGINE

from time import sleep
from scripts.excel_manual import ExcelManual
from scripts.text_manual import (get_all_file,
                                 get_all_file_path,
                                 read_list_txt,
                                 command_str
                                 )
from scripts.conf_manual import config
from scripts.base_path import COMMANDS_FILE, EXCEL_PATH_2


dir_name = config.get_value('desktop', 'desktop_dir')  # dir_path


if __name__ == "__main__":
    files = get_all_file(dir_name)
    all_files_path = get_all_file_path(dir_name, files)

    all_data = []  # all sheets
    for file in all_files_path:
        # for sheet in ['Sheet1', 'Sheet2']:
        excel = ExcelManual(file, 'Sheet2')
        data = excel.read_data
        all_data.append(data)

    pass_commands = []  # all right_command_list
    fail_commands = []  # all error_command_list
    lost_commands = []  # all lost_command_list
    for i in range(len(all_data)):
        for res in all_data[i]:
            value = res['signel']
            if value == 'Pass':
                pass_commands.append(res['expected_command'])  # reback_command
            elif value == 'Error':
                fail_commands.append(res['expected_command'])
            else:
                lost_commands.append(res['expected_command'])
    sleep(1)
    com = read_list_txt(COMMANDS_FILE)
    set_words = command_str(com)  # 48 commands
    print('Please wait, circulating...')

    sleep(1)
    one_excel = ExcelManual(EXCEL_PATH_2, 'Sheet2')
    print('command ：   count  pass_times  error_times    lost_times       pass_rate     error_rate   lost_rate')
    count = 100
    for i in range(len(set_words)):
        word = set_words[i]
        pass_word = pass_commands.count(word)
        fail_word = fail_commands.count(word)
        lost_word = lost_commands.count(word)
        print(
              word,
              ': ',
              str(100) + '        ' +
              str(pass_word), '           ',
              str(fail_word), '           ',
              str(lost_word), '          ',
              str(round(pass_word / count * 100, 2)), '%       ',
              str(round(fail_word / count * 100, 2)), '%       ',
              str(round(lost_word / count * 100, 2)), '%'
              )
        # write to excel
        one_excel.one_write_data(
                                 i+2,
                                 word,
                                 count,
                                 pass_word,
                                 fail_word,
                                 lost_word,
                                 round(pass_word / count * 100, 2),
                                 round(fail_word / count * 100, 2),
                                 round(lost_word / count * 100, 2)
                                 )

    print('Circulated and wrote finished!!!')

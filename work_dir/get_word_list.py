# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-05 22:45
# @Author  : 余翔
# @File    : get_word_list.py
# @Company : BEIJING INTENGINE

import time
from scripts.base_path import ALL_COMMANDS_TXT_PATH
from scripts.excel_manual import ExcelManual
from scripts.conf_manual import config
import re
from scripts.log_manual import log
from path.test_path import Info
from scripts.text_manual import read_log_to_list, write_txt_once


command_path = config.get_value('excel', 'command_path')
excel = ExcelManual(command_path, '建议北京公司内部采集列表')


if __name__ == '__main__':
    one_time = time.ctime()
    print('starting......')
    data = excel.read_data()
    commands = []  # 59个
    for i in data:
        commands.append(i['命令词'])

    # 打开wav.map，获取相应的信息
    # 文件中需要替换一下字符串
    be_replaced = Info.be_replaced  # to be replaced
    replace_other = Info.replace_else + '\\'

    file_path_name = Info.map_path_name  # map文件路径
    # 生成各个语音文件的txt文件
    all_txt_name = [ALL_COMMANDS_TXT_PATH + '\\' + commands[i] + '.txt' for i in range(len(commands))]

    rows = read_log_to_list(file_path_name)
    for one_row in rows:
        row = one_row.split()
        for i in range(0, len(commands)):
            # for i in range(1):
            if commands[i] == row[2]:
                    final_data = row[1].replace(be_replaced, replace_other)
                    if re.findall('/', final_data):
                        final_data = re.sub('/', r'\\', final_data)
                    write_txt_once(all_txt_name[i], final_data)
                    log.error(final_data)
    print("SUCCESS")
    print(one_time, '   ', time.ctime())

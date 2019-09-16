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
from scripts.text_manual import read_log_to_list, write_txt_once, get_one_key


command_path = config.get_value('excel', 'command_path')
excel = ExcelManual(command_path, '建议北京公司内部采集列表')


if __name__ == '__main__':
    """从.map文件获取命令词的语音"""
    one_time = time.ctime()
    print('starting......')
    data = excel.read_data()
    commands = [v for i in data for v in i.values()]  # 获取命令词

    # 生成各个语音的txt文件
    all_txt_name = [ALL_COMMANDS_TXT_PATH + '\\' + commands[i] + '.txt' for i in range(len(commands))]
    rows = read_log_to_list(Info.map_path_name)  # map文件路径
    for one_row in rows:
        for i in range(0, len(commands)):
            if get_one_key(one_row) == commands[i]:
                    replace_other = Info.replace_else + '\\'
                    wav_url = re.search('/.*\.wav', one_row).group()
                    final_data = wav_url.replace(Info.be_replaced, replace_other)
                    final_data = final_data.replace('/', '\\')
                    write_txt_once(all_txt_name[i], final_data)
                    log.error(final_data)

    print("SUCCESS")
    print(one_time, '   ', time.ctime())

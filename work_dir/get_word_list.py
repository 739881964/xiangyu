# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-05 22:45
# @Author  : 余翔
# @File    : test_login.py
# @Company : BEIJING INTENGINE

import time
from scripts.base_path import ALL_TXT_PATH
from scripts.excel_manual import ExcelManual
from scripts.conf_manual import config
import re
from scripts.log_manual import log


command_path = config.get_value('excel', 'command_path')
excel = ExcelManual(command_path, '建议北京公司内部采集列表')


if __name__ == '__main__':
    print(time.ctime() + '\n' + 'starting......')
    data = excel.read_data()
    commands = []  # 59个
    for i in data:
        commands.append(i['命令词'])

    # 打开wav.map，获取相应的信息
    # 文件中需要替换一下字符串
    src_str = r"/speech_data/wav/"  # to be replaced
    dst_str = r"\\192.168.200.20\backup\Algorithm\speech_data\wav"
    dst_str = dst_str + '\\'

    file_path_name = r'\\192.168.1.12\hftest\project\20190903daxian\doc\wav_test.map'

    L_file_name = []
    l_str_chn_word = commands

    # 生成各个语音文件的txt文件
    for i in range(0, len(l_str_chn_word)):
        L_file_name.append(ALL_TXT_PATH + '\\' + l_str_chn_word[i] + '.txt')

    # make a diary, key is '小优小优' ，value is '小优小优.txt'
    # dic_file_out = {}
    # for i in range(0, len(l_str_chn_word)):
    #     dic_file_out[l_str_chn_word[i]] = L_file_name[i]

    with open(file_path_name, 'r', encoding='utf-8') as fp_in:
        str_file_row_list = fp_in.readlines()

    # open every file and read wav.map.
    # then write info to related file

    for str_row in str_file_row_list:
        l_row_str = str_row.split()
        for i in range(0, len(l_str_chn_word)):
            # for i in range(4):
            if l_str_chn_word[i] == l_row_str[2]:  # f the value is valid
                # file_cur = dic_file_out[l_row_str[2]]
                with open(L_file_name[i], 'a+', encoding='utf-8') as fp_out:
                    str_dst = l_row_str[1].replace(src_str, dst_str)
                    if re.findall('/', str_dst):
                        str_dst = re.sub('/', r'\\', str_dst)
                        fp_out.write(str_dst + '\n')
                        log.error(str_dst)
    print("SUCCESS")
    print(time.ctime())

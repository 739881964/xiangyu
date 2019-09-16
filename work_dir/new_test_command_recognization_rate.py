# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-05 22:45
# @Author  : Yu xiang
# @File    : new_test_command_recognization_rate.py
# @Company : BEIJING INTENGINE

from scripts.text_manual import *
from scripts.base_path import *
from scripts.excel_manual import ExcelManual
from scripts.conf_manual import config
from warnings import simplefilter
from time import sleep
from scripts.log_manual import log


simplefilter(action='ignore', category=FutureWarning)
excel = ExcelManual(EXCEL_PATH, 'Sheet1')


if __name__ == "__main__":
    data = read_rs_trip_data(COMPARE_FILE)  # 获取compare2文件内容——list
    all_command = get_key_word(data)  # 获取所有中文
    need_command = get_all_commands(all_command, 100)  # 获取语音播放需要的命令词，循环100次

    all_count_data = read_rstrip_data(RESULT_LOG)  # 获取result日志的内容-list
    count_data = get_res_count_data(all_count_data)  # 获取需要的日志内容

    require_wav = get_new_wav(data) # 获取音频 5500个
    
    all_start_time = get_start_time_list_str(data)  # 获取compare2音频开始播放的时间—str 5500个
    all_res_time_list = get_time_list(count_data)  # 获取result日志需要的时间列表

    print('Start first read_and_write excel operate ......')
    for i in range(0, len(all_start_time)):  # 循环 5500 times
        for j in range(len(all_res_time_list)):
            start_time = all_start_time[i]
            back_time = all_res_time_list[j]
            end_time = all_start_time[i+1]
            try:
                if end_time > back_time > start_time:
                    key = get_one_key(count_data[j])
                    if key == need_command[i]:
                        excel.write_data(i+2, require_wav[i], start_time, need_command[i], back_time, key, config.get_value('res', 'success_res'))
                    else:
                        excel.write_data(i+2, require_wav[i], start_time, need_command[i], back_time, key, config.get_value('res', 'fail_res'))
                        # log.error('error command is : {} expected command is : {}'.format(need_command[i], key))
            except:
                if back_time > start_time:
                    key = get_one_key(count_data[j])
                    if key == need_command[i]:
                        excel.write_data(i+2, require_wav[i], start_time, need_command[i], back_time, key, config.get_value('res', 'success_res'))
                    else:
                        excel.write_data(i+2, require_wav[i], start_time, need_command[i], back_time, key, config.get_value('res', 'fail_res'))
                        # log.error('error command is : {} expected command is : {}'.format(need_command[i], key))
    print('First write success!!!')
    sleep(1)

    print('Second write to excel ...')
    read_data = excel.read_data()
    for i in range(0, len(read_data)):
        _data = read_data[i]['wav_name']
        _time = all_start_time[i]
        if _data is None:
            excel.write_data(i+2, require_wav[i], all_start_time[i], need_command[i], '', '', config.get_value('res', 'no_res'))
            # log.error('lost command is : {}`'.format(need_command[i]))
    print('Second write success!!!')
    sleep(1)

    print('Start calculate right rate...')
    res_data = excel.read_data()
    count_wake_word = res_data[:200]  # 唤醒词所在的位置
    right = []
    error = []
    null = []
    for i in range(len(count_wake_word)):
        if count_wake_word[i]['reback_command'] == '森歌森歌' or count_wake_word[i]['reback_command'] == '达显达显':
            right.append(count_wake_word[i]['reback_command'])
        elif count_wake_word[i]['reback_command'] == '':
            null.append('lost')
        else:
            error.append(count_wake_word[i]['reback_command'])
    re_right = []
    re_error = []
    re__null = []
    else_list = []
    for k in res_data:
        if k not in count_wake_word:
            else_list.append(k)
    for j in range(len(else_list)):
        if else_list[j]['signel'] == 'Pass':
            re_right.append(1)
        elif else_list[j]['signel'] == 'Error':
            re_error.append(2)
        else:
            re__null.append(3)
    awake_rate = len(right) / 200 * 100  # 唤醒率
    recognition_rate = len(re_right) / 5300 * 100  # 识别率
    false_recognition = len(re_error) / 5300 * 100  # 错误率
    un_recognition_rate = len(re__null) / 5300 * 100  # 未识别率
    print('count end！result is：')
    print(
          '唤醒:', 200, ' R:', len(right), ' E:', len(error), ' L:', len(null),
          '\n识别:', 5300, ' R:', len(re_right), ' E:', len(re_error), ' L:', len(re__null),
          '\n唤醒率是: %.2f' % awake_rate + '%',
          '\n识别率是: %.2f' % recognition_rate + '%',
          '\n误识率是: %.2f' % false_recognition + '%',
          '\n未识别率是: %.2f' % un_recognition_rate + '%'
          )

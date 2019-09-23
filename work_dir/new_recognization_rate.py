# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-15 22:45
# @Author  : Yu xiang
# @File    : new_recognization_rate.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE

import time
import pandas as pd
from path.excel_environment import Params
from scripts.text_manual import read_rs_trip_data, get_all_commands, get_key_word, get_start_time_list_str, read_rstrip_data, get_new_wav, count_run_time
from scripts.base_path import COMPARE_FILE, RESULT_LOG, EXCEL_PATH
from scripts.excel_manual import ExcelManual
from scripts.conf_manual import config
from warnings import simplefilter
from time import sleep
from scripts.log_manual import log
from scripts.pandas_manual import write_data, excel_add_sheet
simplefilter(action='ignore', category=FutureWarning)


# excel = ExcelManual(EXCEL_PATH, 'Sheet1')


@count_run_time
def operation(res_len):
    print('Start first read_and_write excel operate ......')
    case_id = list(range(1, len(res_len)))
    wav_name = []
    start_time = []
    expected_command = []
    reback_time = []
    reback_command = []
    signel = []
    for i in range(0, len(all_start_time)):  # 循环 5500 times
        for j in range(len(all_res_list)):
            key = all_res_list[j].split()[-1]  # get命令词
            # key = get_one_key(count_data[j])
            time = all_res_list[j][1:24]
            try:
                if all_start_time[i+1] > time > all_start_time[i]:
                    if key == need_command[i]:
                        wav_name.append(require_wav[i])
                        start_time.append(all_start_time[i])
                        expected_command.append(need_command[i])
                        reback_time.append(time)
                        reback_command.append(key)
                        signel.append('pass')
                        # print(f'正确的命令词: {key}')
                    else:
                        wav_name.append(require_wav[i])
                        start_time.append(all_start_time[i])
                        expected_command.append(need_command[i])
                        reback_time.append(time)
                        reback_command.append(key)
                        signel.append('fail')
                        print(f'错误的命令词: {key}')
                        # log.error('error command is : {} expected command is : {}'.format(need_command[i], key))
            except:
                if i == len(all_start_time) - 1:
                    if time > all_start_time[i]:
                        if key == need_command[i]:
                            wav_name.append(require_wav[i])
                            start_time.append(all_start_time[i])
                            expected_command.append(need_command[i])
                            reback_time.append(time)
                            reback_command.append(key)
                            signel.append('pass')
                            # print(f'正确的命令词: {key}')
                        else:
                            wav_name.append(require_wav[i])
                            start_time.append(all_start_time[i])
                            expected_command.append(need_command[i])
                            reback_time.append(time)
                            reback_command.append(key)
                            signel.append('fail')
                            print(f'错误的命令词: {key}')
    dic = {
        'case_id': case_id,
        'wav_name': wav_name,
        'start_time': start_time,
        'expected_command': expected_command,
        'reback_time': reback_time,
        'reback_command': reback_command,
        'signel': signel
    }
    excel_add_sheet(dic, EXCEL_PATH, 'Sheet1')
    print('successful!!!')


@count_run_time
def compare_wav_com(com, wav):
    _dic = {
        'commands': com,
        'wav_name': wav
    }
    excel_add_sheet(_dic, EXCEL_PATH, 'Sheet2')
    print('successful')


if __name__ == "__main__":
    data = read_rs_trip_data(COMPARE_FILE)  # 获取compare2文件内容——list
    all_command = get_key_word(data)  # 获取所有中文
    need_command = get_all_commands(all_command, 100)  # 获取语音播放需要的命令词，循环100次 .........
    # all_count_data = read_rstrip_data(RESULT_LOG)  # 获取result日志的内容-list
    # count_data = get_res_count_data(all_count_data)  # 获取需要的日志内容
    require_wav = get_new_wav(data)  # 获取音频 5500个
    all_start_time = get_start_time_list_str(data)  # 获取compare2音频开始播放的时间—str 5500个
    # all_res_time_list = get_time_list(count_data)  # 获取result日志需要的时间列表
    all_res_list = read_rstrip_data(RESULT_LOG)[8::2]  # result.log need_content_list ........

    # 写入excel，执行operation方法
    compare_wav_com(need_command, require_wav)
    time.sleep(0.5)
    operation(all_res_list)

    # header = ['case_id', 'wav_name', 'start_time', 'expected_command', 'reback_time', 'reback_command', 'signel']
    # 写入的数据必须是 DataFrame形式，可以使list。也可是dic
    # df_1 = pd.DataFrame(
    #         {
    #             'case_id': case_id,
    #             'wav_name': wav_name,
    #             'start_time': start_time,
    #             'expected_command': expected_command,
    #             'reback_time': reback_time,
    #             'reback_command': reback_command,
    #             'signel': signel
    #         }
    #     )
    # writer = pd.ExcelWriter(EXCEL_PATH)  # excel path
    # df_1.to_excel(excel_writer=writer, sheet_name='Sheet1', index=False)
    # writer.save()

    # sleep(0.5)
    #
    # print('Second write to excel ...')
    # read_data = excel.read_data()
    # for i in range(0, len(read_data)):
    #     _data = read_data[i]['wav_name']
    #     _time = all_start_time[i]
    #     if _data is None:
    #         excel.write_data(i+2,
    #                          require_wav[i],
    #                          all_start_time[i],
    #                          need_command[i],
    #                          '',
    #                          '',
    #                          'Lost'
    #                          )
    #         # log.error('lost command is : {}`'.format(need_command[i]))
    #         print(f'未识别的命令词: {need_command[i]}')
    # print('Second write success!!!')
    # sleep(0.5)
    #
    # print('Start calculate right rate...')
    # res_data = excel.read_data()
    # count_wake_word = res_data[:200]  # 唤醒词所在的位置
    # right = []
    # error = []
    # null = []
    # awake_command = ['森歌森歌', '达显达显']
    # for i in range(len(count_wake_word)):
    #     if count_wake_word[i]['reback_command'] in awake_command:
    #         right.append(count_wake_word[i]['reback_command'])
    #     elif count_wake_word[i]['reback_command'] == '':
    #         null.append('lost')
    #     else:
    #         error.append(count_wake_word[i]['reback_command'])
    #
    # re_right = []
    # re_error = []
    # re__null = []
    # else_list = []
    # for k in res_data:
    #     if k not in count_wake_word:
    #         else_list.append(k)
    # for j in range(len(else_list)):
    #     if else_list[j]['signel'] == 'Pass':
    #         re_right.append(1)
    #     elif else_list[j]['signel'] == 'Error':
    #         re_error.append(2)
    #     else:
    #         re__null.append(3)
    # command_count_time, awake_time = 5300, 200
    # awake_rate = len(right) / awake_time * 100  # 唤醒率
    # recognition_rate = len(re_right) / command_count_time * 100  # 识别率
    # false_recognition = len(re_error) / command_count_time * 100  # 错误率
    # un_recognition_rate = len(re__null) / command_count_time * 100  # 未识别率
    # print('Count end！result is：')
    # print(
    #       '唤醒:', 200, ' R:', len(right), ' E:', len(error), ' L:', len(null),
    #       '\n识别:', command_count_time, ' R:', len(re_right), ' E:', len(re_error), ' L:', len(re__null),
    #       '\n唤醒率是: %.2f' % awake_rate + '%',
    #       '\n识别率是: %.2f' % recognition_rate + '%',
    #       '\n误识率是: %.2f' % false_recognition + '%',
    #       '\n未识别率是: %.2f' % un_recognition_rate + '%'
    #       )
    # print('Finished')

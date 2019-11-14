# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 11:16
# @Author  : Xiang Yu
# @File    : broadcast_wav.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


import os
import random
from time import sleep

from playsound import playsound
from scripts.pandas_manual import PandasManual
from scripts.text_manual import write_txt_once, read_rs_trip_data


# write_path = r'C:\Users\hftest1\Desktop\wav'
# write_file = r'C:\Users\xiangyu\Desktop\多联41-60-new\1-20男'
# error_txt_path = r'C:\Users\xiangyu\Desktop\error_wav.txt'
# result_excel_path = r'D:\大黑板.xlsx'

# error_txt_path = r'C:\Users\xiangyu\Desktop\error_wav.txt'
# result_txt_path = r'C:\Users\xiangyu\Desktop\餐厅灯wav'

# result_excel_path = r'C:\Users\xiangyu\Desktop\61-120\打开餐厅灯.txt'

# panda = PandasManual(result_excel_path)
# _data = panda.get_data('loss_info')
# all_file = os.listdir(result_txt_path)
# print(all_file)


def broadcast_wav():
    """ 按顺序播放 """
    # loss_wav = _data['wav_name'].tolist()
    loss_wav = read_rs_trip_data(r'C:\Users\xiangyu\Desktop\打开餐厅灯.txt')
    # file = all_file[0]
    # _data = read_rs_trip_data(os.path.join(result_txt_path, file))
    # loss_wav = _data  # [::-1]
    for wav in loss_wav:
        # if 'SPEAK' not in wav:
        # wav = os.path.join(r'C:\Download\wav', wav.split('\\')[-1])
        playsound(wav)
        # sleep(1)
        while True:
            result = input('请输入播放结果: ')
            try:
                if int(result) != 1:
                    pass
                else:
                    # wav = wav.split('\\')[-1]
                    # write_txt_once(os.path.join(write_file, file), os.path.join(write_path, wav))
                    print(wav)
                break
            except:
                print('请输入合法的结果！')


broadcast_wav()


# def broadcast_wav():
#     """ 随机播放 """
#     loss_wav = data['wav_name'].tolist()
#
#     length = len(loss_wav)
#     while True:
#         wav = loss_wav[random.randint(0, length)]
#         playsound(wav)
#
#         while True:
#             result = input('请输入播放结果: ')
#             try:
#                 if int(result) == 1:
#                     pass
#                 else:
#                     write_txt_once(error_txt_path, wav)
#                     print(wav)
#                 break
#             except:
#                 print('请输入合法的结果！')


# from pydub import AudioSegment
# from pydub.playback import play
#
#
# song = AudioSegment.from_wav(r'\\192.168.1.12\hftest\hfwav\tongyongduolian2\TJ0010232@TJ0010232B03_9.wav')
# play(song)


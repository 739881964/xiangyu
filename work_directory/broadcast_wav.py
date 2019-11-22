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


def read_rs_trip_data(file_name):
    """abandon \n from data to list"""
    try:
        with open(file_name, 'r', encoding='gbk') as f:
            data = list(map(lambda line: line.rstrip('\n'), f.readlines()))
    except:
        with open(file_name, 'r', encoding='utf-8') as f:
            data = list(map(lambda line: line.rstrip('\n'), f.readlines()))

    return data


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


# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 16:31
# @Author  : Xiang Yu
# @File    : download_wav_from_server.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


import os
import sys

from scripts.text_manual import get_all_file_path, read_rs_trip_data
from functools import reduce


server_path = r'\\192.168.200.20\backup\Algorithm\speech_data\wav\large'
local_word_txt_path = r'D:\dl_wl'


all_txt_name = os.listdir(local_word_txt_path)  # command txt name
all_txt_path = get_all_file_path(local_word_txt_path, all_txt_name)  # command txt path

all_content = list(map(read_rs_trip_data, all_txt_path))
add_together_data = reduce(lambda x, y: x + y, all_content)  # get all wav path

all_wav_name = list(map(lambda x: x.split('\\')[-1], add_together_data))  # get all wav name


def find_wav_path(dir_path: str, wav: '音 频'):
    # __path__ = list()
    all_file = os.listdir(dir_path)
    for file in all_file:
        wav_file_path = os.path.join(dir_path, file)
        print(wav_file_path)
        if os.path.isdir(wav_file_path):
            if file == 'wav':
                one_all_file = os.listdir(wav_file_path)
                print(file)
                for one_file in one_all_file:
                    print(one_file)
                    one_file_path = os.path.join(wav_file_path, one_file)
                    if os.path.isfile(one_file_path):  # wav下面是文件就停止
                        one = os.path.join(one_file_path, wav)
                        if os.path.exists(one):
                            print(one)
                            sys.exit()
                    elif os.path.isdir(one_file_path):  # wav下面是目录继续遍历
                        beyond_wav_dir = os.listdir(one_file_path)
                        for wav_dir in beyond_wav_dir:
                            wav_dir_path = os.path.join(one_file_path, wav_dir)
                            one = os.path.join(wav_dir_path, wav)
                            if os.path.exists(one):
                                print(one)
                                sys.exit()
            else:
                find_wav_path(wav_file_path, wav)


# for k, v in enumerate(all_wav_name):
#     if v == 'SPEAKERAS0158@0158C0283.wav':
#         print(k)

one_wav = all_wav_name[216]
find_wav_path(server_path, one_wav)


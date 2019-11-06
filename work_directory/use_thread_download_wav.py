# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/11 9:37
# @Author  : Xiang Yu
# @File    : use_thread_download_wav.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


# copy wav to my local directory


import shutil
import os
# import gevent
from scripts.text_manual import run_time, read_rs_trip_data

from concurrent.futures import ThreadPoolExecutor
# from gevent import monkey; monkey.patch_all()


before_path = r'C:\Users\xiangyu\Desktop\3\打开餐厅灯.txt'
# after_path = r'\\192.168.1.12\hftest\hfwav\tongyongduolian'
after_path = r'C:\Users\xiangyu\Desktop\cantingdeng'
wav_name_list = read_rs_trip_data(before_path)  # os.listdir(before_path)


def download_wav(i):
    one_wav = wav_name_list[i]
    # one_wav_path = os.path.join(before_path, one_wav)
    # copy to a new wav path
    wav_name = one_wav.split('\\')[-1]
    new_wav_path = os.path.join(after_path, wav_name)

    try:
        shutil.copyfile(one_wav, new_wav_path)
        # print('{} copy successful}'.format(one_wav_path))
    except FileNotFoundError as e:
        raise e


@run_time()
def main():
    with ThreadPoolExecutor(max_workers=len(wav_name_list)) as pool:
        for i in range(len(wav_name_list)):
            pool.map(download_wav, [i])


# gevent.joinall(list(map(lambda x: gevent.spawn(download_wav, x), range(len(wav_name_list)))))


main()


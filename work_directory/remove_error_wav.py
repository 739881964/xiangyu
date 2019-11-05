# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 13:55
# @Author  : Xiang Yu
# @File    : remove_error_wav.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


""" 删除 word_list error 语音 """


import os
from scripts.text_manual import read_rs_trip_data, run_time
from concurrent.futures.thread import ThreadPoolExecutor


src_path = r'C:\Users\xiangyu\Desktop\1-60'
error_txt_path = r'C:\Users\xiangyu\Desktop\error_wav.txt'


src_txt_files = os.listdir(src_path)
src_txt_file_path = list(map(lambda x: os.path.join(src_path, x), src_txt_files))


def remove_wav_path(i):
    src_txt_content = read_rs_trip_data(src_txt_file_path[i])
    error_txt_content = read_rs_trip_data(error_txt_path)

    new_path = os.path.join(src_path, f'{i}.txt')
    with open(new_path, 'a+', encoding='utf-8') as f:
        for data in src_txt_content:
            if data not in error_txt_content:
                f.write(data + '\n')

    re_name = os.path.join(src_path, f'new{i}.txt')
    os.rename(src_txt_file_path[i], re_name)
    os.rename(new_path, src_txt_file_path[i])
    os.remove(re_name)


@run_time()
def main():
    with ThreadPoolExecutor(max_workers=len(src_txt_files)) as pool:
        for i in range(len(src_txt_files)):
            # map中的参数为可迭代-iterable
            pool.map(remove_wav_path, [i])


if __name__ == "__main__":
    main()


# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 16:03
# @Author  : Xiang Yu
# @File    : remove_speak_wav.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


""" 删除word_list 包含SPEAKER的语音 """


import os
from scripts.text_manual import read_rs_trip_data, run_time
from concurrent.futures.thread import ThreadPoolExecutor


# src_path = r'C:\Users\xiangyu\Desktop\duolian _list1_60'
src_path = r'C:\Users\xiangyu\Desktop\duolian_list61_120'
# to_be_replace = r'C:\Users\xiangyu\Desktop\duolian _list1_60'

src_txt_files = os.listdir(src_path)
src_txt_file_path = list(map(lambda x: os.path.join(src_path, x), src_txt_files))

# re_txt_files = os.listdir(to_be_replace)
# re_txt_file_path = list(map(lambda x: os.path.join(to_be_replace, x), re_txt_files))


def remove_wav_path(i):
    src_txt_content = read_rs_trip_data(src_txt_file_path[i])
    # re_txt_content = read_rs_trip_data(re_txt_file_path)

    new_path = os.path.join(src_path, f'{i}.txt')
    with open(new_path, 'a+', encoding='utf8') as f:
        for data in src_txt_content:
            if 'SPEAK' not in data:
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


# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/25 16:57
# @Author  : Xiang Yu
# @File    : replace_url_to local.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


""" txt音频地址替换为本地音频的播放地址 """


import os
from concurrent.futures.thread import ThreadPoolExecutor

from path.test_path import Info
from scripts.text_manual import (get_all_file,
                                 get_all_file_path,
                                 read_rs_trip_data,
                                 write_txt_once,
                                 remove_txt,
                                 run_time
                                 )


base_path = r'C:\Users\xiangyu\Desktop\new_list'
local_path = r'C:\Users\hftest1\Desktop\wav'
old_path = r'C:\Users\xiangyu\Desktop\new_word_file\new_word_list'


old_file_name = get_all_file(old_path)
old_file_path = get_all_file_path(old_path, old_file_name)
new_file_path = get_all_file_path(base_path, old_file_name)

# for i in range(len(old_file_name)):


def replace_url(i):
    content = read_rs_trip_data(old_file_path[i])
    for one_content in content:
        data = one_content.split('\\')[-1]
        wav_path = os.path.join(local_path, data)
        write_txt_once(new_file_path[i], wav_path)


@run_time()
def main():
    with ThreadPoolExecutor(max_workers=58) as pool:
        for i in range(len(old_file_name)):
            pool.map(replace_url, [i])


if __name__ == "__main__":
    try:
        if not os.path.exists(base_path):
            os.mkdir(base_path)
        else:
            remove_txt(base_path)
    except:
        pass

    main()


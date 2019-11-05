# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 17:12
# @Author  : Xiang Yu
# @File    : replace_path_to_txt.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


import os
from scripts.text_manual import read_rs_trip_data, run_time, write_txt_once
from concurrent.futures.thread import ThreadPoolExecutor


src_path = r'C:\Users\xiangyu\Desktop\duolian_list61_120'
to_be_replace = r'C:\Users\xiangyu\Desktop\duolian _list1_60'

src_txt_files = os.listdir(src_path)
src_txt_file_path = list(map(lambda x: os.path.join(src_path, x), src_txt_files))

re_txt_files = os.listdir(to_be_replace)
re_txt_file_path = list(map(lambda x: os.path.join(to_be_replace, x), re_txt_files))


def replace_path(i):
    src_txt_content = read_rs_trip_data(src_txt_file_path[i])
    re_txt_content = read_rs_trip_data(re_txt_file_path[i])

    # num = 0
    for data in re_txt_content:
        txt_len = len(src_txt_content)
        if (txt_len < 60) or (60 < txt_len < 180):
            write_txt_once(src_txt_file_path[i], data)
            new_txt_len = len(read_rs_trip_data(src_txt_file_path[i]))
            if (new_txt_len == 60) or (new_txt_len == 180):
                break

    # while (txt_len < 60) or (60 < txt_len < 180):
    #     write_txt_once(src_txt_file_path[i], re_txt_content[num])
    #     num += 1
    #     new_txt_len = len(read_rs_trip_data(src_txt_file_path[i]))
    #     if (new_txt_len == 60) or (txt_len == 180):
    #         break


@run_time()
def main():
    with ThreadPoolExecutor(max_workers=len(src_txt_files)) as pool:
        for i in range(len(src_txt_files)):
            # map中的参数为可迭代-iterable
            pool.map(replace_path, [i])


if __name__ == "__main__":
    main()


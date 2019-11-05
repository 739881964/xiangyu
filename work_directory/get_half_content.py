# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/27 14:20
# @Author  : Xiang Yu
# @File    : get_half_content.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


""" word_list 对半储存 """


import os

from concurrent.futures.thread import ThreadPoolExecutor
from scripts.text_manual import read_rs_trip_data, get_all_file_path, write_txt_once, run_time


base_path = r'C:\Users\xiangyu\Desktop\new_list'
new_path = r'C:\Users\xiangyu\Desktop\61-120'
# new_path = r'\\192.168.1.12\hftest\project\20191010tongyongduolian\doc\duolian_list61_120'

all_txt = os.listdir(base_path)
all_old_file_path = get_all_file_path(base_path, all_txt)
all_new_file_path = get_all_file_path(new_path, all_txt)


# for one_path in all_old_file_path:
def get_half(i):
    before_content = read_rs_trip_data(all_old_file_path[i])[::-1]

    for data in before_content:
        write_txt_once(all_new_file_path[i], data)
        after_content = read_rs_trip_data(all_new_file_path[i])
        if len(after_content) == len(before_content) // 2:
            break


@run_time()
def main():
    with ThreadPoolExecutor(max_workers=len(all_txt)) as pool:
        for i in range(len(all_txt)):
            # map中的参数为可迭代-iterable
            pool.map(get_half, [i])


if __name__ == '__main__':
    main()


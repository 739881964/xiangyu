# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/4 9:56
# @Author  : Xiang Yu
# @File    : modify_log_time.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


import os
import re
from datetime import datetime


class ModifyTime:

    def __init__(self, path):
        self.path = path

    @classmethod
    def get_time(cls, data):
        """ 将字符串类型的时间转换成datetime格式"""
        return datetime.strptime(data, "%Y-%m-%d %H:%M:%S")

    def read_rs_trip_data(self):
        """ 读取log文件，结果为list """
        try:
            with open(self.path, 'r', encoding='gbk') as f:
                data = list(map(lambda line: line.rstrip('\n'), f.readlines()))
        except:
            with open(self.path, 'r', encoding='utf8') as f:
                data = list(map(lambda line: line.rstrip('\n'), f.readlines()))

        return data

    @staticmethod
    def write_txt_once(file_name, data):
        """ 写入数据到文件 """
        with open(file_name, 'a+', encoding='utf8') as f:
            f.write(data + '\n')

    def get_new_file_name(self):
        """ 创建新生成日志名称 """
        name = self.path.split('\\')[-1]
        new_file_name = self.path.replace(name, '_'.join(['new', name]))
        if os.path.exists(new_file_name):
            os.remove(new_file_name)

        return new_file_name

    def modify_time(self):
        """ 修改识别的时间，从00:00:00开始 """
        pattern = re.compile('\[.*?\]')
        new_file = self.get_new_file_name()
        content = self.read_rs_trip_data()
        start_time = list(filter(lambda x: x if x.endswith('>') else False, content))[0]
        first_time = re.split("\[|\.", start_time)[1]  # 最开始时间
        # print(first_time)
        base_time = '00:00:00'
        with open(new_file, 'a+') as f:
            for _ in range(len(content)):
                data = content[_]
                if 'SpottingWordList' in data:
                    # date_time = re.search(pattern, data).group(0)
                    date_time = re.split('\[|\.', data)[1]
                    self_time = self.get_time(date_time) - self.get_time(first_time)
                    final_data = pattern.sub(f'[{str(self_time)}]', data, count=1)
                    f.write(final_data + '\n')
                    # print(final_data)
                elif data.endswith('>'):
                    final_data = pattern.sub(f'[{base_time}]', data)
                    # print(final_data)
                    f.write(final_data + '\n')
                elif data.endswith('] '):
                    date_time = re.split('\[|\.', data)[1]
                    self_time = self.get_time(date_time) - self.get_time(first_time)
                    final_data = pattern.sub(f'[{str(self_time)}]', data, count=1)
                    f.write(final_data + '\n')
                else:
                    f.write(data + '\n')


# 传入log文件路径
file_path = 'D:\\slaver_board_62_gain_12_COM18_2019.10.11-17.36.49.log'
modify = ModifyTime(file_path)
modify.modify_time()


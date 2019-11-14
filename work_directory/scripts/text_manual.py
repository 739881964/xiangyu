#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-05 22:45
# @Author  : Yu xiang
# @File    : text_manual.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


"""对文件操作，处理封装的方法"""

import time
import os
import yaml
import re

from datetime import datetime, timedelta
from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)


def read_yml(file_path: str) -> dict:
    """ 读取配置文件yaml中的数据 """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = yaml.load(f, Loader=yaml.FullLoader)

    return content


def if_in_func(data: list) -> list:
    """获取compare时间列表，根据 '[' or ']' 判断"""
    time_list = list(map(lambda y: y[1:-1], list(filter(lambda x: '[' in x, data))))

    return time_list


def read_list_txt(file_name: str) -> list:
    """get txt content to list"""
    with open(file_name, 'r', encoding='gbk') as f:  # encoding='utf-8'
        lines = f.readlines()

    return lines


def read_str_txt(file_name):
    """get txt content to str"""
    with open(file_name, 'r', encoding='gbk') as f:  # encoding='utf-8'
        lines = f.read()

    return lines


def read_log_file_str(file_name):
    """read log file"""
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()

    return text


def read_log_to_list(file_name):
    """read log file"""
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.readlines()

    return text


def read_rstrip_data(file_name):
    """abandon \n from data to list"""
    try:
        with open(file_name, 'r', encoding='gbk') as f:
            data = list(map(lambda line: line.rstrip('\n'), f.readlines()))
    except:
        with open(file_name, 'r', encoding='utf-8') as f:
            data = list(map(lambda line: line.rstrip('\n'), f.readlines()))

    return data


def read_rs_trip_data(file_name):
    """abandon \n from data to list"""
    try:
        with open(file_name, 'r', encoding='gbk') as f:
            data = list(map(lambda line: line.rstrip('\n'), f.readlines()))
    except:
        with open(file_name, 'r', encoding='utf-8') as f:
            data = list(map(lambda line: line.rstrip('\n'), f.readlines()))

    return data


def get_split_zh(a_list):
    """获取字符串第一个中文词"""
    res = list(map(lambda x: x.split()[0], a_list))

    return res


def get_one_zh(data):
    return data.split()[-1]


def get_one_time(data):
    return data.split()[0][1:-1]


def write_txt_once(file_path, data):
    """write to txt once """
    with open(file_path, 'a+', encoding='utf-8') as f:
        f.write(data + '\n')


def write_txt_one_more(file_path, data, int_num):
    """write content to txt more times"""
    with open(file_path, 'a+', encoding='utf-8') as f:
        for i in range(int_num):
            f.write(data + '\n')


def get_zh(str):
    """get Chinese from str and duplicate removal"""
    res = re.findall('[\u4e00-\u9fa5]+', str)
    # des_res = list(filter(lambda x: True if x not in list() else False, res))
    des_res = list()
    for i in res:
        if i not in des_res:
            des_res.append(i)

    return des_res


def get_one_key(str):
    """get Chinese"""
    res = re.compile('[\u4e00-\u9fa5]+')
    if res.findall(str):
        return res.findall(str)[0]


def _get_key(st):
    """get Chinese"""
    res = re.findall('[\u4e00-\u9fa5]+', st)
    if res:
        return res[0]


def count_times(file_path, text, data):
    """circulate word appear times"""
    for word in data:
        try:
            res = word + 'appear times is : ' + str(text.count(word)) + '次'
            write_txt_once(file_path, res)
            print(res)
        except Exception as e:
            res = f'Search word: {word} not exist'
            write_txt_once(file_path, res)
            print(e)


def command_str(data: list) -> list:
    commands = list(map(lambda x: x.replace('\n', ''), data))

    return commands


def get_command(data: list, n: int) -> list:
    commands = list(map(lambda x: n * x.replace('\n', ''), data))

    return commands


def get_time_list(data) -> list:
    a_list = list()
    pattern = re.compile('[[](.*?)[]]')
    for one_data in data:
        res = pattern.findall(one_data)[0]
        a_list.append(res)

    return a_list


def get_key(data, _time):
    """find command depend on time"""
    for i in data:
        if _time in i:
            key = get_zh(i)
            return key


def get_key_word(data) -> list:
    """get command depend on list"""
    keys = list()
    for i in data:
        if get_zh(i):
            key_word = get_zh(i)
            keys.append(key_word[0])

    return keys


def get_all_commands(a_list, n) -> list:
    _set = list()
    for i in a_list:
        if i not in _set:
            _set.append(i)
    command_list = []
    for k in _set:
        for j in range(n):
            command_list.append(k)

    return command_list


def get_all_word(file_path) -> list:
    """获取命令词"""
    data = read_rs_trip_data(file_path)
    all_word = get_split_zh(data)

    return all_word


def get_all_command_times(a_list):
    # 统计每个命令次出现的次数-list
    one_list = []
    for i in a_list:
        if i not in one_list:
            one_list.append(i)

    times = list(map(a_list.count, one_list))

    return one_list, times


def get_time(data):
    """return wav datetime"""
    return datetime.strptime(data, "%Y-%m-%d %H:%M:%S")


def get_str_time(data):
    """get str-list"""
    return data.strftime('%Y-%m-%d %H:%M:%S')


# def get_start_time_list(data):
#     """return wav broadcast start_time"""
#     start_time_list = list()
#     pattern = re.compile('[[](.*)[.]')
#     for i in data:
#         if ('IET' and 'wav') in i:
#             start_time = pattern.findall(i)[0][0:23]
#             start_time_list.append(start_time)
#         elif ('IET' not in i) and ('wav' in i):
#             start_time = pattern.findall(i)[0]
#             start_time_list.append(start_time)
#
#     return start_time_list


def get_start_time_list(data):
    """return wav broadcast start_time"""
    start_time_list = list()
    pattern = re.compile('[[](.*)[.]')
    for i in range(len(data)):
        one_data = data[i]
        if pattern.findall(one_data):
            if ('IET' and 'wav') in one_data:
                res = pattern.findall(one_data)
                start_time_list.append(res[0][0:23])
        elif ('IET' not in one_data) and ('wav' in one_data):
            start_time_list.append(data[i-1][1:-2])

    return start_time_list


def get_actual_time(one_time):
    """return wav broadcast start_time add five s"""
    return one_time + timedelta(minutes=1/12)  # +5秒


def get_res_count_data(data):
    """get Chinese depend on data where from slaver_board.log """
    _count_data = list()
    pattern = re.compile('[\u4e00-\u9fa5]+')
    for i in data:  # i is str
        # __data = re.findall('[\u4e00-\u9fa5]+', i)
        if pattern.findall(i):
            _count_data.append(i)

    return _count_data


def get_every_command_times(data):
    """get Chinese depend on data where from slaver_board.log """
    count_data = list()
    pattern = re.compile('[\u4e00-\u9fa5]+')
    for i in data:  # i is str
        res = pattern.findall(i)
        if res and 'NO' not in i:
            count_data.append(res[0])

    return count_data


def get_last_wav(data):
    """get 240 wav"""
    wav_list = list()
    for i in data:
        if re.findall('^D(.*?)wav$', i):
            res = re.findall('^D(.*?)wav$', i)
            resp = 'D' + res[0] + 'wav'
            wav_list.append(resp)

    get_wav = list()  # get where circulate wav n times
    for i in range(len(wav_list)):
        if i % 2 == 0:
            get_wav.append(wav_list[i])

    last_wav = list()
    for i in get_wav:
        if not re.findall('55.wav', i):
            last_wav.append(i)

    return last_wav


def get_new_wav(data):
    wav_list = list()
    pattern = re.compile(r'\\\\.*\.wav')
    for i in data:
        if pattern.findall(i):
            res = pattern.findall(i)[0]
            # resp = 'D' + res + 'wav'
            wav_list.append(res)

    return wav_list


def get_all_time(data, n):
    """abandon time, if n, return n, else filter then return n time_list"""
    if len(data) == n:  # 可以再优化
        return data
    else:
        five_time = data[12::49]
        all_start_time_list = list()
        for i in data:
            if i not in five_time:
                all_start_time_list.append(i)  # n

    return all_start_time_list


def run_time(num: int = 0):
    """calculate run count time"""
    def count_run_time(func):
        def run(*args, **kw):
            one_time = time.perf_counter()
            res = func(*args, **kw)
            spent_time = time.perf_counter() - one_time
            if spent_time > num:
                print('执行时间为: %.2f 秒' % spent_time)
            return res
        return run
    return count_run_time


def get_all_file(file_path):
    """get all files from file_path"""
    all_file = os.listdir(file_path)

    return all_file


def get_all_file_path(dir_path, files):
    """join and get all file path"""
    all_file_path = list(map(lambda x: os.path.join(dir_path, x), files))

    return all_file_path


def get_wav_name(file_name):
    """get wav name """
    wav_list = list()
    with open(file_name, 'r', encoding='utf-8') as f:
        line = f.readlines()
        for i in line:
            if '\n' == i:
                continue
            else:
                j = i.strip('\r\n')
                wav_list.append(j)

    return wav_list


def get_all_command(data, n, awake_times, else_times):
    count_time = list()
    for i in data:
        if i in data[:n]:
            for j in range(awake_times):
                count_time.append(i)
        else:
            for j in range(else_times):
                count_time.append(i)

    return count_time


def remove_txt(file_path):
    """
    删除 file_path 下的txt文件，递归
    """
    all_file = os.listdir(file_path)
    for file in all_file:
        one_file_path = os.path.join(file_path, file)
        if os.path.isfile(one_file_path):
            if os.path.splitext(one_file_path)[1] == '.txt':
                os.remove(one_file_path)
        else:
            remove_txt(one_file_path)


if __name__ == "__main__":
    one_list = [1, 1, 3, 3, 5, 6, 7, 8, 10, 10, 10]
    print(get_all_command_times(one_list))


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-05 22:45
# @Author  : Yu xiang
# @File    : test_login.py

import re
from datetime import datetime, timedelta
from warnings import simplefilter
import time
import os
from scripts.base_path import COMMAND_WRITE_FILE_PATH
simplefilter(action='ignore', category=FutureWarning)


def read_list_txt(file_name):
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
    data = []
    for line in open(file_name, encoding='gbk'):
        res = line.rstrip('\n')
        data.append(res)
    return data


def read_rs_trip_data(file_name):
    """abandon \n from data to list"""
    data = []
    for line in open(file_name, encoding='utf-8'):
        res = line.rstrip('\n')
        data.append(res)
    return data


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
    des_res = []
    res = re.findall('[\u4e00-\u9fa5]+', str)
    for i in res:
        if i not in des_res:
            des_res.append(i)
    return des_res


def get_one_key(str):
    """get Chinese"""
    res = re.findall('[\u4e00-\u9fa5]+', str)[0]
    return res


def count_times(text, data):
    """circulate word appear times"""
    for word in data:
        try:
            res = word + 'appear times is : ' + str(text.count(word)) + '次'
            write_txt_once(COMMAND_WRITE_FILE_PATH, res)
            print(res)
        except:
            res = f'Search word: {word} not exist'
            write_txt_once(COMMAND_WRITE_FILE_PATH, res)


def command_str(data):
    commands = []  # get commands
    for i in data:
        res = i.replace('\n', '')
        commands.append(res)
    return commands


def get_command(data, n):
    commands = []  # get commands * n
    for i in data:
        res = i.replace('\n', '')
        commands.append(res)
    five_commands = n * commands
    return five_commands


def get_time_list(data):
    time_list = []  # get time set
    for i in data:
        all_time = re.findall('[[](.*)[.]', i)
        time_list.append(all_time[0])
    return time_list


def get_key(data, time):
    """find command depend on time"""
    for i in data:
        if time in i:
            key = get_zh(i)
            return key


def get_key_word(data):
    """get command depend on list"""
    keys = []
    for i in data:
        key_word = get_zh(i)
        keys.append(key_word[0])
    return keys


def get_time(data):
    """return wav datetime"""
    return datetime.strptime(data, "%Y-%m-%d %H:%M:%S")


def get_str_time(data):
    """get str-list"""
    return data.strftime('%Y-%m-%d %H:%M:%S')


def get_start_time_list(data):  # datetime-list
    """return wav broadcast start_time"""
    start_time_list = []
    for i in data:
        # time = compare_data[2::5][0]
        start_time_str = re.findall('[[](.*)[.]', i)[0]
        start_time = get_time(start_time_str)
        start_time_list.append(start_time)
    return start_time_list


def get_start_time_list_str(data):  # str-list
    """return wav broadcast start_time"""
    start_time_list_str = []
    for i in data:
        if re.findall('[[](.*)[.]', i):
            start_time_str = re.findall('[[](.*)[.]', i)[0]
            start_time_list_str.append(start_time_str)
    return start_time_list_str


def get_actual_time(time):
    """return wav broadcast start_time add five s"""
    return time + timedelta(minutes=1/12)  # +5秒


def get_res_count_data(data):
    """get Chinese depend on data where from res.log """
    _count_data = []
    for i in data:  # i is str
        __data = re.findall('[\u4e00-\u9fa5]+', i)
        if __data:
            _count_data.append(i)
    return _count_data


def get_last_wav(data):
    """get 240 wav"""
    wav_list = []
    for i in data:
        if re.findall('^D(.*?)wav$', i):
            res = re.findall('^D(.*?)wav$', i)
            resp = 'D' + res[0] + 'wav'
            wav_list.append(resp)

    get_wav = []  # get where circulate wav n times
    for i in range(len(wav_list)):
        if i % 2 == 0:
            get_wav.append(wav_list[i])

    last_wav = []
    for i in get_wav:
        if not re.findall('55.wav', i):
            last_wav.append(i)
    return last_wav


def get_all_time(data):
    """abandon time, if 240, return 240, else filter then return 240 time_list"""
    if len(data) == 240:  # 可以再优化
        return data
    else:
        five_time = data[12::49]
        all_start_time_list = []
        for i in data:
            if i not in five_time:
                all_start_time_list.append(i)  # 240
        return all_start_time_list


def count_run_time(func):
    """calculate run count time"""
    def run(*args, **kw):
        one_time = time.ctime()
        func(*args, **kw)
        print('[{} --- {}]'.format(one_time, time.ctime()))
    return run


def get_all_file(file_path):
    """get all files from dir"""
    all_file = os.listdir(file_path)
    return all_file


def get_all_file_path(dir_path, files):
    """join and get all path"""
    all_file_path = []
    for file in files:
        file_path = dir_path + '\\' + file
        all_file_path.append(file_path)
    return all_file_path


def get_wav_name(file_name):
    """get wav name """
    wav_list = []
    with open(file_name, 'r', encoding='utf-8') as f:
        line = f.readlines()
        for i in line:
            if '\n' == i:
                continue
            else:
                l = i.strip('\r\n')
                wav_list.append(l)
    return wav_list


if __name__ == "__main__":

    xyz = 'abc03efg004pp05'
    m = re.search('\d+$', xyz)
    print(m.group())
    print(xyz[m.start():m.end()])

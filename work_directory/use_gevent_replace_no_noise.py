# coding=utf-8

import os
import time
import gevent
from gevent import monkey
from path.test_path import Info
from scripts.log_manual import log
from scripts.text_manual import remove_txt, get_all_file, get_all_file_path


monkey.patch_all()


all_map_path = [
    r'\\192.168.200.20\backup\Algorithm\speech_data\wav\large\TJ001\wav.map',
    r'\\192.168.200.20\backup\Algorithm\speech_data\wav\large\TJ002\wav.map',
    r'\\192.168.200.20\backup\Algorithm\speech_data\wav\large\TJ002-2\wav.map',
    r'\\192.168.200.20\backup\Algorithm\speech_data\wav\large\TJ003\wav.map.new',
    r'\\192.168.200.20\backup\Algorithm\speech_data\wav\large\TJ003-2\wav.map',
    r'\\192.168.200.20\backup\Algorithm\speech_data\wav\large\TJ004\wav.map',
    r'\\192.168.200.20\backup\Algorithm\speech_data\wav\large\TJ004_split\wav.map.new',
]

all_else_path = [
    r'\\192.168.200.20\backup\Algorithm\speech_data\wav\large\TJ002\wav.map',
    r'\\192.168.200.20\backup\Algorithm\speech_data\wav\large\TJ002-2\wav.map',
    r'\\192.168.200.20\backup\Algorithm\speech_data\wav\large\TJ003-2\wav.map',
    r'\\192.168.200.20\backup\Algorithm\speech_data\wav\large\TJ004\wav.map',
]


def read_content(file_path):
    """读取txt文件，返回一个列表"""
    t = list()
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            t.append(line.strip('\n'))

    return t


def write_in_txt(file_path, data):
    """写入数据到txt文件"""
    with open(file_path, 'a+') as f:
        f.write(data + '\n')


now = lambda: time.ctime()


def get_wav(i):
    """ 从map获取wav """
    all_file_name = get_all_file(Info.old_url)
    old_file_path = get_all_file_path(Info.old_url, all_file_name)
    new_file_path = get_all_file_path(Info.new_url, all_file_name)
    content = read_content(old_file_path[i])
    one_time = now()
    for wav_path in all_map_path:
        wav_name = read_content(wav_path)
        for one_wav in wav_name:
            for one_content in content:
                if one_content == one_wav.split()[0]:
                    whole_url = None
                    try:
                        if wav_path == r'\\192.168.200.20\backup\Algorithm\speech_data\wav\large\TJ003\wav.map.new':
                            whole_url = wav_path[:-11] + 'wav\\' + one_content[5:9] + '\\' + one_content + '.wav'
                        elif wav_path == r'\\192.168.200.20\backup\Algorithm\speech_data\wav\large\TJ004_split\wav.map.new':
                            whole_url = wav_path[:-11] + 'wav\\' + one_content + '.wav'
                        elif wav_path == r'\\192.168.200.20\backup\Algorithm\speech_data\wav\large\TJ001\wav.map':
                            whole_url = wav_path[:-7] + 'wav\\' + one_content + '.wav'
                        elif wav_path in all_else_path:
                            whole_url = wav_path[:-7] + 'wav\\' + one_content[5:9] + '\\' + one_content + '.wav'
                        write_in_txt(new_file_path[i], whole_url)
                        print(whole_url, '\n', '开始时间：{}  结束时间：{}'.format(one_time, now()))
                    except Exception as e:
                        print(e)
                        log.error(e)


if __name__ == '__main__':
    """ 删除存在的txt文件 """
    remove_txt(Info.new_url)

    gevent.joinall(list(map(lambda x: gevent.spawn(get_wav, x), range(68))))


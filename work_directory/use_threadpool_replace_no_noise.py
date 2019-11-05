# coding=utf-8


import asyncio
import os
import time
import gevent
from scripts.thread_manual import MYThread
from concurrent.futures import ThreadPoolExecutor
from path.test_path import Info
from scripts.log_manual import log
from scripts.text_manual import (remove_txt,
                                 get_all_file,
                                 get_all_file_path,
                                 count_run_time
                                 )
from gevent import monkey


# monkey.patch_all()


# gevent.joinall(list(map(
#     lambda x: gevent.spawn(
#         get_wav, x,
#         all_map_path,
#         all_old_file_path,
#         all_new_file_path
#         ),
#     range(len(all_file_name)))))


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


def get_wav(i, old_file_path, map_path, new_file_path):
    """" 从map获取wav """
    content = read_content(old_file_path[i])
    one_time = now()
    for wav_path in map_path:
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


@count_run_time
def main():
    print('开始')
    all_file_name = get_all_file(Info.old_url)
    all_old_file_path = get_all_file_path(Info.old_url, all_file_name)
    all_new_file_path = get_all_file_path(Info.new_url, all_file_name)

    with ThreadPoolExecutor(max_workers=len(all_file_name)) as pool:
        print('____' * 8)
        for i in range(len(all_file_name)):
            # map中的参数为可迭代-iterable
            pool.map(get_wav, [i], [all_old_file_path], [all_map_path], [all_new_file_path])

    print('完成!!!')

    # for i in range(len(all_new_file_path)):
    #     loop.run_until_complete(get_wav(i, all_map_path, all_old_file_path, all_new_file_path))


# loop = asyncio.get_event_loop()


if __name__ == "__main__":
    main()


# async def main():
#     all_file_name = get_all_file(Info.old_url)
#     all_old_file_path = list(map(lambda x: Info.old_url + '\\' + x, all_file_name))
#     all_new_file_path = list(map(lambda x: Info.new_url + '\\' + x, all_file_name))
#
#     tasks = list(map(lambda x: asyncio.create_task(get_wav(x,
#                                                            all_map_path,
#                                                            all_old_file_path,
#                                                            all_new_file_path)
#                                                    ),
#                      range(len(all_old_file_path))))
#
#     await asyncio.wait(tasks)
#
#
# if __name__ == '__main__':
#     remove_txt(Info.new_url)
#     asyncio.run(main())


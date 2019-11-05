# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/19 9:16
# @Author  : Xiang Yu
# @File    : beijing_normalize.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


"""多线程归一化音频脚本"""


import wave
from concurrent.futures.thread import ThreadPoolExecutor

import numpy as np
import os
import struct
from path.test_path import Info
from scripts.text_manual import read_log_to_list, write_txt_once


# 目的：本脚本将file list文件夹下所有list中的语音振幅全部拉至80%处。
# 然后生成新的file list文件夹。该文件夹会生成于本脚本的目录下


def normalize(i, final_path, init_path, all_txt, new_path):
    # for txt in all_txt:
    #     if '.txt' in txt:
    f_txt_file = os.path.join(init_path, all_txt[i])
    l_wav_file = read_log_to_list(f_txt_file)
    for tmp in l_wav_file:
        # get wav name
        str_wav_name = (tmp.split('\\')[-1])[:-1]
        f_wav_name = tmp[:-1]

        f_rb = open(f_wav_name, "rb")
        # 首先载入Python的标准处理WAV文件的模块，然后调用wave.open打开wav文件，注意需要使用"rb"(二进制模式)打开文件：
        f = wave.open(f_wav_name, "rb")
        # open返回一个的是一个Wave_read类的实例，通过调用它的方法读取WAV文件的格式和数据：
        # 读取格式信息
        params = f.getparams()
        nchannels, sampwidth, framerate, nframes = params[:4]

        # getparams：一次性返回所有的WAV文件的格式信息，它返回的是一个组元(tuple)：声道数, 量化位数（byte单位）, 采样频率,
        # 采样点数, 压缩类型, 压缩类型的描述。wave模块只支持非压缩的数据，因此可以忽略最后两个信息：
        # getnchannels, getsampwidth, getframerate, getnframes等方法可以单独返回WAV文件的特定的信息。

        # 读取波形数据
        str_data = f.readframes(nframes)
        # readframes：读取声音数据，传递一个参数指定需要读取的长度（以取样点为单位），readframes返回的是二进制数据（一大堆
        # bytes)，在Python中用字符串表示二进制数据：
        f.close()

        i_range = int(nframes)
        j_x = list(map(lambda x: str_data[2 * x + 1] * 256 + str_data[2 * x], range(i_range)))

        l_wav_node = list()
        for i_x in j_x:
            # convert to signed int
            if i_x > 32768:  # means it is a negative value
                l_wav_node.append(i_x - 65536)
            else:
                l_wav_node.append(i_x)

        # 得到最大值
        int_max = np.max(l_wav_node)
        int_dst_max = 32767 * 0.8  # 将振幅拉到80%

        f_times = (int_dst_max / int_max)

        l_new_wav_node = list(map(lambda x: round(x * f_times), l_wav_node))

        l_new_wav_node_one_byte = list()
        with open(os.path.join(final_path, str_wav_name), 'wb') as f_dst_wave_file:
            f_dst_wave_file.write(f_rb.read(44))
            for i in range(len(l_new_wav_node)):
                if l_new_wav_node[i] >= 0:
                    l_new_wav_node_one_byte.append(int(l_new_wav_node[i] % 256))
                    l_new_wav_node_one_byte.append(int((l_new_wav_node[i] / 256) % 256))
                else:
                    i_new_value = l_new_wav_node[i] + 65536
                    l_new_wav_node_one_byte.append(int(i_new_value % 256))
                    l_new_wav_node_one_byte.append(int((i_new_value / 256) % 256))

                a = struct.pack('B', l_new_wav_node_one_byte[2 * i])
                f_dst_wave_file.write(a)
                a = struct.pack('B', l_new_wav_node_one_byte[2 * i + 1])
                f_dst_wave_file.write(a)
        f_rb.close()

    # 生成新的file list
    # 将原file list的txt中的语音拷贝至新的file list中，然后将路径替换掉
    for one_path_wav in l_wav_file:
        one_wav_name = one_path_wav.split("\\")[-1]
        write_txt_once(new_path, os.path.join(final_path, one_wav_name))
        print(one_wav_name)


def main():
    # 修改处1.存放最后语音的文件夹
    deposit_wav_path = r'C:\Download\wav'
    # 修改处2.原始的语音文件地址file list
    origin_list_path = r'C:\Users\xiangyu\Desktop\new_word_file\new_word_list'

    # 生成的最终file list
    # 位置位于当前路径下file_list中
    # 文件夹，存放着不同语音的文件
    if not os.path.exists(deposit_wav_path):
        os.mkdir(deposit_wav_path)

    now_path = r'C:\Users\xiangyu\Desktop\new_word_file'
    file_list_path = os.path.join(now_path, 'file_list')
    if not os.path.exists(file_list_path):
        os.mkdir(file_list_path)

    all_origin_txt_name = os.listdir(origin_list_path)

    with ThreadPoolExecutor(max_workers=len(all_origin_txt_name)) as pool:
        for i in range(len(all_origin_txt_name)):
            # map中的参数为可迭代-iterable
            pool.map(
                normalize, [i], [deposit_wav_path], [origin_list_path],
                [all_origin_txt_name], [file_list_path]
            )
        # normalize(i, set_path, origin_path, all_origin_txt_name, now_path)


if __name__ == "__main__":
    main()


# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-11 19:26
# @Author  : 余翔
# @File    : normalize_wav.py
# @Company : BEIJING INTENGINE

import os
import re
import sox
from scripts.text_manual import get_all_file, get_wav_name
from scripts.log_manual import log


if __name__ == '__main__':
    """replace all wav path"""
    file_path = "C:\\Users\\xiangyu\\Desktop\\daxian_zhengxiang_word_list_file"  # 111
    path = get_all_file(file_path)
    list_data = []
    for i in range(len(path)):
        with open(file_path + '\\' + path[i], 'r') as f:
            res = f.readlines()
            for j in res:
                data = j.strip('\n')
                list_data.append(data)
    last_wav = []
    for v in list_data:
        if v != '':
            last_wav.append(v)
    one_v = []
    for data in last_wav:
        if data not in one_v:
            one_v.append(data)
    wav_path = []
    for v in one_v:
        res = re.findall(r'.*?wav\\.*?\\', v)
        res = ''.join(res)
        wav_path.append(res)

    set_wav = set(wav_path)

    txt_list = get_all_file(file_path)
    for j in txt_list:
        txt_name = file_path + '\\' + j
        wav_list = get_wav_name(txt_name)
        for i in range(len(wav_list)):
            in_file = wav_list[i]
            in_file_path = re.findall(r'.*?wav\\.*?\\', in_file)
            in_file_path = ''.join(in_file_path)
            in_fine_name = in_file[len(in_file_path):]  # get wav name

            out_file = in_file.replace(in_file_path, '\\\\192.168.1.12\\hftest\hfwav\\daxian\\zhengxiang\\') + in_fine_name
            os.system('sox --norm=-3 {0} {1}'.format(in_file, out_file))
            log.info(out_file)

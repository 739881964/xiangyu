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
from path.test_path import Info


if __name__ == '__main__':
    """归一化音频"""
    txt_list = get_all_file(Info.da_xian_word_list)
    for j in txt_list:
        txt_name = Info.da_xian_word_list + '\\' + j
        wav_list = get_wav_name(txt_name)
        for i in range(len(wav_list)):
            in_file = wav_list[i]
            in_file_path = re.search(r'.*\\', in_file).group()
            in_fine_name = in_file[len(in_file_path):]  # get wav name
            out_file = in_file.replace(in_file_path, '\\\\192.168.1.12\\hftest\hfwav\\daxian\\zhengxiang\\')
            os.system('sox --norm=-3 {0} {1}'.format(in_file, out_file))
            log.error(out_file)

    # path = get_all_file(file_path)
    # list_data = []
    # for i in range(len(path)):
    #     with open(file_path + '\\' + path[i], 'r') as f:
    #         res = f.readlines()
    #         for j in res:
    #             data = j.strip('\n\t')
    #             list_data.append(data)
    # last_wav = []
    # for v in list_data:
    #     if v != '':
    #         last_wav.append(v)
    # one_v = []
    # for data in last_wav:
    #     if data not in one_v:
    #         one_v.append(data)
    # wav_path = []
    # for v in one_v:
    #     res = re.findall(r'.*?wav\\.*?\\', v)
    #     res = ''.join(res)
    #     wav_path.append(res)
    #
    # set_wav = set(wav_path)

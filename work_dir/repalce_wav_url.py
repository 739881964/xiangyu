# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/12 18:34
# @Author  : Xiang Yu
# @File    : repalce_wav_url.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE

from path.test_path import Info
from scripts.text_manual import *
import re
from scripts.base_path import ALL_TXT_PATH
from scripts.log_manual import log


if __name__ == '__main__':
    """替换音频前面的地址，切到本地音频，name不变"""
    all_file = get_all_file(Info.all_txt)  # txt文件个数
    all_file_path = get_all_file_path(Info.all_txt, all_file)  # txt文件路径
    new_txt_file = [Info.new_txt_file + file for file in all_file]  # 新的txt文件路径

    for num in range(len(new_txt_file)):  # 文件个数
        data = read_log_to_list(all_file_path[num])
        for one_data in data:
            one_wav_path = re.search(r'.*\\', one_data).group()
            one_wav_name = one_data[len(one_wav_path):]
            wav_info = Info.after_replace_product_path + one_wav_name
            write_txt_once(new_txt_file[num], wav_info)
            log.error(wav_info)

    pass

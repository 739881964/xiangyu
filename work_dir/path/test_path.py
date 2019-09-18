# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/12 18:04
# @Author  : Xiang Yu
# @File    : test_path.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE

from scripts.conf_manual import config


class Info(object):
    """数据作为类属性"""
    be_replaced = '/speech_data/wav/'  # 被替换
    replace_else = r'\\192.168.200.20\backup\Algorithm\speech_data\wav' + '\\'  # 替换
    local_map_file = r'C:\Users\xiangyu\Desktop\new_word_file\wav_test.map'  # 音频——.map路径
    all_txt = r'C:\Users\xiangyu\Desktop\xiangzheng\select_word_list'  # word_list 路径
    new_txt_file = r'C:\Users\xiangyu\Desktop\new_wav_url\new_url_wav' + '\\'
    after_replace_product_path = r'\\192.168.1.12\hftest\hfwav\daxian\zhengxiang' + '\\'
    da_xian_word_list = r'C:\Users\xiangyu\Desktop\daxian_zhengxiang_word_list_file'
    normalize_file_path = '\\\\192.168.1.12\\hftest\\hfwav\\daxian\\zhengxiang\\'
    new_word_list_path = r'C:\Users\xiangyu\Desktop\new_word_file\new_word_list'
    commands_file = r'C:\Users\xiangyu\Desktop\new_word_file\commands.txt'
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/12 18:04
# @Author  : Xiang Yu
# @File    : base_path.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


class Info(object):
    """数据作为类属性"""
    be_replaced = r'/speech_data/wav/'  # config.get_value('info', 'be_replaced')  # to be replaced
    replace_else = r'\\192.168.200.20\backup\Algorithm\speech_data\wav' + '\\'  # config.get_value('info', 'replace_else') + '\\'
    map_path_name = r'\\192.168.1.12\hftest\project\20190903daxian\doc\wav_test.map'  # config.get_value('info', 'map_path')
    all_txt = r'C:\Users\xiangyu\Desktop\xiangzheng\select_word_list'
    new_path = r'\\192.168.1.12\hftest\hfwav\daxian\xiaodugui' + '\\'

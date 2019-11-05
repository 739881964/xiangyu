# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/12 18:04
# @Author  : Xiang Yu
# @File    : test_path.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


"""各文件的路径，不同用户需要自己手动配置"""


class Info(object):
    """URL作为类属性"""
    be_replaced = '/speech_data/wav/'  # 被替换
    replace_else = r'\\192.168.200.20\backup\Algorithm\speech_data\wav' + '\\'  # 替换
    local_map_file = r'C:\Users\xiangyu\Desktop\new_word_file\wav_test.map'  # 音频——.map路径
    map_path = r'C:\Users\xiangyu\Desktop\new_wav_url\wav_test.map'
    all_txt = r'C:\Users\xiangyu\Desktop\xiangzheng\select_word_list'  # word_list 路径
    new_txt_file = r'C:\Users\xiangyu\Desktop\new_wav_url\new_url_wav' + '\\'
    after_replace_product_path = r'\\192.168.1.12\hftest\hfwav\daxian\zhengxiang' + '\\'
    da_xian_word_list = r'C:\Users\xiangyu\Desktop\daxian_zhengxiang_word_list_file'
    normalize_file_path = r'\\192.168.1.12\hftest\hfwav\daxian\zhengxiang' + '\\'
    new_word_list_path = r'C:\Users\xiangyu\Desktop\new_word_file\new_word_list'
    commands_file = r'/Users/yuxiang/Desktop/new_word_file/word_list.txt'
    command_file = r'C:\Users\xiangyu\Desktop\new_word_file\words.txt'
    after_normalize_wav_path = r'C:\Users\xiangyu\Desktop\new_word_file\normalize_wav'
    replace_noise_wav = r'\\192.168.200.20\backup\Algorithm\speech_data\wav'
    other_word_list_path = r'C:\Users\xiangyu\Desktop\word_list_selected'
    after_replace_no_noise_wav = r'C:\Users\xiangyu\Desktop\no_noise_word_list'
    beijing_url = r'\\192.168.200.20\share\Exchange\hftest\wav\20190925jieshifeitong' + '\\'
    xiaojie_path = r'C:\Users\xiangyu\Desktop\new_word_file\xiaojie_word_list'
    old_url = r'C:\Users\xiangyu\Desktop\new_word_file\new_word_list'
    new_url = r'C:\Users\xiangyu\Desktop\new_word_file\after_replace_no_noise_wav'
    bin_path = r'C:\Users\xiangyu\Documents\WXWork\1688854109245460\Cache\File\2019-09\luyin\luyin'


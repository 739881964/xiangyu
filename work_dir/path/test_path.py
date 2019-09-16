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
    be_replaced = config.get_value('info', 'be_replaced')  # 被替换
    replace_else = config.get_value('info', 'replace_else') + '\\'  # 替换
    map_path_name = config.get_value('info', 'map_path')  # 音频——.map路径
    all_txt = config.get_value('info', 'all_txt')  # word_list 路径
    new_txt_file = config.get_value('info', 'new_txt_file') + '\\'
    after_replace_product_path = config.get_value('info', 'product_path') + '\\'
    da_xian_word_list = config.get_value('info', 'da_xian_word_list')

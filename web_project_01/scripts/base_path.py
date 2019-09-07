#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-07 00:18
# @Author  : Xiang Yu
# @File    : bid_data.py
# @company : BEIJING-INTENGINE

import os


BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 根目录

CASES_PATH = os.path.join(BASE_PATH, 'cases')  # 测试用例目录

CACHE_PATH = os.path.join(CASES_PATH, '.pytest_cache')  # 缓存目录

LOGS_DIR_PATH = os.path.join(BASE_PATH, 'logs')  # 日志目录

LOG_FILE_PATH = os.path.join(LOGS_DIR_PATH, 'test_log.txt')  # 日志文件目录

CONFS_DIR_PATH= os.path.join(BASE_PATH, 'confs')  # 日志目录

CONFS_FILE_PATH = os.path.join(CONFS_DIR_PATH, 'test.cfg')  # 日志文件目录

LOG_IMG_DIR = os.path.join(BASE_PATH, 'log_img')
if not os.path.exists(LOG_IMG_DIR):  # if not exists then create img directory
    os.mkdir(LOG_IMG_DIR)

pass

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-04 22:06
# @Author  : Yu xiang
# @File    : base_path.py

import os
# 文件, 数据路径 -> py文件


# 根目录
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 日志目录
LOGS_DIR_PATH = os.path.join(BASE_PATH, 'logs')

# 日志文件
LOGS_FILE_PATH = os.path.join(LOGS_DIR_PATH, 'log.txt')

# 配置文件目录
CONFS_DIR_PATH = os.path.join(BASE_PATH, 'confs')

# 配置文件
CONFS_FILE_PATH = os.path.join(CONFS_DIR_PATH, 'test.cfg')

# 测试用例目录
TEST_CASES_PATH = os.path.join(BASE_PATH, 'CASES')

# 缓存目录
CACHE_FILE_PATH = os.path.join(TEST_CASES_PATH, '.pytest_cache')

# 错误截图目录
LOG_IMG_DIR = os.path.join(BASE_PATH, 'log_img')
if not os.path.exists(LOG_IMG_DIR):  # 不存在就创建截图日志目录
    os.mkdir(LOG_IMG_DIR)

pass

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-04 22:06
# @Author  : Yu xiang
# @File    : base_path.py

import os


BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOGS_FILE_PATH = os.path.join(BASE_PATH, 'log.txt')

CONFS_FILE_PATH = os.path.join(BASE_PATH, 'test.cfg')

LOG_IMG_DIR = os.path.join(BASE_PATH, 'log_img')
if not os.path.exists(LOG_IMG_DIR):  # if not exists then create img directory
    os.mkdir(LOG_IMG_DIR)

pass

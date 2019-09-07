#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-06 23:42
# @Author  : Yu xiang
# @File    : operate_test_case.py

import unittest
from scripts.base_path import CASES_PATH, CACHE_PATH
import shutil
import os
import time


if __name__ == '__main__':  # 运行测试用例
    """如果存在缓存文件，即删除"""
    if os.path.exists(CACHE_PATH):
        shutil.rmtree(CACHE_PATH)

    time.sleep(1)
    suite = unittest.defaultTestLoader.discover(CASES_PATH)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

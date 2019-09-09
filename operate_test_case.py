#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-05 22:45
# @Author  : Yu xiang
# @File    : test_login.py

import unittest
from scripts.base_path import TEST_CASES_PATH, CACHE_FILE_PATH
import os
import shutil
import time
import pytest


if __name__ == "__main__":
    """执行用例之前删除测试用例下的缓存文件目录"""
    if os.path.exists(CACHE_FILE_PATH):
        shutil.rmtree(CACHE_FILE_PATH)

    pytest.main()


# if __name__ == "__main__":
#     """执行用例之前删除测试用例下的缓存文件目录"""
#     if os.path.exists(CACHE_FILE_PATH):
#         shutil.rmtree(CACHE_FILE_PATH)
#
#     time.sleep(1)
#     suite = unittest.defaultTestLoader.discover(TEST_CASES_PATH)
#     runner = unittest.TextTestRunner(verbosity=2)
#     runner.run(suite)


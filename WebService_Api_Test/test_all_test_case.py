# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:xiangyu
# phone：19942429056
# datetime:2019/9/4 10:45
# software: PyCharm


import unittest
from .libs.HTMLTestRunnerNew import HTMLTestRunner
from .scripts.base_path import CASES_PATH, REPORTS_PATH, USER_CONF_FILE_PATH
from datetime import datetime
import cases.three_mobile_register_request_case as test
import os


if __name__ == '__main__':

    # 存在配置文件就不注册三个账号
    if not os.path.exists(USER_CONF_FILE_PATH):
        test.generate_mobile()

    suite = unittest.defaultTestLoader.discover(CASES_PATH)
    path = 'C:\\Users\\xiangyu\\Desktop\\test_files\WebService_Api_Test\\reports\\result_01.html'
    result_path = REPORTS_PATH + '\\' + datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S") + '.html'
    with open(path, 'wb') as f:
        runner = HTMLTestRunner(stream=f,
                                title='接口测试报告',
                                description='接口测试执行结果',
                                tester='余翔')
        runner.run(suite)

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-05 22:45
# @Author  : Yu xiang
# @File    : log_manual.py
# @Company : BEIJING INTENGINE

from scripts.base_path import LOG_FILE_PATH
import logging
from scripts.conf_manual import config


class LogManual(object):
    def __init__(self):
        # define log obj name and log level
        self.log = logging.getLogger(config.get_value('log', 'log_name'))
        self.log.setLevel(config.get_value('log', 'log_lv'))

        # add log output form file and console
        file_log = logging.FileHandler(LOG_FILE_PATH)
        console_log = logging.StreamHandler()

        # add output's log level
        file_log.setLevel(config.get_value('log', 'file_lv'))
        console_log.setLevel(config.get_value('log', 'console_lv'))

        # log format
        more_log = logging.Formatter(config.get_value('log', 'more'))
        simple_log = logging.Formatter(config.get_value('log', 'simple'))

        # binding output format
        file_log.setFormatter(more_log)
        console_log.setFormatter(simple_log)

        self.log.addHandler(file_log)
        self.log.addHandler(console_log)

    def get_log(self):
        return self.log


log = LogManual().get_log()


if __name__ == '__main__':
    log.info('this is a info log')
    log.error('this is a error log')
    num = range(10)
    print(num)
    for i in range(10):
        print(i)

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-05 22:45
# @Author  : 余翔
# @File    : twice_package.py
# @Company : BEIJING INTENGINE

from scripts.conf_manual import ConfManual, config
from scripts.excel_manual import ExcelManual
from scripts.log_manual import log
from scripts.text_manual import *


class Packages(object):
    """二次封装excel，log，text，conf类"""
    excel_path = config.get_value('', '')
    sheet_name = config.get_value('', '')
    conf_path = config.get_value('', '')

    def __init__(self, excel_path, sheet_name, conf_path):
        self.excel_path = excel_path
        self.sheet_name = sheet_name
        self.conf_path = conf_path

    def _pass(self):
        pass
        # excel = ExcelManual()
        # conf = ConfManual()

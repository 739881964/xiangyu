# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-05 22:45
# @Author  : Yu xiang
# @File    : conf_manual.py
# @Company : BEIJING INTENGINE

from configparser import ConfigParser
from scripts.base_path import CONF_FILE_PATH


class ConfManual(object):
    """
    配置文件 *.conf 读写类
    """
    def __init__(self, file_path):
        self.file_path = file_path
        self.config = ConfigParser()
        self.config.read(self.file_path, encoding='utf-8')

    def get_value(self, sess, opt):  # str
        return self.config.get(sess, opt)

    def get_int(self, sess, opt):  # int
        return self.config.getint(sess, opt)

    def get_float(self, sess, opt):  # float
        return self.config.getfloat(sess, opt)

    def get_boolean(self, sess, opt):  # bool
        return self.config.getboolean(sess, opt)

    def get_eval(self, sess, opt):
        return eval(self.get_value(sess, opt))

    @staticmethod
    def write_conf(file_name, data):
        configs = ConfigParser()

        for i in data:
            configs[i] = data[i]

        with open(file_name, 'a') as f:
            configs.write(f)


config = ConfManual(CONF_FILE_PATH)


if __name__ == '__main__':
    __data = {
        'a': {1: 2}
    }
    config.write_conf(CONF_FILE_PATH, __data)

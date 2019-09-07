#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-07 00:18
# @Author  : Xiang Yu
# @File    : bid_data.py
# @company : BEIJING-INTENGINE

from configparser import ConfigParser
from scripts.base_path import CONFS_FILE_PATH


class ConfigClass(object):

    def __init__(self, file_path):
        self.file_path = file_path
        self.config = ConfigParser()
        self.config.read(self.file_path, encoding='utf-8')

    def get_value(self, sess, opt):
        return self.config.get(sess, opt)

    def get_int(self, sess, opt):
        return self.config.getint(sess, opt)

    def get_float(self, sess, opt):
        return self.config.getfloat(sess, opt)

    def get_eval(self, sess, opt):
        return eval(self.get_value(sess, opt))

    def get_boolean(self, sess, opt):
        return self.config.getboolean(sess, opt)

    @staticmethod
    def write_in_cfg(data, fp):
        configer = ConfigParser()
        for key in data:
            configer[key] = data[key]

        with open(fp, 'w') as f:
            configer.write(f)


config = ConfigClass(CONFS_FILE_PATH)


if __name__ == '__main__':
    pass
    # config = ConfigClass('cfg.cfg')
    # datas = {'excel': {'res': 6}}
    # config.write_in_cfg(datas, 'cfg.cfg')
    # a = config.get_value('excel', 'res_col')
    # print(a)

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/12 12:41
# @Author  : Xiang Yu
# @File    : thread_manual.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


"""thread/process"""


import threading
import multiprocessing
from time import ctime
from queue import Queue


class MYThread(threading.Thread):
    """创建一个线程类继承于threading"""
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name
        # self.q = []

    def run(self):
        self.func(*self.args)


class MYProcess(multiprocessing.Process):
    """创建一个进程类继承于process"""
    def __init__(self, func, args, name=''):
        multiprocessing.Process.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)

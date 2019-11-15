# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/14 15:35
# @Author  : Xiang Yu
# @File    : local_threading.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE

import time
import threading


try:
    import greenlet
    get_ident = greenlet.getcurrent
except:
    get_ident = threading.get_ident


class Local(object):

    def __init__(self):
        object.__setattr__(self, 'DIC', {})

    def __getattr__(self, item):
        ident = get_ident()
        if ident in self.DIC:
            return self.DIC[ident].get(item)
        return None

    def __setattr__(self, key, value):
        ident = get_ident()
        if ident in self.DIC:
            self.DIC[ident][key] = value
        else:
            self.DIC[ident] = {key: value}


local = Local()
local.xxx = 123
# print(local.xxx, local)


if __name__ == "__main__":
    def task(t):
        local.id = t
        print(local.id, t)
        time.sleep(1)

    for i in range(10):
        T = threading.Thread(target=task, args=(i, ))
        T.start()


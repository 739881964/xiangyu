# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/12 12:34
# @Author  : Xiang Yu
# @File    : run_threading.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE

from scripts.thread_manual import MYThread
from time import sleep, ctime

loop = [1, 2]

def run_threading(n, one_time):
    print('start time case', n, 'at:', ctime())
    sleep(one_time)
    print('case', n, 'done at:', ctime())


def main():
    print('all start at:', ctime())
    threads = []
    loops = range(len(loop))

    for i in loops:  # create threading
        t = MYThread(run_threading, (i, loop[i]), run_threading.__name__)
        threads.append(t)

    for i in loops:  # start all threading
        threads[i].start()

    for i in loops:  # wait all threading finish
        threads[i].join()

    print('all done at:', ctime())


if __name__ == "__main__":
    main()

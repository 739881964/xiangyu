# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/30 12:10
# @Author  : Xiang Yu
# @File    : asyncio_example.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


import asyncio
import time
import gevent
from gevent import monkey


monkey.patch_all()


def func(n):
    gevent.sleep(0.5)
    print('hello China', n)
    gevent.sleep(0.5)
    print('hello Beijing', n + 1)


# 定义异步函数
async def hello():
    await asyncio.sleep(1)
    print('Hello World:%s' % time.time())


def run():
    for i in range(5):
        loop.run_until_complete(hello())


async def foo():
    print('start foo')
    await asyncio.sleep(1)
    print('----end foo')


loop = asyncio.get_event_loop()


def main():
    event_list = list(map(lambda x: gevent.spawn(func, x), range(3)))
    gevent.joinall(event_list)


if __name__ =='__main__':
    # asyncio.run(foo())
    # gevent.joinall([gevent.spawn(func), gevent.spawn(func)])
    main()

